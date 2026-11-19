---
aliases:
- /chainguard/administration/iam-organizations/verified-orgs/
title : "Verified organizations"
lead: ""
description: "What a verified organization is, how Enterprise, Starter, and Team organizations get verified, and what verification changes"
type: "article"
date: 2023-08-15T14:22:23-07:00
lastmod: 2026-11-19T15:28:23+00:00
draft: false
tags: ["Chainguard Console", "Conceptual"]
images: []
menu:
  docs:
    parent: "iam-organizations"
weight: 30
toc: true
---

The Chainguard platform organizes resources in a hierarchical structure called [IAM organizations](/platform/administration/iam-organizations/overview-of-chainguard-iam-model/). A customer typically uses one root-level _organization_ to manage its Chainguard resources.

## About verified organizations

A verified organization is a root-level organization whose name Chainguard has confirmed and reserved for you. Only one organization on the Chainguard platform can hold a given verified name. Because of that, you can use the name anywhere you would otherwise use the organization's unique ID.

Verifying your organization lets you:

- Pull container images from a readable path, such as `cgr.dev/example.com/python`, instead of `cgr.dev/<org_id>/python`.
- Log in through your [custom identity provider](/platform/administration/custom-idps/custom-idps/) by entering your organization name. This works in `chainctl`, the Chainguard Console, and the [Terraform provider](/platform/administration/terraform-provider/), so users don't need your identity provider's ID.
- [Request new container images](/chainguard/containers/reference/request-resources/) in the Chainguard Console.

## How an organization gets verified

How your organization gets verified depends on how it was created. Verification isn't a feature of a [plan](/get-started/self-serve/plans/), and you can't verify an organization yourself.

| How the organization was created | Verified? | Organization name |
| --- | --- | --- |
| Chainguard set it up for an Enterprise customer | Yes. Chainguard verifies it manually, typically during onboarding. | Agreed with Chainguard, usually your company's domain |
| You signed up for Chainguard Starter with a business email address | Yes, automatically at signup | Your email domain, such as `example.com` |
| You signed up for Chainguard Starter with a personal email address, such as a Gmail address | No | A name you choose, which can't look like a domain name |

Chainguard decides this once, when the organization is created. [Upgrading to Chainguard Team](/get-started/self-serve/upgrade-team/) keeps the organization's verification status: a verified Starter organization stays verified on Team, and an unverified one stays unverified.

### Unverified Starter and Team organizations

An unverified Starter or Team organization keeps its plan's images, libraries, and other products. It differs from a verified organization in these ways:

- Its registry path uses the organization's ID, such as `cgr.dev/<org_id>/python`, instead of a name.
- It isn't tied to an email domain, which changes who you can invite and how compute is metered. For details, refer to [Plan limits](/get-started/self-serve/plans/#plan-limits).

Chainguard doesn't yet offer a way to verify an existing Starter or Team organization. If you plan to invite colleagues or want to pull images by name, [sign up for Chainguard Starter](/get-started/self-serve/sign-up-starter/) with a business email address. That creates a new organization, separate from any organization you created with a personal address.

## Check whether your organization is verified

You can check whether your organization is verified using [`chainctl`](/platform/chainctl-usage/how-to-install-chainctl/). The following command uses [`jq`](https://jqlang.org/) to filter the JSON output down to each organization's name and verification status.

```sh
chainctl iam organization ls -o json | jq '.items[] | {name, verified}'
```

A verified organization has the field `"verified": true`. The output for an unverified organization doesn't include the `verified` field, so `jq` prints `null`.

```json
{
  "name": "example.com",
  "verified": true
}
{
  "name": "example-unverified-org",
  "verified": null
}
```

If you're an Enterprise customer and your organization isn't verified, ask your Chainguard account team or support to verify it. For a Starter or Team organization, refer to [Unverified Starter and Team organizations](#unverified-starter-and-team-organizations).

## Log in with your organization name

If you've configured a [custom identity provider](/platform/administration/custom-idps/custom-idps/) and your organization is verified, you can select your identity provider by entering your organization name when you log in.

When authenticating with `chainctl`, pass the `--org-name` flag. This example uses the organization name `example.com`.

```sh
chainctl auth login --org-name example.com
```

As an alternative, you can set the organization name by editing the `chainctl` configuration file with the following command.

```sh
chainctl config edit
```

This command opens your system's default text editor, where you can edit the local `chainctl` configuration. Add the following lines to this file.

```yaml
default:
  org-name: example.com
```

You can also set this with a single command using the `chainctl config set` subcommand, as in this example.

```sh
chainctl config set default.org-name example.com
```

After you set the organization name, `chainctl auth login` uses the configured identity provider automatically.

When you log in to the Chainguard Console, the Console detects your organization name from your email address in most cases. If your organization name doesn't match your email domain, enter it manually to select your custom identity provider.

## Pull images by organization name

If your organization has access to Chainguard Containers, its container images are in a private repository within the Chainguard registry. You can pull them from `cgr.dev/<org_id>/<image_name>`, where `<org_id>` is your organization's unique ID. After Chainguard verifies your organization, you can use its name in place of the ID. For example, if your verified organization is named `example.com`, you can pull private images with a command like `docker pull cgr.dev/example.com/<image_name>`.

## Restrictions for verified organizations

A verified organization's name works interchangeably with its unique ID. Changing the name can break image pulls from your organization's repository within the Chainguard registry, and it can break authentication for users who log in to your custom identity provider by organization name. For that reason, you can't rename a verified organization yourself. To rename it, contact support.
