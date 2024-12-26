---
title : "Create an Assumable Identity for a Bitbucket Pipeline"
linktitle: "Bitbucket Assumable Identity"
aliases:
- chainguard/chainguard-enforce/authentication/identity-examples/enforce-bitbucket-identity/
lead: ""
description: "Procedural tutorial outlining how to create a Chainguard identity that can be assumed by a Bitbucket workflow."
type: "article"
date: 2023-05-17T08:48:45+00:00
lastmod: 2024-12-26T08:48:45+00:00
draft: false
tags: ["Chainguard Images", "Product", "Procedural"]
images: []
weight: 020
---

Chainguard's [*assumable identities*](/chainguard/administration/iam-organizations/assumable-ids/) are identities that can be assumed by external applications or workflows in order to perform certain tasks that would otherwise have to be done by a human.

This procedural tutorial outlines how to create an identity using Terraform, and then how to update a Bitbucket pipeline so that it can assume the identity and interact with Chainguard resources.


## Prerequisites

To complete this guide, you will need the following.

* `terraform` installed on your local machine. Terraform is an open-source Infrastructure as Code tool which this guide will use to create various cloud resources. Follow [the official Terraform documentation](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli) for instructions on installing the tool.
* `chainctl` — the Chainguard command line interface tool — installed on your local machine. Follow our guide on [How to Install `chainctl`](/chainguard/administration/how-to-install-chainctl/) to set this up.
* A Bitbucket pipeline you can use to test out the identity you'll create. We recommend following Bitbucket's [Getting Started guide](https://support.atlassian.com/bitbucket-cloud/docs/get-started-with-bitbucket-pipelines/) to set this up. If you need to enable pipelines for your repository, visit Bitbucket's [Configure your first pipeline](https://support.atlassian.com/bitbucket-cloud/docs/configure-your-first-pipeline/) page to get started.

## Creating Terraform Files

We will be using Terraform to create an identity for a Bitbucket pipeline to assume. This step outlines how to create three Terraform configuration files that, together, will produce such an identity.

To help explain each configuration file's purpose, we will go over what they do and how to create each file one by one. First, though, create a directory to hold the Terraform configuration and navigate into it.

```sh
mkdir ~/bitbucket-id && cd $_
```

This will help make it easier to clean up your system at the end of this guide.


### `main.tf`

The first file, which we will call `main.tf`, will serve as the scaffolding for our Terraform infrastructure.

The file will consist of the following content.

```
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

`sample.tf` will create a couple of structures that will help us test out the identity with a Bitbucket a workflow.

This Terraform configuration consists of two main parts. The first part of the file will contain the following lines.

```
data "chainguard_group" "group" {
  name = "my-customer.biz"
}
```

This section looks up a Chainguard IAM organization named `my-customer.biz`. This will contain the identity — which will be created by the `bitbucket.tf` file — to access when we test it out later on.

Now you can move on to creating the rest of our Terraform configuration files, `bitbucket.tf`.

### `bitbucket.tf`

The `bitbucket.tf` file is what will actually create the identity for your Bitbucket workflow to assume. The file will consist of four sections, which we'll go over one by one.

The first section creates the identity itself.

```
resource "chainguard_identity" "bitbucket" {
  parent_id   = data.chainguard_group.group.id
  name        = "bitbucket"
  description = <<EOF
    This is an identity that authorizes Bitbucket workflows
    for this repository to assume to interact with chainctl.
  EOF

    claim_match {
    audience        = "ari:cloud:bitbucket::workspace/%workspace-uuid%"
    issuer          = "https://api.bitbucket.org/2.0/workspaces/%workspace-name%/pipelines-config/identity/oidc"
    subject_pattern = "{%repository-uuid%}:.+"
  }
}
```

First, this section creates a Chainguard Identity tied to the `chainguard_group` looked up in the `sample.tf` file. The identity is named `bitbucket` and has a brief description.

The most important part of this section is the `claim_match`. When the Bitbucket pipeline tries to assume this identity later on, it must present a token matching the `audience`, `issuer` and `subject` specified here in order to do so. The `audience` is the intended recipient of the issued token, while the `issuer` is the entity that creates the token.

Finally, the `subject_pattern` is the entity (here, the Bitbucket pipeline build) that the token represents. Note that the curly braces around the `%repository-uuid%` variable are part of the generated OIDC token from Bitbucket, so be sure to include both opening `{` and closing `}` characters around your repository UUID.

In this case, the `issuer` field points to `https://api.bitbucket.org/2.0/workspaces/%workspace-name%/pipelines-config/identity/oidc`, the issuer of JWT tokens for Bitbucket pipelines.

Instead of pointing to a literal value with a `subject` field, though, this file points to a regular expression using the `subject_pattern` field. When you run a Bitbucket pipeline, it generates a unique identifier for each pipeline `- step` and appends that to the `subject_pattern` field. Since the identifier is not known ahead of time, passing the regular expression `.+` allows you to specify a subject regex that will work for every build from this pipeline.

Refer to your Bitbucket repository OIDC settings page for reference values. To find the page, browse to your **Repository settings** page, and then find the **OpenID Connect** section in the left menu. For the purposes of this guide, you will need to replace `%workspace-name%`, `%workspace-uuid%`, and `%repository-uuid%` with the values from your Bitbucket OIDC settings page.

The next section will output the new identity's `id` value. This is a unique value that represents the identity itself.

```
output "bitbucket-identity" {
  value = chainguard_identity.bitbucket.id
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
  identity = chainguard_identity.bitbucket.id
  group    = data.chainguard_group.group.id
  role     = data.chainguard_role.viewer.items[0].id
}
```

Run the following command to create this file with each of these sections. Be sure to change the `subject_pattern` value to align with your own Bitbucket pipeline OIDC variables. For example, if your repository UUID were `C668DE74-6D94-4924-90B1-8B9AB7EE9089`, you would set the `subject_pattern` value to `"{C668DE74-6D94-4924-90B1-8B9AB7EE9089}:.+"`, ensuring that the curly braces are included.

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

If the plan worked successfully and you're satisfied that it will produce the resources you expect, you can apply it.

```sh
terraform apply
```

Before going through with applying the Terraform configuration, this command will prompt you to confirm that you want it to do so. Enter `yes` to apply the configuration.

```
. . .

Plan: 4 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + bitbucket-identity = (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value:
```

After pressing `ENTER`, the command will complete and will output an `bitbucket-identity` value. Note that you may receive a `PermissionDenied` error part way through the apply step. If so, run `chainctl auth login` once more, and then `terraform apply` again to resume creating the identity and resources.

```
. . .

Apply complete! Resources: 3 added, 0 changed, 0 destroyed.

Outputs:

bitbucket-identity = "%bitbucket-identity%"
```

This is the identity's [UIDP (unique identity path)](/chainguard/administration/cloudevents/events-reference/#uidp-identifiers), which you configured the `bitbucket.tf` file to emit in the previous section. Note this value down, as you'll need it when you test this identity using a Bitbucket workflow. If you need to retrieve this UIDP later on, though, you can always run the following `chainctl` command to obtain a list of the UIDPs of all your existing identities.

```sh
chainctl iam identities ls
```

You're now ready to edit a Bitbucket pipeline in order to test out this identity.


## Testing the identity with a Bitbucket pipeline

To test the identity you created with Terraform in the previous section, ensure you have Pipelines enabled for your repository and then create a `bitbucket-pipelines.yml` file in the root of your repository. Note that if you already have a pipeline with steps defined then you only need to add the `oidc: true` field to your pipeline to enable OIDC for the step in question.

Copy the following pipeline defintion into your `bitbucket-pipelines.yml` file and commit it to the repository.

```
image: atlassian/default-image:3

pipelines:
  default:
    - step:
        oidc: true
        max-time: 5
        script:
          - curl -o chainctl "https://dl.enforce.dev/chainctl/latest/chainctl_$(uname -s | tr '[:upper:]' '[:lower:]')_$(uname -m)"
          - chmod +x chainctl

          # Assume the bitbucket pipeline identity
          - ./chainctl auth login --identity-token $BITBUCKET_STEP_OIDC_TOKEN --identity %bitbucket-identity%
          - ./chainctl auth configure-docker --identity-token $BITBUCKET_STEP_OIDC_TOKEN --identity %bitbucket-identity%
```

The important line is the `oidc: true` option, which enables OIDC for the individual step in the pipeline. This configuration is why the `subject_pattern` with a regular expression is used in the Terraform configuration, since each step gets its own UUID identifier, which is added to the `sub` field in the generated OIDC token. Since the step UUID is known known before the build, the subject match needs to use a regular expression.

Now you can add the commands for testing the identity like `chainctl images repos list` in the following example:

```
...
          # Assume the bitbucket pipeline identity
          - ./chainctl auth login --identity-token $BITBUCKET_STEP_OIDC_TOKEN --identity %bitbucket-identity%
          - ./chainctl images repos list
          - docker pull cgr.dev/<organization>/<repo>:<tag>
```

Once you commit the `bitbucket-pipelines.yml` file the pipeline will run.

Assuming everything works as expected, your pipeline will be able to assume the identity and run the `chainctl images repos list` command, listing repos available to the organization.

```
. . .
chainctl        	100%[===================>]  54.34M  6.78MB/s	in 13s

2023-05-17 13:19:45 (4.28 MB/s) - ‘chainctl’ saved [56983552/56983552]

Successfully exchanged token.
Valid! Id: 3f4ad8a9d5e63be71d631a359ba0a91dcade94ab/d3ed9c70b538a796
```

If you'd like to experiment further with this identity and what the pipeline can do with it, there are a few parts of this setup that you can tweak. For instance, if you'd like to give this identity different permissions you can change the role data source to the role you would like to grant.

```
data "chainguard_roles" "editor" {
  name = "editor"
}
```

You can also edit the pipeline itself to change its behavior. For example, instead of listing the repos the identity has access to, you could have the workflow inspect the organizations.

```
          - ./chainctl images repos list
```

Of course, the Bitbucket pipeline will only be able to perform certain actions on certain resources, depending on what kind of access you grant it.


## Removing Sample Resources

To remove the resources Terraform created, you can run the `terraform destroy` command.

```sh
terraform destroy
```

This will destroy the role-binding, and the identity created in this guide. It will not delete the organization.

You can then remove the working directory to clean up your system.

```sh
rm -r ~/bitbucket-id/
```

Following that, all of the example resources created in this guide will be removed from your system.


## Learn more

For more information about how assumable identities work in Chainguard, check out our [conceptual overview of assumable identities](/chainguard/administration/iam-organizations/assumable-ids/). Additionally, the Terraform documentation includes a section on [recommended best practices](https://developer.hashicorp.com/terraform/cloud-docs/recommended-practices) which you can refer to if you'd like to build on this Terraform configuration for a production environment. Likewise, for more information on using Bitbucket pipelines, we encourage you to check out the [official project documentation](https://support.atlassian.com/bitbucket-cloud/docs/get-started-with-bitbucket-pipelines/), particularly their [documentation on OIDC](https://support.atlassian.com/bitbucket-cloud/docs/integrate-pipelines-with-resource-servers-using-oidc/).
