---
title : "Create an Assumable Identity for a Buildkite Pipeline"
linktitle: "Buildkite Assumable Identity"
aliases:
- /chainguard/chainguard-enforce/authentication/identity-examples/enforce-buildkite-identity/
lead: ""
description: "Procedural tutorial outlining how to create a Chainguard identity that can be assumed by a Buildkite workflow."
type: "article"
date: 2023-05-17T08:48:45+00:00
lastmod: 2024-05-09T08:48:45+00:00
draft: false
tags: ["Chainguard Images", "Product", "Procedural"]
images: []
weight: 015
---

Chainguard's [*assumable identities*](/chainguard/administration/iam-organizations/assumable-ids/) are identities that can be assumed by external applications or workflows in order to perform certain tasks that would otherwise have to be done by a human.

This procedural tutorial outlines how to create an identity using Terraform, and then how to update a Buildkite pipeline so that it can assume the identity and interact with Chainguard resources.


## Prerequisites

To complete this guide, you will need the following.

* `terraform` installed on your local machine. Terraform is an open-source Infrastructure as Code tool which this guide will use to create various cloud resources. Follow [the official Terraform documentation](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli) for instructions on installing the tool.
* `chainctl` — the Chainguard command line interface tool — installed on your local machine. Follow our guide on [How to Install `chainctl`](/chainguard/chainguard-enforce/how-to-install-chainctl/) to set this up.
* A Buildkite agent and pipeline you can use to test out the identity you'll create. We recommend following Buildkite's [Getting Started guide](https://buildkite.com/docs/tutorials/getting-started) to set these up.


## Creating Terraform Files

We will be using Terraform to create an identity for a Buildkite pipeline to assume. This step outlines how to create three Terraform configuration files that, together, will produce such an identity.

To help explain each configuration file's purpose, we will go over what they do and how to create each file one by one. First, though, create a directory to hold the Terraform configuration and navigate into it.

```sh
mkdir ~/buildkite-id && cd $_
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

```
data "chainguard_group" "group" {
  name = "my-customer.biz"
}
```

This section looks up a Chainguard IAM organization named `my-customer.biz`. This will contain the identity — which will be created by the `buildkite.tf` file — to access when we test it out later on.

Now you can move on to creating the last of our Terraform configuration files, `buildkite.tf`.

### `buildkite.tf`

The `buildkite.tf` file is what will actually create the identity for your Buildkite workflow to assume. The file will consist of four sections, which we'll go over one by one.

The first section creates the identity itself.

```
resource "chainguard_identity" "buildkite" {
  parent_id   = data.chainguard_group.group.id
  name   	 = "buildkite"
  description = <<EOF
    This is an identity that authorizes Buildkite workflows
    for this pipeline to assume to interact with chainctl.
  EOF

  claim_match {
    issuer 		 = "https://agent.buildkite.com"
    subject_pattern = "organization:<organization-name>:pipeline:<pipeline-name>:ref:refs/heads/main:commit:[0-9a-f]+:step:"
  }
}
```

First, this section creates a Chainguard Identity tied to the `chainguard_group` looked up in the `sample.tf` file. The identity is named `buildkite` and has a brief description.

The most important part of this section is the `claim_match`. When the Buildkite workflow tries to assume this identity later on, it must present a token matching the `issuer` and `subject` specified here in order to do so. The `issuer` is the entity that creates the token, while the `subject` is the entity (here, the Buildkite pipeline build) that the token represents.

In this case, the `issuer` field points to `https://agent.buildkite.com`, the issuer of JWT tokens for Buildkite pipelines.

Instead of pointing to a literal value with a `subject` field, though, this file points to a regular expression using the `subject_pattern` field. When you run a Buildkite pipeline, it generates a unique commit for each build. Passing the regular expression `[0-9a-f]+` allows you to generate an identity that will work for every build from this pipeline.

You may refer to [the official Buildkite documentation](https://buildkite.com/docs/agent/v3/cli-oidc#claims) for more details on how Buildkite `issuer` and `subject` claims can be formatted to suit your specific needs. For the purposes of this guide, though, you will need to replace `<organization-name>` and `<pipeline-name>` with the name of your Buildkite organization and the name of your Buildkite pipeline.

The next section will output the new identity's `id` value. This is a unique value that represents the identity itself.

```
output "buildkite-identity" {
  value = chainguard_identity.buildkite.id
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
  identity = chainguard_identity.buildkite.id
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

If the plan worked successfully and you're satisfied that it will produce the resources you expect, you can apply it. First, though, you'll need to log in to `chainctl` to ensure that Terraform can create the Chainguard resources.

```sh
chainctl auth login
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
  + buildkite-identity = (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value:
```

After pressing `ENTER`, the command will complete and will output an `buildkite-identity` value.

```
...

Apply complete! Resources: 3 added, 0 changed, 0 destroyed.

Outputs:

buildkite-identity = "<your buildkite identity>"
```

This is the identity's [UIDP (unique identity path)](/chainguard/administration/cloudevents/events-reference/#uidp-identifiers), which you configured the `buildkite.tf` file to emit in the previous section. Note this value down, as you'll need it when you test this identity using a Buildkite workflow. If you need to retrieve this UIDP later on, though, you can always run the following `chainctl` command to obtain a list of the UIDPs of all your existing identities.

```sh
chainctl iam identities ls
```

You're now ready to edit a Buildkite pipeline in order to test out this identity.


## Testing the identity with a Buildkite pipeline

To test the identity you created with Terraform in the previous section, navigate to your Buildkite pipeline. From the Buildkite Dashboard, click **Pipelines** in the top navigation bar and then click on the pipeline you specified in the `buildkite.tf` file.

From there, click the **Edit Steps** button to add the following commands to a step in your pipeline. Be sure to replace `<your buildkite identity>` with the identity UIDP you noted down in the previous section.

```
- command: |
	curl -o chainctl "https://dl.enforce.dev/chainctl/latest/chainctl_$(uname -s | tr '[:upper:]' '[:lower:]')_$(uname -m)"
	chmod +x chainctl
  token=$(buildkite-agent oidc request-token --audience issuer.enforce.dev)
	./chainctl auth login --identity-token $token --identity <your buildkite identity>
  ./chainctl auth configure-docker --identity-token $token --identity <your buildkite identity>
  ./chainctl images repos list
  docker pull cgr.dev/<organization>/<repo>:<tag>
```

These commands will cause your Buildkite pipeline to download `chainctl` and make it executable. It will then sign in to Chainguard using the Buildkite identity you generated previously. If this workflow can successfully assume the identity, then it will be able to execute the `chainctl images repos list` command and retrieve the list of repos available to the organization.

There are a couple ways you can add commands to an existing Buildkite pipeline, so follow whatever procedure works best for you.

If you followed the [**Getting Started** guide linked in the prerequisites](https://buildkite.com/docs/tutorials/getting-started), your pipeline will have a structure like this.

```
steps:
  - label: "Pipeline upload"
	command: buildkite-agent pipeline upload
```

You could add the commands for testing the identity like this.

```
steps:
  - label: "Buildkite test"
	command: |
	  buildkite-agent pipeline upload
    curl -o chainctl "https://dl.enforce.dev/chainctl/latest/chainctl_$(uname -s | tr '[:upper:]' '[:lower:]')_$(uname -m)"
	  chmod +x chainctl
    token=$(buildkite-agent oidc request-token --audience issuer.enforce.dev)
	  ./chainctl auth login --identity-token $token --identity <your buildkite identity>
    ./chainctl auth configure-docker --identity-token $token --identity <your buildkite identity>
    chainctl images repos list
```

Click the **Save and Build** button. Ensure that your Buildkite agent is running, and then wait a few moments for the pipeline to finish building.

Assuming everything works as expected, your pipeline will be able to assume the identity and run the `chainctl images repos list` command, returning the images available to the organization. Then it will pull an image from the organization's repository.

```
...
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

You can also edit the pipeline itself to change its behavior. For example, instead of listing repos, you could have the workflow inspect the organization.

```
chainctl iam organizations ls
```

Of course, the Buildkite pipeline will only be able to perform certain actions on certain resources, depending on what kind of access you grant it.


## Removing Sample Resources

To remove the resources Terraform created, you can run the `terraform destroy` command.

```sh
terraform destroy
```

This will destroy the role-binding and the identity created in this guide. It will not delete the organization.

You can then remove the working directory to clean up your system.

```sh
rm -r ~/buildkite-id/
```

Following that, all of the example resources created in this guide will be removed from your system.


## Learn more

For more information about how assumable identities work in Chainguard, check out our [conceptual overview of assumable identities](/chainguard/administration/iam-organizations/assumable-ids/). Additionally, the Terraform documentation includes a section on [recommended best practices](https://developer.hashicorp.com/terraform/cloud-docs/recommended-practices) which you can refer to if you'd like to build on this Terraform configuration for a production environment. Likewise, for more information on using Buildkite, we encourage you to check out the [official project documentation](https://buildkite.com/docs), particularly their [documentation on Buildkite OIDC](https://buildkite.com/docs/agent/v3/cli-oidc).
