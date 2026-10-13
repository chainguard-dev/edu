---
aliases:
- /chainguard/administration/terraform-provider/
title: "Introduction to the Chainguard Terraform provider"
linktitle: "Terraform provider"
type: "article"
description: "An introduction to working with the Chainguard Terraform provider"
date: 2024-01-28T15:56:52-07:00
lastmod: 2026-10-09T00:00:00+00:00
draft: false
tags: ["Platform", "Procedural"]
images: []
menu:
  docs:
    parent: "administration"
toc: true
weight: 50
---

[Terraform](https://www.terraform.io/) is an infrastructure as code tool that lets you declaratively configure resources in cloud providers like AWS and GCP, SaaS platforms, and many other API-driven environments. Third-party developers write [Terraform providers](https://developer.hashicorp.com/terraform/language/providers) so that Terraform can manage resources in their environments.

[The Chainguard Terraform provider](https://registry.terraform.io/providers/chainguard-dev/chainguard/latest) lets you manage resources on the Chainguard Platform, such as identities, role-bindings, custom roles, and more. This guide shows how to configure the provider and use it to manage your Chainguard resources.

## Prerequisites

To use the Chainguard Terraform provider, [install Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli) on your local machine.

This guide also uses [`chainctl`](/platform/chainctl-usage/how-to-install-chainctl/) to retrieve some information about your Chainguard resources. The provider itself doesn't require it.

## Configure the Chainguard Terraform provider

Terraform uses [a native configuration language](https://developer.hashicorp.com/terraform/language) to define resources. You store each configuration in one or more `.tf` files in a directory called the *root module*. With the Terraform CLI, the root module is the working directory where you run `terraform` commands to create or destroy your resources.

To use the Chainguard Terraform provider, add it to the block of required providers in your configuration:

```hcl
terraform {
  required_providers {
    chainguard = { source = "chainguard-dev/chainguard" }
  }
}
```

If you don't have an active Chainguard token when you apply the configuration, the provider launches a browser to complete the OAuth 2.0 flow with one of the default identity providers: GitHub, GitLab, or Google. The provider doesn't need `chainctl` to authenticate.

You can customize the behavior of the authentication flow in several ways. For example, you can specify a [verified organization](/platform/administration/iam-organizations/verified-orgs/) name to use a previously configured custom identity provider:

```hcl
provider "chainguard" {
  login_options {
    organization_name = "my-org.com"
  }
}
```

You can also configure the provider to use an OIDC token, either by supplying it directly or pulling it from a file, with the automatic browser flow disabled. This is useful when setting up CI workflows:

```hcl
provider "chainguard" {
  login_options {
    # Disable the automatic browser authentication flow.
    disabled = true
    # identity_id is the exact ID of an assumable identity.
    # Get this ID with chainctl iam identities list
    identity_id    = "1f127a7c0609329f04b43d845cf80eea4247a07c/d6305475446bbef6"
    identity_token = "/path/to/oidc/token"
  }
}
```

You can find more information about authenticating with the Chainguard Terraform provider in the [provider documentation](https://registry.terraform.io/providers/chainguard-dev/chainguard/latest/docs) and [the included examples](https://github.com/chainguard-dev/terraform-provider-chainguard/tree/main/examples).

## Define organization references

Terraform manages resources declaratively: you define the state you want your resources in, and Terraform and the provider handle the details of reaching that state.

Resources on the Chainguard platform are organized in a hierarchical structure consisting of [organizations and folders](/platform/administration/iam-organizations/overview-of-chainguard-iam-model/#organizations-and-folders). An organization is a customer or group of customers working with the same Chainguard resources, while a folder is a collection of resources within a Chainguard organization. Most users only need to work at the organization level.

![Diagram outlining hierarchical structure of Chainguard resources. The diagram has two halves: one labeled "Organization" and another labeled "Chainguard". Under Organization is a box labeled "Tags" with an arrow pointing toward another box labeled "Repos." Under both halves is a box labeled "Role Bindings" which has four arrows pointing from it. Two arrows point to boxes (labeled "Identities" and "Custom Roles") under Organization and the other two point to boxes (labeled "User Identities" and "Roles") under Chainguard.](tf-diagram.png)

All user-managed resources are defined in relation to the organization to which they belong. This means developers need to be able to reference their organization throughout their configuration. This section describes two ways to define this kind of reference: using local values and data sources. For more on referencing an organization, refer to the [`chainguard_group` resource documentation](https://registry.terraform.io/providers/chainguard-dev/chainguard/latest/docs/resources/group).

> **Note:** Chainguard organizations were previously called "groups," with a "root group" representing what is now referred to as an organization and "subgroups" referring to folders. The Chainguard Terraform provider still refers to "groups" instead of organizations. To align with our other [IAM resources](/platform/administration/iam-organizations/), this document uses the new nomenclature wherever possible.

### Define local values

The Terraform configuration language allows you to define *local values* that assign a name to a given expression. This allows you to reference the name of a local value multiple times throughout a Terraform configuration rather than repeating the expression each time. This section shows how to define a local value that holds the ID of a Chainguard organization.

If you are familiar with `chainctl`, you can find your organization's ID with the following command:

```shell
chainctl iam organizations list -o table
```

Once you've copied the UIDP of your organization (the 40-character hex string listed in the `ID` column of the previous command's output), use it to create a local value in Terraform:

```hcl
locals {
  org_id = "[organization UIDP]"
}
```

Throughout your Terraform code, you can refer to this value as `local.org_id`. If you are setting up a reusable Terraform module, consider an input variable instead. For more information, refer to the [Terraform documentation](https://developer.hashicorp.com/terraform/language/values/variables).

### Use data sources

*Data sources* allow Terraform to access and use information defined outside of Terraform. The available data sources for Chainguard resources are [groups](https://registry.terraform.io/providers/chainguard-dev/chainguard/latest/docs/data-sources/group), [identities](https://registry.terraform.io/providers/chainguard-dev/chainguard/latest/docs/data-sources/identity), and [roles](https://registry.terraform.io/providers/chainguard-dev/chainguard/latest/docs/data-sources/role).

If you know the exact name of your organization, you can use a data source to query the API for it:

```hcl
data "chainguard_group" "org" {
  # This indicates the group is an organization.
  parent_id = "/"
  name      = "[organization name]"
}
```

To refer to the organization's ID in other parts of your Terraform configuration, use the reference `data.chainguard_group.org.id`. The remaining examples in this guide use this reference.

## Manage users

The Chainguard Terraform provider is useful for configuring your organization's users and roles. When authenticating with the Chainguard platform, you have the option of using the default OIDC providers (GitHub, GitLab, Google). You can also bring your own identity provider, as long as it is OIDC compliant.

To configure a new identity provider for your organization, use the `chainguard_identity_provider` resource. You must provide a `parent_id` (your organization's ID), a `name` (the identity provider service is a good choice), a `default_role` that new users are bound to when they first log in, and an `oidc` configuration:

```hcl
# The default role can be either a built-in role, or a custom role.
# To see the list of available built-in roles
# use chainctl iam roles list --managed
data "chainguard_role" "default_role" {
  name = "registry.pull_token_creator"
}

resource "chainguard_identity_provider" "idp" {
  parent_id   = data.chainguard_group.org.id
  name        = "[identity provider service]"
  description = "My org's identity provider"
  # Role data sources return a list of matched roles.
  # Don't use data.chainguard_role.default_role.id here, as that
  # is not the ID of the returned role.
  default_role = data.chainguard_role.default_role.items.0.id

  oidc {
    issuer        = "[URL of identity provider issuer]"
    client_id     = "[identity provider client ID]"
    client_secret = "[identity provider client secret]"

    # The openid scope is always requested. Add any other scopes
    # your identity provider supports, such as email or profile.
    additional_scopes = ["email"]
  }
}
```

As this example shows, you also have the option of including a `description` of the identity provider.

If you're not bringing your own identity provider, but rather relying on one of the default OIDC providers, you can still pre-bind users to roles within your organization so they can log in and access your organization's resources right away.

As an example, say you want your users to log in with their GitHub account. To pre-bind users to a role within your organization, you need their GitHub IDs. Add them to a Terraform configuration like the following:

```hcl
# Create a custom role in this example for first-time users.
resource "chainguard_role" "default_role" {
  parent_id   = data.chainguard_group.org.id
  name        = "org-default-role"
  description = "The role new users are bound to on first login."

  # A full list of all capabilities you can assign to a role
  # is available with chainctl iam roles capabilities list
  capabilities = [
    "groups.list",
    "repo.list",
    "tag.list",
    ...
  ]
}

# Gather a list of user identities
data "chainguard_identity" "users" {
  # Assumes a github_ids set variable that holds
  # your users' GitHub IDs
  for_each = var.github_ids

  # The issuer is always the same when using the default
  # OIDC providers.
  issuer = "https://auth.chainguard.dev/"

  # Subjects are prepended with the name of the OIDC provider
  # when using the default provider: github, gitlab, or google-oauth2
  subject = "github|${each.key}"
}

# Bind your users to a default role
resource "chainguard_rolebinding" "default_bindings" {
  for_each = var.github_ids

  group    = data.chainguard_group.org.id
  identity = data.chainguard_identity.users[each.key].id
  role     = chainguard_role.default_role.id
}
```

After applying this Terraform configuration, any user whose GitHub ID you included can log in and is already bound to the default role.

## Learn more

The [Chainguard Terraform provider documentation](https://registry.terraform.io/providers/chainguard-dev/chainguard/latest/docs) includes examples of how you can use it to manage your Chainguard resources.

For more information on setting up custom identity providers, refer to [Custom IdPs](/platform/administration/custom-idps/custom-idps/), as well as our examples for [Okta](/platform/administration/custom-idps/idp-providers/okta/), [Ping Identity](/platform/administration/custom-idps/idp-providers/ping-id/), and [Microsoft Entra ID](/platform/administration/custom-idps/idp-providers/ms-entra-id/). For a fuller example of this guide's approach, refer to the tutorial on [using the Terraform provider to grant a GitHub team access to a Chainguard organization](/platform/administration/iam-organizations/roles-role-bindings/rolebinding-terraform-gh/).
