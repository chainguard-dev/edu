---
title: "Introduction to the Chainguard Terraform Provider"
linktitle: "Terraform Provider"
type: "article"
description: "An introduction to working with the Chainguard Terraform provider"
date: 2024-01-28T15:56:52-07:00
lastmod: 2024-05-09T15:22:20+01:00
draft: false
tags: ["Product", "Overview"]
images: []
menu:
  docs:
    parent: "administration"
toc: true
weight: 008
---

[Terraform](https://www.terraform.io/) is an infrastructure as code tool that allows users to declaratively configure resources in cloud providers like AWS and GCP, SaaS platforms, and many other API-driven environments. [Terraform providers](https://developer.hashicorp.com/terraform/language/providers) are written by third-party developers to allow Terraform to manage resources in their environment.

[The Chainguard Terraform provider](https://registry.terraform.io/providers/chainguard-dev/chainguard/latest) enables users to manage resources on the Chainguard Platform, such as identities, role-bindings, custom roles, and more. This guide provides a brief introduction to the Chainguard Terraform provider, including how to configure it and use it to manage your Chainguard resources.


## Prerequisites

In order to use the Chainguard Terraform provider, you will need to [install Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli) on your local machine.

Also, while it isn't necessary for using the Chainguard Terraform provider, this guide assumes you have [`chainctl` installed](https://edu.chainguard.dev/chainguard/administration/how-to-install-chainctl/) in order to retrieve some information about your Chainguard resources.


## Configuring the Chainguard Terraform provider

Terraform uses [a native configuration language](https://developer.hashicorp.com/terraform/language) to define resources. Each configuration is stored in one or more `.tf` files, which in turn are stored in what is called a *root module*. When using the Terraform CLI, the root module is the working directory where you invoke `terraform` commands to create or destroy your resources.

To use the Chainguard Terraform provider, add it to the block of required providers in your configuration:

```
terraform {
  required_providers {
	chainguard = { source = "chainguard-dev/chainguard" }
  }
}
```

If you don't have an active Chainguard token when you apply the configuration, the provider will automatically launch a browser to complete the Oauth 2 flow with one of the default identity providers: GitHub, GitLab, or Google. This means the Terraform provider does not require `chainctl` to be installed to manage authentication with Chainguard.

You can customize the behavior of the authentication flow in a number of ways. For example, you can specify an identity to assume, or a [verified organization](/chainguard/administration/iam-groups/verified-orgs/) name in order to use a previously-configured custom identity provider:

```
provider "chainguard" {
  login_options {
	organization_name = "my-org.com"
	# identity_id is the exact ID of an assumable identity.
	# Get this ID with chainctl iam identities list
	identity_id = "1f127a7c0609329f04b43d845cf80eea4247a07c/d6305475446bbef6"
  }
}
```

You can also configure the provider to use an OIDC token, either by supplying it directly or pulling it from a file, with the automatic browser flow disabled. This is useful when setting up CI workflows:

```
provider "chainguard" {
  login_options {
	# Disable the automatic browser authentication flow.
	disabled   	= true
	identity_token = "/path/to/oidc/token"
  }
}
```

You can find more information about authenticating with the Chainguard Terraform provider in the [provider documentation](https://registry.terraform.io/providers/chainguard-dev/chainguard/latest/docs) and [the included examples](https://github.com/chainguard-dev/terraform-provider-chainguard/tree/main/examples).

## Defining Organization References

Terraform was designed to allow users to manage various resources declaratively. In practice, this means that you define the state you want your resources to be in and then you let Terraform and the provider handle the details of bringing that state to reality. 

Resources on the Chainguard platform are organized in a hierarchical structure consisting of [**Organizations** and **Folders**](/chainguard/administration/iam-organizations/overview-of-chainguard-iam-model/#organizations-and-folders). An organization is a customer or group of customers working with the same Chainguard resources, while a folder is a collection of resources within a Chainguard organization. Most users will only need to work at the organization level.

![Diagram outlining hierarchical structure of Chainguard resources. The diagram has two halves: one labeled "Organization" and another labeled "Chainguard". Under Organization is a box labeled "Tags" with an arrow pointing toward another box labeled "Repos." Under both halves is a box labeled "Role Bindings" which has four arrows pointing from it. Two arrows point to boxes (labeled "Identities" and "Custom Roles") under Organization and the other two point to boxes (labeled "User Identities" and "roles) under Chainguard.](tf-diagram.png)

All user-managed resources are defined in relation to the organization to which they belong. This means developers need to be able to reference their organization throughout their configuration. We'll outline two ways to define this kind of reference: using local values and data sources. For more details on referencing an organization, please refer to the [`chainguard_group` resource documentation](https://registry.terraform.io/providers/chainguard-dev/chainguard/latest/docs/resources/group) for more information.

> **Note:** Chainguard organizations were previously called "groups," with a "root group" representing what is now referred to as an organization and "subgroups" referring to folders. As of this writing, the Chainguard Terraform provider still refers to "groups" instead of organizations. To align with our other [IAM resources](/chainguard/administration/iam-organizations/), this document uses the new nomenclature wherever possible.

### Defining local values

The Terraform configuration language allows you to define *local values* which assign a name to a given expression. This allows you to reference the name of a local value multiple times throughout a Terraform configuration rather than repeating the expression each time. As an example, this section will outline how to define a local variable representing the ID of a Chainguard organization.

If you are familiar with `chainctl`, you can find your organization's ID with the following command:

```shell
chainctl iam organizations list -o table
```

Once you've copied the UIDP of your organization (the 40-digit long hex string listed in the `ID` column of the previous command's output), you can use it to create a local variable in Terraform:

```
locals {
  org_id = "[organization UIDP]"
}
```

Throughout your Terraform code, you can refer to this value as `local.org_id`. If you are setting up a reusable Terraform module, you may consider using an input variable instead. Please refer to the [Terraform documentation](https://developer.hashicorp.com/terraform/language/values/variables) for more  information.

### Using data sources

*Data sources* allow Terraform to access and use information that was defined outside ofWe'll outline two ways to define this kind of reference: using local values and data sources. The available data sources for Chainguard resources are [groups](https://registry.terraform.io/providers/chainguard-dev/chainguard/latest/docs/data-sources/group), [identities](https://registry.terraform.io/providers/chainguard-dev/chainguard/latest/docs/data-sources/identity), and [roles](https://registry.terraform.io/providers/chainguard-dev/chainguard/latest/docs/data-sources/role).

If you know the exact name of your organization, you can use a data resource to query the API for it:

```
data "chainguard_group" "org" {
  # This indicates the group is an organization.
  parent_id = "/"
  name  	= "[organization name]"
}
```

To refer to the organization's ID in other parts of your Terraform configuration, you would use the reference `data.chainguard_group.org.id`. The rest of the examples in this document will use this for referring to the organization's ID.


## Managing users

The Chainguard Terraform provider is useful for configuring your organization's users and roles. When authenticating with the Chainguard platform, you have the option of using the default OIDC providers (GitHub, GitLab, Google). You can also bring your own identity provider, as long as it is OIDC compliant.

To configure a new identity provider for your organization, use the `chainguard_identity_provider` resource. You must provide a `parent_id` (your organization's ID), a `name` (the identity provider service is a good choice), a `default_role` that new users will be bound to upon their first login, and an `oidc` configuration:

```
# The default role can be either a built-in role, or a custom role.
# To see the list of available built-in roles
# use chainctl iam roles list --managed
data "chainguard_role" "default_role" {
  name = "registry.pull_token_creator"
}

resource "chainguard_identity_provider" "idp" {
  parent_id   = data.chainguard_group.org.id
  name    	= "[identity provider service]"
  description = "My org's identity provider"
  # Role data sources return list of matched roles.
  # Don't use data.chainguard_role.default_role.id here, as that
  # is not the ID of the returned role.
  default_role = data.chainguard_role.default_role.items.0.id

  oidc {
	issuer    	= "[URL of identity provider issuer]"
	client_id 	= "[identity provider client ID]"
	client_secret = "[identity provider client secret]"

	# openid scope is always requested, add additional scopes
	# your identity provider provides (e.g. email, profile)
	additional_scopes = ["email"]
  }
}
```

As this example shows, you also have the option of including a `description` of the identity provider. 

If you're not bringing your own identity provider, but rather relying on one of the default OIDC providers, you can still pre-bind users to roles within your organization so they can log in and access your organization's resources right away. 

As an example, say you want your users to log in with their GitHub account. To pre-bind users to a role within your organization, you will need to know their GitHub IDs and add them to a Terraform configuration like the following:

```
# Create a custom role in this example for first time users.
resource "chainguard_role" "default_role" {
  parent_id   = data.chainguard_group.org.id
  name    	= "org-default-role"
  description = "The role new users are bound to on first login."

  # A full list of all capabilities you can assign to a role
  # are available with chainctl iam roles capabilities list
  capabilities = [
	"groups.list",
	"repo.list",
	"tag.list",
	...
  ]
}

# Gather a list of user identities
data "chainguard_identity" "users" {
  # Assumes there exists a github_ids set variable defined
  # with the GitHub IDs of your users
  for_each = var.github_ids


  # The issuer is always the same when using the default
  # OIDC providers.
  issuer  = "https://auth.chainguard.dev/"
 
  # Subjects are prepended with the name of the OIDC provider
  # when using the default provider: github, gitlab, or google-oauth2
  subject = "github|${each.key}”
}

# Bind your users to a default role
resource "chainguard_rolebinding" "default_bindings" {
  for_each = var.github_ids

  group 	= data.chainguard_group.org.id
  identity  = data.chainguard_identity.users[each.key].id
  role  	= chainguard_role.default_role.id
}
```

After applying this Terraform configuration, any user whose GitHub ID was included can log in and will already be bound to the default role.


## Learn more

The [Chainguard Terraform provider documentation](https://registry.terraform.io/providers/chainguard-dev/chainguard/latest/docs) includes examples of how you can use it to manage your Chainguard resources.

For more information on setting up custom identity providers, we encourage you to check out our documentation on setting up [custom IDPs](/chainguard/administration/custom-idps/custom-idps/), as well as our examples for [Okta](/chainguard/administration/custom-idps/okta/), [Ping Identity](/chainguard/administration/custom-idps/ping-id/), and [Azure Active Directory](/chainguard/administration/custom-idps/azure-ad/). Additionally, [our tutorial](/chainguard/administration/iam-groups/rolebinding-terraform-gh/) on using the Terraform provider to grant members of a GitHub team access to the resources managed by a Chainguard organization provides more context and information to the method outlined in this guide.

