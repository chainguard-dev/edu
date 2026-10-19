---
title: "Create an assumable identity for HCP Terraform"
date: 2026-10-19T14:34:54+00:00
lastmod: 2026-10-19T14:34:54+00:00
linktitle: "HCP Terraform"
description: "Authenticate the Chainguard Terraform provider in HCP Terraform with a workload identity token, then manage your other Chainguard identities in Terraform."
type: "article"
draft: false
tags: ["Platform", "Procedural"]
images: []
weight: 85
---

HCP Terraform can authenticate the [Chainguard Terraform provider](/platform/administration/terraform-provider/) without a stored credential. For each plan and apply, HCP Terraform issues a short-lived workload identity token. The provider exchanges that token for a Chainguard token by assuming an [assumable identity](/platform/administration/assumable-ids/assumable-ids/) that trusts your workspace.

The provider can't create the identity it needs to sign in, so you create that first identity once with `chainctl`. This guide calls it the *bootstrap identity*. After it exists, the workspace can manage your other Chainguard identities and role bindings in Terraform.

{{< note >}}
The provider reads HCP Terraform's workload identity token starting in version 0.5.4. Earlier versions can't authenticate this way in HCP Terraform.
{{< /note >}}

## Prerequisites

To complete this guide, you need the following:

* An HCP Terraform workspace that runs plans and applies remotely. The workspace can use any workflow: VCS-driven, CLI-driven, or API-driven.
* [`chainctl` installed](/platform/chainctl-usage/how-to-install-chainctl/) on your local machine, signed in as a user who can create identities and role bindings in your Chainguard organization.

## How the token exchange works

The exchange uses two kinds of token, and the provider accepts only one of them as input:

* **A workload identity token** is an OpenID Connect (OIDC) token that HCP Terraform issues. Its issuer is `https://app.terraform.io`. This is the token the provider exchanges.
* **A Chainguard token** is the token that `chainctl auth login` caches and that `chainctl auth token` prints. Its issuer is Chainguard. It's the *result* of an exchange, so the provider can't exchange it again.

When a workspace sets the `TFC_WORKLOAD_IDENTITY_AUDIENCE` environment variable, HCP Terraform puts a workload identity token in the `TFC_WORKLOAD_IDENTITY_TOKEN` environment variable of every plan and apply. The provider reads that variable, presents the token to Chainguard, and receives a Chainguard token for the identity the token matches.

## Find your workspace details

The bootstrap identity trusts tokens from one workspace. HCP Terraform puts the workspace's details in each token's subject claim, which has the following format:

```
organization:<hcp-organization>:project:<project>:workspace:<workspace>:run_phase:<plan-or-apply>
```

Collect these values:

* Your HCP Terraform organization name.
* The workspace name.
* The workspace ID, which starts with `ws-`. In HCP Terraform, open the workspace, go to **Settings > General**, and copy the **ID**.

Workspace and project names can change, but the workspace ID can't. The identity in the next section matches the ID as well as the names, so renaming a different workspace to this workspace's name doesn't grant it access. If you rename this workspace or your HCP Terraform organization, update the identity's subject pattern to match, or the workspace loses access.

## Create the bootstrap identity

Run the following command, replacing each placeholder with your own values. `<organization>` is your Chainguard organization, not your HCP Terraform organization:

```sh
chainctl iam identities create hcp-terraform \
  --parent=<organization> \
  --identity-issuer=https://app.terraform.io \
  --subject-pattern='^organization:<hcp-organization>:project:[^:]+:workspace:<workspace>:run_phase:(plan|apply)$' \
  --claim-pattern='terraform_workspace_id:^<workspace-id>$' \
  --role=owner
```

This command does the following:

* `--identity-issuer` accepts only tokens that HCP Terraform issued.
* `--subject-pattern` accepts both the plan phase and the apply phase. HCP Terraform issues a separate token for each phase, and the subject ends in `run_phase:plan` or `run_phase:apply`. A pattern that matches only one phase fails the other one. The `[^:]+` part matches any project name.
* `--claim-pattern` also requires the workspace ID.
* `--role=owner` lets the workspace create, update, and delete identities and role bindings. `owner` is the only built-in role that can do all of these. To grant less, [create a custom role](/platform/administration/iam-organizations/roles-role-bindings/roles-role-bindings/) with only the capabilities your configuration needs, and bind the identity to it instead.

The command prints the new identity's ID, which has the form `<organization-id>/<identity-suffix>`. Copy it for the next steps. To find it later, run `chainctl iam identities list --parent=<organization>`.

## Configure the workspace

In HCP Terraform, open the workspace and go to **Variables**. Add an **Environment variable** with the following values:

* **Key:** `TFC_WORKLOAD_IDENTITY_AUDIENCE`
* **Value:** `https://issuer.enforce.dev`

The value sets the token's audience to Chainguard's issuer, which is the audience the exchange accepts. Make the variable an environment variable, not a Terraform variable. HCP Terraform issues a workload identity token only when an environment variable sets the audience.

If another tool in the workspace already uses `TFC_WORKLOAD_IDENTITY_AUDIENCE` with a different audience, name the variable `TFC_WORKLOAD_IDENTITY_AUDIENCE_CHAINGUARD` instead. HCP Terraform then issues a second token in `TFC_WORKLOAD_IDENTITY_TOKEN_CHAINGUARD`, and the provider uses that token in preference to the untagged one.

## Configure the provider

In your Terraform configuration, set `identity_id` to the bootstrap identity's ID:

```hcl
terraform {
  required_providers {
    chainguard = {
      source  = "chainguard-dev/chainguard"
      version = ">= 0.5.4"
    }
  }
}

provider "chainguard" {
  login_options {
    identity_id = "<identity-id>"
  }
}
```

Don't set `identity_token`. If you set it, the provider uses that value instead of HCP Terraform's token. Don't set `disabled = true` either, because it stops the provider from exchanging any token.

## Verify the identity

A provider block on its own doesn't make the provider sign in. To confirm that the exchange works, add a data source that reads your organization, and an output that shows its ID:

```hcl
data "chainguard_group" "org" {
  parent_id = "/"
  name      = "<organization>"
}

output "org_id" {
  value = data.chainguard_group.org.id
}
```

Start a run in HCP Terraform. If the plan shows a value for `org_id`, the workspace signed in as the bootstrap identity. If the plan fails, refer to [Troubleshooting](#troubleshooting).

## Manage other identities in Terraform

With the bootstrap identity in place, the workspace can manage the rest of your identities. For example, the following configuration creates an identity that a GitHub Actions workflow can assume, and lets it pull images:

```hcl
resource "chainguard_identity" "github_ci" {
  parent_id   = data.chainguard_group.org.id
  name        = "github-ci"
  description = "Pulls images from GitHub Actions workflows in one repository."

  claim_match {
    issuer          = "https://token.actions.githubusercontent.com"
    subject_pattern = "^repo:<github-owner>/<github-repo>:.*$"
  }
}

data "chainguard_role" "puller" {
  name = "registry.pull"
}

resource "chainguard_rolebinding" "github_ci_pull" {
  identity = chainguard_identity.github_ci.id
  group    = data.chainguard_group.org.id
  role     = data.chainguard_role.puller.items[0].id
}
```

Keep the bootstrap identity out of this configuration. If the workspace manages the identity it signs in with, a change to that identity can lock the workspace out, and you would need `chainctl` to recover it.

If several workspaces need Chainguard access, you don't need a bootstrap identity for each one. Keep the bootstrap identity in one workspace that manages identities, and have it create a narrower identity for each of the other workspaces, using the same issuer and subject pattern format with that workspace's names.

## Troubleshooting

Find the error message from your run in the following sections. To see which sign-in path the provider took, set the `TF_LOG` environment variable to `INFO` on the workspace and run again.

### Unsupported audience

```
rpc error: code = PermissionDenied desc =
verify token: rpc error: code = PermissionDenied desc = unsupported
audience(s) [https://console-api.enforce.dev]
```

The provider received a Chainguard token, such as the output of `chainctl auth token`, instead of a workload identity token. A Chainguard token can't be exchanged again. Remove the Chainguard token from `identity_token`, from the `TF_CHAINGUARD_IDENTITY_TOKEN` environment variable, and from any Terraform variable that feeds them, and let the provider read HCP Terraform's token.

If the audience in the message is something other than a Chainguard address, the workload identity token has the wrong audience. Check that `TFC_WORKLOAD_IDENTITY_AUDIENCE` is `https://issuer.enforce.dev`.

### Automatic auth disabled

```
rpc error: code = Unauthenticated desc = automatic auth disabled
```

The provider configuration sets `disabled = true` in `login_options`. That setting stops the provider from getting a new Chainguard token by any method, including a token exchange. Remove it.

### Invalid subject

```
token has invalid subject
```

The token came from HCP Terraform, but it doesn't match the bootstrap identity. Check the following:

* The subject pattern matches both `run_phase:plan` and `run_phase:apply`.
* The organization and workspace names in the pattern match the workspace, including case.
* The workspace ID in the claim pattern is this workspace's ID.

To see the identity's current claim match, run `chainctl iam identities describe <identity-id> -o json`.

### The provider tries to open a browser

If the run log shows that the provider is launching a browser login flow, or the run waits until it times out, the provider found no token to exchange. Check that the workspace has `TFC_WORKLOAD_IDENTITY_AUDIENCE` as an environment variable, and that the configuration requires provider version 0.5.4 or later.

## Learn more

* [Introduction to the Chainguard Terraform provider](/platform/administration/terraform-provider/)
* [Overview of assumable identities](/platform/administration/assumable-ids/assumable-ids/)
* [HCP Terraform workload identity tokens](https://developer.hashicorp.com/terraform/cloud-docs/workspaces/dynamic-provider-credentials/workload-identity-tokens), which describes the token's claims
* [Manually generating workload identity tokens](https://developer.hashicorp.com/terraform/cloud-docs/workspaces/dynamic-provider-credentials/manual-generation), which covers the audience variables
