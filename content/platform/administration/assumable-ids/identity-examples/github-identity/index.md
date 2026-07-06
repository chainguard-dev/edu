---
title : "Create an Assumable Identity for a GitHub Actions Workflow"
linktitle: "GitHub Actions"
aliases:
- /chainguard/chainguard-enforce/iam-groups/enforce-github-identity/
- /chainguard/chainguard-enforce/authentication/identity-examples/enforce-github-identity/
- /chainguard/administration/iam-organizations/identity-examples/github-identity/
- /chainguard/administration/assumable-ids/identity-examples/github-identity/
lead: ""
description: "Tutorial outlining how to create a Chainguard identity that can be assumed by a GitHub Actions workflow."
type: "article"
date: 2023-05-04T08:48:45+00:00
lastmod: 2025-11-28T06:00:00+00:00
draft: false
tags: ["Chainguard Containers"]
images: []
weight: 005
---

Chainguard's [*assumable identities*](/chainguard/administration/iam-organizations/assumable-ids/)
are identities that can be assumed by external applications or workflows in
order to perform certain tasks that would otherwise have to be done by a human.
For instance, an assumable identity can be used to allow a GitHub Actions
workflow to pull images from `cgr.dev` without a static pull token.

This tutorial outlines how to create an identity, and then create a GitHub Actions workflow that will assume the identity to interact with Chainguard resources.

## Prerequisites

To complete this guide, you will need the following.

* One of:
  * `chainctl` — the Chainguard command line interface tool — installed on your local machine. Follow our guide on [How to Install `chainctl`](/chainguard/chainctl-usage/how-to-install-chainctl/) to set this up.
  * `terraform` installed on your local machine. Terraform is an Infrastructure as Code tool which this guide will use to create various cloud resources. Follow [the official Terraform documentation](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli) for instructions on installing the tool.
* A GitHub repository you can use for testing out GitHub identity federation. To complete this guide, you must have permissions to create GitHub Actions on this testing repo.

## Creating an Identity

### Chainctl

This command creates an identity that can be assumed by workflows in the
`my-org/repo-name` repository. The identity is bound to the `registry.pull`
role.

```sh
chainctl iam identities create github my-identity-name \
    --github-repo=my-org/repo-name \
    --role registry.pull
```

You can also include the `--github-ref` flag to restrict it to workflows that
run from a specific branch. For instance, the `main` branch.

```sh
chainctl iam identities create github my-identity-name \
    --github-repo=my-org/repo-name \
    --github-ref=refs/heads/main \
    --role registry.pull
```

Regex is also available. For example creating an identity that can be assumed by multiple repositories and multiple branches.

```sh
chainctl iam identitie create github my-identity-name \
    --github-repo='my-org/.*' \
    --github-refs='refs/heads/main|master'
    --role registry.pull
```

This will return the identity's
[UIDP (unique identity path)](/chainguard/administration/cloudevents/events-reference/#uidp-identifiers).
Note this value down, as you'll need it to set up the GitHub Actions workflow.

If you need to retrieve the UIDP later on, you can always run the following
`chainctl` command to list the identity.

```sh
chainctl iam identities list --name=my-identity-name
```

### Terraform

Alternatively, you could create the identity with the [Chainguard Terraform
provider](https://registry.terraform.io/providers/chainguard-dev/chainguard/latest).

Substitute your Chainguard organization name, GitHub organization and GitHub
repository for `<org-name>`, `<github-org>` and `<github-repo>`, respectively.

```hcl
data "chainguard_group" "org" {
  name = "<org-name>"
}

resource "chainguard_identity" "my_identity_name" {
  parent_id   = data.chainguard_group.org.id
  name        = "my-identity-name"

  claim_match {
    issuer  = "https://token.actions.githubusercontent.com"
    subject = "repo:<github-org>/<github-repo>:ref:refs/heads/main"
  }
}

data "chainguard_role" "registry_pull" {
  name = "registry.pull"
}

resource "chainguard_rolebinding" "my_identity_name_registry_pull" {
  identity = chainguard_identity.my_identity_name.id
  group	= data.chainguard_group.org.id
  role 	= data.chainguard_role.registry_pull.items[0].id
}

output "my_identity_name_id" {
  value = chainguard_identity.my_identity_name.id
}
```

In this example the `chainguard_identity.my_identity_name` resource defines an
identity in your organization that can be assumed by a GitHub workflow that
matches the claims in the `claim_match` block.

The `chainguard_rolebinding.my_identity_name_registry_pull` resource binds the
`registry.pull` role to the identity.

The `my_identity_name_id` output provides the identity's [UIDP (unique identity
path)](/chainguard/administration/cloudevents/events-reference/#uidp-identifiers).
You'll need this value to set up the GitHub Actions workflow.

## Creating and Testing a GitHub Actions Workflow

This example workflow definition assumes an identity with the [`setup-chainctl`](https://github.com/chainguard-dev/setup-chainctl)
GitHub Action, lists repositories with `chainctl` and pulls an
image from `cgr.dev`.

Commit this workflow to the `main` branch of your repository as
`.github/workflows/assume-and-explore.yaml`, substituting `<identity-id>` with
the UIDP of the assumable identity you created in the previous step and
`<org-name>` with the name of your Chainguard organization.

```yaml
name: Assume and Explore

on:
  workflow_dispatch: {}

jobs:
  assume-and-explore:
    name: actions assume example

    permissions:
      id-token: write

    runs-on: ubuntu-latest
    steps:

    - uses: chainguard-dev/setup-chainctl@main
      with:
        identity: <identity-id>

    - run: |
        chainctl image repo list --parent=<org-name>

    - run: |
        docker pull cgr.dev/<org-name>/example-image:latest
```

Once its committed, you can trigger the workflow by navigating to
`Actions > Assume And Explore` from the home page of your repository and
selecting `Run workflow`.

## Learn more

For more information about how assumable identities work in Chainguard, check out our [conceptual overview of assumable identities](/chainguard/administration/iam-organizations/assumable-ids/). Additionally, the Terraform documentation includes a section on [recommended best practices](https://developer.hashicorp.com/terraform/cloud-docs/recommended-practices) which you can refer to if you'd like to build on the provided Terraform configuration for a production environment. Likewise, for more information on using GitHub Actions, we encourage you to check out the [official documentation on the subject](https://docs.github.com/en/actions).
