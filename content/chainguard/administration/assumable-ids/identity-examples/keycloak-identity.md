---
title : "Create an Assumable Identity for a CLI session authenticated with Keycloak"
linktitle: "Keycloak"
aliases:
- /chainguard/administration/iam-groups/identity-examples/keycloak-identity/
- /chainguard/administration/iam-organizations/identity-examples/keycloak-identity/
- /chainguard/administration/assumable-ids/identity-examples/keycloak-identity/
lead: ""
description: "Procedural tutorial outlining how to create a Chainguard identity that can be assumed by a Keycloak user."
type: "article"
date: 2024-03-26T08:48:45+00:00
lastmod: 2024-05-09T08:48:45+00:00
draft: false
tags: ["Chainguard Containers", "Product", "Procedural"]
images: []
weight: 040
---

Chainguard's [*assumable identities*](/chainguard/administration/iam-organizations/assumable-ids/) are identities that can be assumed by external applications or workflows in order to perform certain tasks that would otherwise have to be done by a human.

This procedural tutorial outlines how to create an identity using Terraform, and then assume the identity with the CLI to interact with Chainguard resources.


## Prerequisites

To complete this guide, you will need the following.

* `terraform` installed on your local machine. Terraform is an open-source Infrastructure as Code tool which this guide will use to create various cloud resources. Follow [the official Terraform documentation](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli) for instructions on installing the tool.
* `chainctl` — the Chainguard command line interface tool — installed on your local machine. Follow our guide on [How to Install `chainctl`](/chainguard/chainctl-usage/how-to-install-chainctl/) to set this up.
* A Keycloak deployment. [Keycloak](https://www.keycloak.org/) is an Open Source identity provider which Chainguard provides as an [image](https://images.chainguard.dev/directory/image/keycloak/versions?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement&utm_content=edu-content-chainguard-administration-iam-organizations-identity-examples-keycloak-identity)


## Creating Terraform Files

We will be using Terraform to create an identity for a Keycloak user to assume. This step outlines how to create three Terraform configuration files that, together, will produce such an identity.

To help explain each configuration file's purpose, we will go over what they do and how to create each file one by one. First, though, create a directory to hold the Terraform configuration and navigate into it.

```sh
mkdir ~/keycloak-id && cd $_
```

This will help make it easier to clean up your system at the end of this guide.


### `main.tf`

The first file, which we will call `main.tf`, will serve as the scaffolding for our Terraform infrastructure.

The file will consist of the following content.

```hcl
terraform {
  required_providers {
    chainguard = {
      source = "chainguard-dev/chainguard"
    }
  }
}
```

This is a fairly barebones Terraform configuration file, but we will define the rest of the resources in the other two files. In `main.tf`, we declare and initialize the Chainguard Terraform provider.

Next, you can create the `sample.tf` file.

### `sample.tf`

`sample.tf` will create a couple of structures that will help us test out the identity in a workflow.

This Terraform configuration consists of two main parts. The first part of the file will contain the following lines.

```hcl
data "chainguard_group" "group" {
  name   	 = "my-customer.biz"
}
```

This section looks up a Chainguard IAM organization named `my-customer.biz`. This organization will contain the identity — which will be created by the `keycloak.tf` file — to access when we test it out later on.

If you aren't sure of the name of your organization, you can retrieve a list of available organizations with the following command.

```sh
chainctl iam organizations list -o table
```

Now you can move on to creating the last of our Terraform configuration files, `keycloak.tf`.

### `keycloak.tf`

The `keycloak.tf` file is what will actually create the identity for your CLI to assume. The file will consist of four sections, which we'll go over one by one.

The first section creates the identity itself.

```
resource "chainguard_identity" "keycloak" {
  parent_id   = data.chainguard_group.group.id
  name    	= "keycloak"
  description = <<EOF
	This is an identity that authorizes Keycloak in this
	repository to assume to interact with chainctl.
  EOF

  claim_match {
    issuer   = "https://<keycloak issuer>"
    subject  = "<keycloak user ID>"
    audience = "<keycloak audience>"
  }
}
```

First this section creates a Chainguard Identity tied to the `chainguard_group` looked up in the `sample.tf` file. The identity is named `keycloak` and has a brief description.

The most important part of this section is the `claim_match`. When the the user tries to assume this identity later on, it must present a token matching the `issuer`, `subject`, and `audience` specified here in order to do so. The `issuer` is the entity that creates the token, the `subject` is the entity that the token represents (here, the Keycloak user), and the `audience` is the intended recipient of the token.

In this case, the `issuer` field points to the realm you are using on your Keycloak server, the issuer of JWT tokens. The `audience` field will likely be `account` depending on your Keycloak setup.

To discover the issuer, audience, and subject you will need to authenticate with the Keycloak server from the CLI and decode the JWT token returned. There are many ways to authenticate, but here is one example with password authentication:

```sh
curl --data "grant_type=password&client_id=<client name>&client_secret=<client secret>&username=<user>&password=<password>" https://<DNS NAME>/realms/<realm>/protocol/openid-connect/token | jq -r .access_token | cut -d\. -f2 | sed 's/$/==/' | base64 -d | jq | jq .iss,.aud,.sub
```

The next section of the `keycloak.tf` file will output the new identity's `id` value. This is a unique value that represents the identity itself.

```
output "keycloak-identity" {
  value = chainguard_identity.keycloak.id
}
```

The section after that looks up the `viewer` role.

```
data "chainguard_role" "viewer" {
  name = "viewer"
}
```

The final section grants this role to the identity.

```
resource "chainguard_rolebinding" "view-stuff" {
  identity = chainguard_identity.keycloak.id
  group	= data.chainguard_group.group.id
  role 	= data.chainguard_role.viewer.items[0].id
}
```

Following that, your Terraform configuration will be ready. Now you can run a few `terraform` commands to create the resources defined in your `.tf` files.

## Creating Your Resources

First, run `terraform init` to initialize Terraform's working directory.

```sh
terraform init
```

Then run `terraform plan`. This will produce a speculative execution plan that outlines what steps Terraform will take to create the resources defined in the files you set up in the last section.

```sh
terraform plan
```

Then apply the configuration.

```sh
terraform apply
```

Before going through with applying the Terraform configuration, this command will prompt you to confirm that you want it to do so. Enter `yes` to apply the configuration.

```
...

Plan: 4 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + keycloak-identity = (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value:
```

After typing `yes` and pressing `ENTER`, the command will complete and will output a `keycloak-ci` value.

```
...

Apply complete! Resources: 4 added, 0 changed, 0 destroyed.

Outputs:

keycloak-identity = "<your actions identity>"
```

This is the identity's [UIDP (unique identity path)](/chainguard/administration/cloudevents/events-reference/#uidp-identifiers), which you configured the `keycloak.tf` file to emit in the previous section. Note this value down, as you'll need it to authenticate with `chainctl`. If you need to retrieve this UIDP later on, though, you can always run the following `chainctl` command to obtain a list of the UIDPs of all your existing identities.

```sh
chainctl iam identities ls
```

Note that you may receive a `PermissionDenied` error part way through the apply step. If so, run `chainctl auth login` once more, and then `terraform apply` again to resume creating the identity and resources.

## Testing the identity

From a CLI with the `chainctl` binary installed and access to the Keycloak server:

First, create a pair of environment variables for when you log into Chainguard using the identity. This command generates a JSON Web Token (JWT) by logging in to Keycloak with a username and password and then assigning the token to a variable named `ID_TOKEN`.

```sh
export ID_TOKEN=$(curl \
  --data "grant_type=password&client_id=<client>&client_secret=<client secret>&username=<user>&password=<password>" \
  https://<keycloak URL>/realms/<realm>/protocol/openid-connect/token | jq -r .access_token)
```

Next set a variable named `ID` to your identity's UIDP value with the following command. Be sure to replace `<identity UIDP>` with the identity's UIDP value, which you noted down in the previous section.

```sh 
export ID=<identity UIDP>
```

After creating these variables, run the following commands to log in to Chainguard under the assumed identity. 

```
chainctl auth login \
  --identity-token $ID_TOKEN \
  --identity $ID

chainctl auth configure-docker \
  --identity-token $ID_TOKEN \
  --identity $ID
```

After logging in, the pipeline will be able to run any `chainctl` command under the assumed identity. To test out this ability, this configuration runs the `chainctl images repos list` command to list all available image repositories associated associated with the organization.

```sh
chainctl images repos list

```

After updating the Keycloak configuration, commit the changes and the pipeline will run automatically. A status box in the dashboard will let you know whether the pipeline runs successfully.

If the token times out, `chainctl` will try to reauthenticate and fail. If you repeat the same login command with the old token you will see messages like this:

```sh
chainctl auth login --identity-token $ID_TOKEN --identity $ID
Error: [101] unable to exchange tokens: rpc error: code = PermissionDenied desc = verifying token: oidc: token is expired (Token Expiry: 2024-03-18 11:44:35 +0000 UTC)
```

To authenticate with `chainctl` you will need to generate a new token with Keycloak.

If you'd like to experiment further with this identity and what the workflow can do with it, there are a few parts of this setup that you can tweak. For instance, if you'd like to give this identity different permissions you can change the role data source to the role you would like to grant.

```
data "chainguard_roles" "editor" {
  name = "editor"
}
```

To retrieve a list of all the available roles, you can run the following command.

```sh
chainctl iam roles list
```

This command's output will also include any custom roles you are able to grant.


## Removing Sample Resources

To remove the resources Terraform created, you can run the `terraform destroy` command.

```sh
terraform destroy
```

This will destroy identity and the role-binding created in this guide. It will not delete the organization.

You can then remove the working directory to clean up your system.

```sh
rm -r ~/keycloak-id/
```

Following that, all of the example resources created in this guide will be removed from your system.


## Learn more

For more information about how assumable identities work in Chainguard, check out our [conceptual overview of assumable identities](/chainguard/administration/iam-organizations/assumable-ids/). Additionally, the Terraform documentation includes a section on [recommended best practices](https://developer.hashicorp.com/terraform/cloud-docs/recommended-practices) which you can refer to if you'd like to build on this Terraform configuration for a production environment. For more information about OIDC you can find a lot of documentation on the [OpenID Foundation website](https://openid.net/). For Keycloak specific information, we encourage you to check out the [official Keycloak documentation](https://www.keycloak.org/documentation)
