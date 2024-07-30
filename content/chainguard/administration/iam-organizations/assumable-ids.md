---
title : "Overview of Assumable Identities in Chainguard"
linktitle: "Assumable Identities"
aliases: 
- /chainguard/chainguard-enforce/authentication/assumable-ids/
- /chainguard/chainguard-enforce/iam-groups/assumable-ids/
- /chainguard/administration/iam-organizations/assumable-ids/
lead: ""
description: "An overview of what assumable identities are and how they can be used with Chainguard assets."
type: "article"
date: 2023-05-04T08:48:45+00:00
lastmod: 2024-05-09T08:48:45+00:00
draft: false
tags: ["Chainguard Images", "Product", "Conceptual"]
images: []
weight: 015
---

Both [`chainctl`](/chainguard/chainctl/) and the [Chainguard Console](https://console.enforce.dev/) are useful tools for interacting with Chainguard. However, there may be times that you want to hand off certain administrative tasks to an automation system, like Buildkite or GitHub Actions. 

In such cases, you can create a Chainguard identity for these systems to assume, allowing them to perform certain tasks within a specific scope. You can restrict access to an identity so that only workflows that present tokens matching a specific issuer and subject can assume it. Likewise, assumable identities can be tied to certain roles — like `viewer`, `owner`, or `editor` — letting you place strict limits on what a given identity is allowed to do. 

This guide provides a general overview of assumable identities in Chainguard, outlining how they work and how to create them.
 

## About Assumable Identities

Chainguard's *assumable identities* are identities that can be assumed by workflows in order to complete tasks without manual authorization. In many ways, these are similar to AWS roles or Google Service accounts, as Chainguard identities allow you to delegate access to your Chainguard resources to external applications or services.

Chainguard originally only supported what are referred to as *literal identities*. These are identities that consist of a unique mapping of verified issuer and subject to refer to an individual user. Literal identities can work well for self-service enrollment in some cases. However, they start to run into problems in several scenarios, such as with systems that use variable `subject` claims (like Buildkite, which injects commit SHAs) or automation systems (like continuous integration systems), which can be difficult to register to literal identities on their first use. 

Assumable identities essentially reverse the lookup process of literal identities. Instead of Chainguard analyzing at a token's issuer and subject to determine their literal identity, the client presents an assumable identity's UIDP (unique identifier path). Chainguard then checks this UIDP against the client's token. If the token's issuer and subject match those required by the identity, then the client may assume the identity.

This enables you to create identities that can only be assumed by specific automated workflows, providing greater security for your build and deployment processes. We have a number of examples of how to create assumable identities for specific providers.

* [GitHub](/chainguard/administration/iam-organizations/identity-examples/github-identity/)
* [GitLab](/chainguard/administration/iam-organizations/identity-examples/gitlab-identity/)
* [AWS Lambda](/chainguard/administration/iam-organizations/identity-examples/aws-identity/)
* [Jenkins](/chainguard/administration/iam-organizations/identity-examples/jenkins-identity/)
* [Buildkite](/chainguard/administration/iam-organizations/identity-examples/buildkite-identity/)
* [Bitbucket](/chainguard/administration/iam-organizations/identity-examples/bitbucket-identity/)

A notable difference between registered users and identities in Chainguard's IAM model is that identities are tied to a specific [IAM organization](/chainguard/chainguard-enforce/iam-groups/overview-of-enforce-iam-model/). When you create an identity, you must specify a Chainguard organization under which the identity will be created.

However, an identity won't automatically have access to the other resources associated with that organization. In order for an identity to be able to interact with a organization's resources — including the Images, repositories, and users associated with the organization — it must be granted the permissions it needs to do so. To do this, you must also tie the identity to a role. Chainguard comes with a few built-in roles, including `viewer`, `editor`, and `owner`. You can also create custom role-bindings with `chainctl`. Check out the [`chainctl iam role-bindings` documentation](/chainguard/chainctl/chainctl-docs/chainctl_iam_role-bindings/) for more details. 

Now that you have a better understanding of what assumable identities are, let's go over how you can set up an assumable identity. There are currently two main ways you can create an identity: with Terraform and with `chainctl`. Let's first go over how to set up an identity with Terraform.


## Terraform

To set up an assumable identity with Terraform, you will need to add a few specific blocks to your Terraform configuration. The following example `resource` block is the most important of these, as it is what creates the assumable identity.

```
resource "chainguard_identity" "<id-ref>" {
  parent_id   = <chainguard organization ID>
  name   	 = "<identity name>"
  description = <<EOF
    This is an example description for an identity.
  EOF

  claim_match {
    issuer  = "https://some.issuer.uri.com"
    subject = "example-subject"
  }
}
```

Here, `parent_id` defines the Chainguard organization that the identity will be tied to. This could be a literal value — like a Chainguard organization identification number — or a [local value](https://developer.hashicorp.com/terraform/language/values/locals) that references an existing organization. You can enter whatever you'd like for the `name`, though it helps to provide a descriptive name for your identities. The `description` field is optional, but it can be helpful to include to clarify the identity's purpose.

The `claim_match` block within this section is what specifies the users and workloads allowed to assume the identity. You must specify an issuer and subject in the claim match block, but you can optionally specify an `audience` here as well.

This example provides literal values for both the `issuer` and `subject` fields. This means that any workload or individual attempting to use this identity must have a signature whose issuer and subject match those within the `claim_match` block exactly. You can instead use the `issuer_pattern`, `subject_pattern`, or `audience_pattern` fields to pass regular expression patterns which clients must match in order to assume the identity. 

```
  claim_match {
	issuer_pattern = ".*"
	subject_pattern = ".*"
	audience_pattern = ".*"
  }
```

This gives you some more flexibility with defining who has access to the identity. Note that this example `claim_match` block would match any signature, meaning it would be so permissive as to be insecure.

Another block to include in your Terraform configuration is an `output` block that outputs the UIDP of the identity you're trying to assume. This is a unique value that you can use to let Chainguard know that you want to assume the role.

```
output "<id-ref>-identity" {
  value = chainguard_identity.<id-ref>.id
}
```

The last two blocks you should include in a Terraform configuration are what apply a role-binding to the new identity. First, you need to include a `data` section to look up the role. In this example it looks up Chainguard's built-in `viewer` role.

```
data "chainguard_roles" "viewer" {
  name = "viewer"
}
```

Then you need to include another `resource` block to create the role-binding using the determined role. The identity will have the permissions of that role over the organization specified within this block.

```
resource "chainguard_role-binding" "view-stuff" {
  identity = chainguard_identity.<id-ref>.id
  group    = chainguard_group.user-group.id
  role     = data.chainguard_roles.viewer.items[0].id
}
```

This means that the identity this Terraform configuration will create will only be able to view the resources tied to the same organization the identity is tied to.

Applying this configuration will create the assumable identity. You can follow any of our [identity examples](/chainguard/administration/iam-organizations/identity-examples/) to create an assumable identity that can be used by a continuous integration workflow to interact with Chainguard. The Terraform files used in the linked tutorials are based closely on the template outlined here.


## Managing identities with `chainctl`

You can also set up an assumed identity using the `chainctl` command-line tool. Specifically, you can run the `chainctl iam identities create` subcommand, which uses the following syntax:

```sh
chainctl iam identities create <identity-name> \
    --identity-issuer=<issuer of the identity> \
    --issuer-keys=<keys for the issuer> \
    --subject=<subject of the identity> \
    --group=<organization name> \
    --role=<role>
```

As with Terraform, you must provide `chainctl` with certain information about the identity you want to create, including the issuer and subject of the identity, the role-bindings associated with the identity (if any), and the organization under which the identity should be created.

You can change an existing identity with the `update` command. The following example would update the identity's issuer.

```sh
chainctl iam identities update <identity-name> --identity-issuer=https://new-issuer.mycompany.com
```

To delete an identity, use the `delete` subcommand.

```sh
chainctl iam identities delete <identity-name>
```

For more detailed information on managing identities with `chainctl`, we encourage you to check out the [`chainctl` reference documentation](/chainguard/chainctl/chainctl-docs/chainctl_iam_identities/).


## Assuming an identity

Whether you create an identity with `chainctl` or with Terraform, Chainguard will generate a UIDP (unique identifier path) tied to the identity. You can retrieve a list of all the identities you've created — along with their UIDPs — with the following command.

```sh
chainctl iam identities ls -o table
```
```
                             ID                             |      NAME      |    TYPE     | DESCRIPTION |         ROLES         |                   ISSUER                    | EXPIRES  
------------------------------------------------------------+----------------+-------------+-------------+-----------------------+---------------------------------------------+----------
  c95870ebffa72a258df087ea727ee92daf177e29/f067a9080d45a098 | sampleidentity | claim_match |             | example-group: viewer | https://token.actions.githubusercontent.com | n/a      
```

If a workflow is authorized to assume the identity — meaning that its token matches the `issuer` and `subject` specified for the identity — then it only needs to present this identification number in order to assume it.


## Learn More

As mentioned previously, we've published a few tutorials that outline how you can [set up an identity for a CI/CD workflow to assume](/chainguard/chainguard-enforce/iam-groups/identity-examples/). We strongly encourage you to follow these guides to better understand how assumable identities work in Chainguard.
