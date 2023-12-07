---
title : "Create an Assumable Identity for a GitLab CI/CD Pipeline"
linktitle: "GitLab CI/CD Assumable Identity"
lead: ""
description: "Procedural tutorial outlining how to create a Chainguard Enforce identity that can be assumed by a GitLab CI/CD pipeline."
type: "article"
date: 2023-06-28T08:48:45+00:00
lastmod: 2023-09-22T08:48:45+00:00
draft: false
tags: ["Enforce", "Product", "Procedural"]
images: []
weight: 010
---

In Chainguard Enforce, [*assumable identities*](/chainguard/chainguard-enforce/iam-groups/assumable-ids/) are identities that can be assumed by external applications or workflows in order to perform certain tasks that would otherwise have to be done by a human.

This procedural tutorial outlines how to create an identity using Terraform, and then create a GitLab CI/CD pipeline that will assume the identity to interact with Chainguard resources.


## Prerequisites

To complete this guide, you will need the following.

* `terraform` installed on your local machine. Terraform is an open-source Infrastructure as Code tool which this guide will use to create various cloud resources. Follow [the official Terraform documentation](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli) for instructions on installing the tool.
* `chainctl` — the Chainguard Enforce command line interface tool — installed on your local machine. Follow our guide on [How to Install `chainctl`](/chainguard/chainguard-enforce/how-to-install-chainctl/) to set this up.
* A GitLab project and CI/CD pipeline you can use to test out the identity you'll create. GitLab provides a [quickstart tutorial on creating your first pipeline](https://docs.gitlab.com/ee/ci/quick_start/) which can be useful for getting a testing pipeline up and running.


## Creating Terraform Files

We will be using Terraform to create an identity for a GitLab pipeline to assume. This step outlines how to create three Terraform configuration files that, together, will produce such an identity.

To help explain each configuration file's purpose, we will go over what they do and how to create each file one by one. First, though, create a directory to hold the Terraform configuration and navigate into it.

```sh
mkdir ~/enforce-gitlab && cd $_
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

This section looks up a Chainguard IAM group named `my-customer.biz`. This will contain the identity — which will be created by the `gitlab.tf` file — to access when we test it out later on.

Now you can move on to creating the last of our Terraform configuration files, `gitlab.tf`.

### `gitlab.tf`

The `gitlab.tf` file is what will actually create the identity for your GitLab CI pipeline workflow to assume. The file will consist of four sections, which we'll go over one by one.

The first section creates the identity itself.

```
resource "chainguard_identity" "gitlab" {
  parent_id   = chainguard_group.group.id
  name    	= "gitlab-ci"
  description = <<EOF
	This is an identity that authorizes Gitlab CI in this
	repository to assume to interact with chainctl.
  EOF

  claim_match {
    issuer   = "https://gitlab.com"
    subject  = "project_path:<group_name>/<project_name>:ref_type:branch:ref:main"
    audience = "https://gitlab.com"
  }
}
```

First this section creates a Chainguard Identity tied to the `chainguard_group` looked up in the `sample.tf` file. The identity is named `gitlab-ci` and has a brief description.

The most important part of this section is the `claim_match`. When the GitLab pipeline tries to assume this identity later on, it must present a token matching the `issuer`, `subject`, and `audience` specified here in order to do so. The `issuer` is the entity that creates the token, the `subject` is the entity that the token represents (here, the GitLab pipeline), and the `audience` is the intended recipient of the token.

In this case, the `issuer` field points to `https://gitlab.com`, the issuer of JWT tokens for GitLab pipelines. Likewise, the `audience` field also points to `https://gitlab.com`. This will work for demonstration purposes, but if you're taking advantage of GitLab's support for custom audiences then be sure to change this to the appropriate audience.

The GitLab documentation provides [several examples of `subject` claims](https://docs.gitlab.com/ee/ci/cloud_services/#configure-a-conditional-role-with-oidc-claims) which you can refer to if you want to construct a `subject` claim specific to your needs. For the purposes of this guide, though, you will need to replace `<group_name>` and `<project_name>` with the name of your GitLab group and project names, respectively.

The next section will output the new identity's `id` value. This is a unique value that represents the identity itself.

```
output "gitlab-identity" {
  value = chainguard_identity.gitlab.id
}
```

The section after that looks up the `viewer` role.

```
data "chainguard_roles" "viewer" {
  name = "viewer"
}
```

The final section grants this role to the identity on the group.

```
resource "chainguard_rolebinding" "view-stuff" {
  identity = chainguard_identity.gitlab.id
  group	= chainguard_group.group.id
  role 	= data.chainguard_roles.viewer.items[0].id
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
  + gitlab-identity = (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value:
```

After typing `yes` and pressing `ENTER`, the command will complete and will output a `gitlab-ci` value.

```
...

Apply complete! Resources: 4 added, 0 changed, 0 destroyed.

Outputs:

gitlab-identity = "<your actions identity>"
```

This is the identity's [UIDP (unique identity path)](/chainguard/chainguard-enforce/reference/events/#uidp-identifiers), which you configured the `gitlab.tf` file to emit in the previous section. Note this value down, as you'll need it to set up the GitLab CI pipeline you'll use to test the identity. If you need to retrieve this UIDP later on, though, you can always run the following `chainctl` command to obtain a list of the UIDPs of all your existing identities.

```sh
chainctl iam identities ls
```

Note that you may receive a `PermissionDenied` error part way through the apply step. If so, run `chainctl auth login` once more, and then `terraform apply` again to resume creating the identity and resources.

You're now ready to create a GitLab CI pipeline which you'll use to test out this identity.

## Testing the identity with a GitLab CI/CD Pipeline

From the GitLab Dashboard, select **Projects** in the left-hand sidebar menu. From there, click on the project you specified in the `subject` claim to be taken to the project overview. There, in the list of the repository's contents, there will be a file named `.gitlab-ci.yml`. This is a special file that's required when using GitLab CI/CD, as it contains the CI/CD configuration.

Click on the `.gitlab-ci.yml` file, then click the **Edit** button and select an option for editing the file. For the purpose of this guide, delete whatever content is in this file to start and replace it with the following.

```
image: cgr.dev/chainguard/wolfi-base

stages:
  - assume-and-explore

assume-and-explore:
  id_tokens:
    ID_TOKEN_1:
      aud: https://gitlab.com

  stage: assume-and-explore

  script:
  - |
    # Install chainctl.
    wget -O chainctl "https://dl.enforce.dev/chainctl/latest/chainctl_linux_$(uname -m)"
    chmod +x chainctl
    mv chainctl /usr/bin

    # Assume the identity.
    chainctl auth login \
      --identity-token $ID_TOKEN_1 \
      --identity <your gitlab identity>
    chainctl auth configure-docker \
      --identity-token $ID_TOKEN_1 \
      --identity <your gitlab identity>

    # Explore available images.
    chainctl images repos list

    # Pull an image.
    docker pull cgr.dev/<group>/<repo>:<tag>
```

Let's go over what this configuration does.

First, GitLab requires that pipelines have a shell. To this end, this configuration uses the [`cgr.dev/chainguard/wolfi-base` image](https://edu.chainguard.dev/chainguard/chainguard-images/reference/wolfi-base/) since it includes the `sh` shell.

Next, this configuration creates a JSON Web Token (JWT) with an [`id_tokens`](https://docs.gitlab.com/ee/ci/yaml/index.html#id_tokens) block that will allow the job to be able to fetch an OIDC token and authenticate with Chainguard Enforce. GitLab requires that any JWTs created in this manner must include an `aud` keyword. In this case, it should align with the `audience` associated with the Chainguard identity created in the `gitlab.tf` file: `https://gitlab.com`.

Following that, the job runs a few commands to download and install `chainctl`. It then uses `chainctl`, the JWT, and the Chainguard identity's `id` value to log in to Chainguard Enforce under the assumed identity. Be sure to replace `<your gitlab identity>` with the identity UIDP you noted down in the previous section.

After logging in, the pipeline is able to run any `chainctl` command under the assumed identity. To test out this ability, this configuration runs the `chainctl images repos list` command to list all available image repos associated associated with the group.

After updating the configuration, commit the changes and the pipeline will run automatically. A status box in the dashboard will let you know whether the pipeline runs successfully.

Click the **View Pipeline** button, and then click the **assume-and-explore** job button to open the job's output from the last run. There you should see a list of repos accessible to your group.

This indicates that the GitLab CI/CD pipeline did indeed assume the identity and run the `chainctl images repos list` command.

If you'd like to experiment further with this identity and what the workflow can do with it, there are a few parts of this setup that you can tweak. For instance, if you'd like to give this identity different permissions you can change the role data source to the role you would like to grant.

```
data "chainguard_roles" "editor" {
  name = "editor"
}
```

To retrieve a list of all the available roles — including any custom roles — you can run the following command.

```sh
chainctl iam roles list
```

You can also edit the pipeline itself to change its behavior. For example, instead of inspecting the image repos the identity has access to, you could have the workflow inspect the groups like in the following exmaple.

```
chainctl iam groups ls
```

Of course, the GitLab pipeline will only be able to perform certain actions on certain resources, depending on what kind of access you grant it.


## Removing Sample Resources

To remove the resources Terraform created, you can run the `terraform destroy` command.

```sh
terraform destroy
```

This will destroy identity and the role-binding created in this guide. It will not delete the group.

You can then remove the working directory to clean up your system.

```sh
rm -r ~/enforce-gitlab/
```

Following that, all of the example resources created in this guide will be removed from your system.


## Learn more

For more information about how assumable identities work in Chainguard Enforce, check out our [conceptual overview of assumable identities](/chainguard/chainguard-enforce/iam-groups/assumable-ids/). Additionally, the Terraform documentation includes a section on [recommended best practices](https://developer.hashicorp.com/terraform/cloud-docs/recommended-practices) which you can refer to if you'd like to build on this Terraform configuration for a production environment. Likewise, for more information on using GitLab CI/CD pipelines, we encourage you to check out the [official documentation on the subject](https://docs.gitlab.com/ee/ci/pipelines/).
