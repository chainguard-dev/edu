---
title : "Create an Assumable Identity for a Buildkite Pipeline"
linktitle: "Buildkite"
aliases:
- /chainguard/chainguard-enforce/authentication/identity-examples/enforce-buildkite-identity/
- /chainguard/chainguard-enforce/iam-groups/enforce-buildkite-identity/
- /chainguard/administration/iam-organizations/identity-examples/buildkite-identity/
- /chainguard/administration/assumable-ids/identity-examples/buildkite-identity/
lead: ""
description: "Procedural tutorial outlining how to create a Chainguard identity that can be assumed by a Buildkite workflow."
type: "article"
date: 2023-05-17T08:48:45+00:00
lastmod: 2025-12-11T08:48:45+00:00
draft: false
tags: ["Chainguard Containers", "Procedural"]
images: []
weight: 015
---

Chainguard's [*assumable identities*](/chainguard/administration/iam-organizations/assumable-ids/) are identities that can be assumed by external applications or workflows in order to perform certain tasks that would otherwise have to be done by a human.

This tutorial outlines how to create an identity using Terraform, and then how to update a Buildkite pipeline so that it can assume the identity and interact with Chainguard resources.


## Prerequisites

To complete this guide, you must have the following in place:

* `terraform` installed on your local machine. Terraform is an open-source Infrastructure as Code tool which this guide uses to create various cloud resources. Follow [the official Terraform documentation](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli) for instructions on installing the tool.
* `chainctl` — the Chainguard command line interface tool — installed on your local machine. Follow our guide on [How to Install `chainctl`](/chainguard/chainctl-usage/how-to-install-chainctl/) to set this up.
* A Buildkite agent and pipeline you can use to test out the identity you'll create. We recommend following Buildkite's [Getting Started guide](https://buildkite.com/docs/tutorials/getting-started) to set these up.


## Creating Terraform Files

This guide outlines using Terraform to create an identity for a Buildkite pipeline to assume. This step outlines how to create three Terraform configuration files that, together, produce such an identity.

To help explain each configuration file's purpose, we will go over what they do and how to create each file one by one. First, create a directory to hold the Terraform configuration and navigate into it.

```sh
mkdir ~/buildkite-id && cd $_
```

This will help make it easier to clean up your system at the end of this guide.


### `main.tf`

The first file, named `main.tf`, serves as the scaffolding for our Terraform infrastructure.

The file consists of the following content:

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

`sample.tf` creates a couple of structures that help us test out the identity in a workflow.

This Terraform configuration consists of the following lines:

```hcl
data "chainguard_group" "group" {
  name = "example.com"
}
```

This section looks up a Chainguard IAM organization named `example.com`. You must change this to the name of your Chainguard organization where you want to create the Buildkite identity.

Now you can move on to creating the last of our Terraform configuration files, `buildkite.tf`.

### `buildkite.tf`

The `buildkite.tf` file is what actually creates the identity for your Buildkite workflow to assume. The file consists of four sections, which we'll go over one by one.

The first section creates the identity itself:

```hcl
resource "chainguard_identity" "buildkite" {
  parent_id   = data.chainguard_group.group.id
  name        = "buildkite"
  description = <<EOF
    This is an identity that authorizes Buildkite workflows
    for this pipeline to assume to interact with chainctl.
  EOF

  claim_match {
    issuer          = "https://agent.buildkite.com"
    subject_pattern = "organization:<buildkite-organization>:pipeline:<pipeline>:ref:refs/heads/main:commit:[0-9a-f]+:step:.*"
  }
}
```

First, this section creates a Chainguard Identity tied to the `chainguard_group` specified in the `sample.tf` file. The identity is named `buildkite` and has a brief description.

The most important part of this section is the `claim_match`. When the Buildkite workflow tries to assume this identity later on, it must present a token matching the `issuer` and `subject` specified here in order to do so successfully. The `issuer` is the entity that creates the token, while the `subject` is the entity (here, the Buildkite pipeline build) that the token represents.

In this case, the `issuer` field points to `https://agent.buildkite.com`, the issuer of JWT tokens for Buildkite pipelines.

Instead of pointing to a literal value with a `subject` field, though, this file points to a regular expression using the `subject_pattern` field. When you run a Buildkite pipeline, it generates a unique commit for each build. Passing the regular expression `[0-9a-f]+` allows you to generate an identity that works for every build from this pipeline.

You may refer to [the official Buildkite documentation](https://buildkite.com/docs/agent/v3/cli-oidc#claims) for more details on how Buildkite `issuer` and `subject` claims can be formatted to suit your specific needs. For the purposes of this guide, though, you must replace `<buildkite-organization>` and `<pipeline>` with the name of your Buildkite organization and the name of your Buildkite pipeline.

The next section outputs the new identity's `id` value. This is a unique value that represents the identity itself:

```hcl
output "buildkite-identity" {
  value = chainguard_identity.buildkite.id
}
```

The section after that looks up the `viewer` role:

```hcl
data "chainguard_role" "viewer" {
  name = "viewer"
}
```

The final section grants this role to the identity:

```hcl
resource "chainguard_rolebinding" "view-stuff" {
  identity = chainguard_identity.buildkite.id
  group    = data.chainguard_group.group.id
  role     = data.chainguard_role.viewer.items[0].id
}
```

After creating the `buildkite.tf` file with each of these sections, your Terraform configuration will be ready. Now you can run a few `terraform` commands to create the resources defined in your `.tf` files.

## Creating Your Resources

First, run `terraform init` to initialize Terraform's working directory:

```sh
terraform init
```

Then run `terraform plan`. This produces a speculative execution plan that outlines what steps Terraform will take to create the resources defined in the files you set up in the last section:

```sh
terraform plan
```

If the plan worked successfully and you're satisfied that it will produce the resources you expect, you can apply it. First, though, you'll need to log in to `chainctl` to ensure that Terraform can create the Chainguard resources:

```sh
chainctl auth login
```

Then apply the configuration:

```sh
terraform apply
```

Before going through with applying the Terraform configuration, this command prompts you to confirm that you want it to do so. Enter `yes` to apply the configuration:

```output
...
Plan: 4 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + buildkite-identity = (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value:
```

After pressing `ENTER`, the command will complete and output a `buildkite-identity` value:

```
...

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.

Outputs:

buildkite-identity = "<your-buildkite-identity>"
```

This is the identity's [UIDP (unique identity path)](/chainguard/administration/cloudevents/events-reference/#uidp-identifiers), which you configured the `buildkite.tf` file to emit in the previous section. Note this value down, as you'll need it when you test this identity using a Buildkite workflow. If you need to retrieve this UIDP later on, though, you can always run the following `chainctl` command to obtain a list of the UIDPs of all your existing identities:

```sh
chainctl iam identities ls
```

You're now ready to edit a Buildkite pipeline in order to test out this identity.


## Testing the Identity with a Buildkite Pipeline

To test the identity you created with Terraform in the previous section, navigate to your Buildkite pipeline. From the Buildkite Dashboard, click **Pipelines** in the top navigation bar and then click on the pipeline you specified in the `buildkite.tf` file.

From there, click the **Edit Steps** button to add the following commands to a step in your pipeline. Be sure to replace `<your-buildkite-identity>` with the identity UIDP you noted down in the previous section.

If you followed the [**Getting Started** guide linked in the prerequisites](https://buildkite.com/docs/tutorials/getting-started), your pipeline will have a structure like this.

```Pipeline
steps:
  - label: "Pipeline upload"
    command: buildkite-agent pipeline upload
```

You could add the commands for testing the identity like this:

```Pipeline
- command: |
    curl -o chainctl "https://dl.enforce.dev/chainctl/latest/chainctl_$(uname -s | tr '[:upper:]' '[:lower:]')_$(uname -m)"
    chmod +x chainctl
    mv chainctl /usr/bin
    buildkite-agent oidc request-token --audience issuer.enforce.dev > .token.txt
    chainctl auth login --identity-token $(cat .token.txt) --identity <your-buildkite-identity>
    chainctl auth configure-docker --identity-token $(cat .token.txt) --identity <your-buildkite-identity>
    rm .token.txt
    chainctl images repos list
    docker pull cgr.dev/<organization>/<repo>:<tag>
```

These commands instruct your Buildkite pipeline to download `chainctl` and make it executable. 

The pipeline then runs a `buildkite-agent oidc request-token` command, which requests and prints an OIDC token that claims the Job ID and the specified audience. It pipes this token into a file named `.token.txt`, and then signs in to Chainguard using this token along with the Buildkite identity you generated previously.

If this workflow can successfully assume the identity, it then executes the `chainctl images repos list` command and retrieves the list of repos available to the organization.

Click the **Save and Build** button. Ensure that your Buildkite agent is running, and then wait a few moments for the pipeline to finish building.

### Testing the identity with a Buildkite plugin

You can also create a [Buildkite plugin](https://buildkite.com/docs/pipelines/integrations/plugins/writing) that uses the assumable identity to access your Chainguard resources.

Note that to use a plugin like the following example with the pipeline you created previously, the plugin code must reside in the same repository where the pipeline is running.

To get started, create some directories within your repository:

```sh
mkdir -p .buildkite/plugins/cgrauth/hooks
```

Create a `plugin.yml` file within the `cgrauth` directory. This is a special file that describes what information the plugin requires and what configuration options it accepts:

```sh
cat > .buildkite/plugins/cgrauth/plugin.yml <<EOF
name: Auth
description: Authenticate to pull images
author: https://github.com/<github-id>
requirements: [bash]
configuration:
  properties:
    identity: { type: string }
  required: [identity]
  additionalProperties: false
EOF
```

Be sure to replace `<github-id>` with your GitHub username.

Plugins can implement a number of [plugin hooks](https://buildkite.com/docs/agent/v3/hooks). Run the following command to create a pre-command hook within the `hooks/` subdirectory:

```sh
cat > .buildkite/plugins/cgrauth/hooks/pre-command <<EOF
#!/usr/bin/env bash
set -euo pipefail

identity="${BUILDKITE_PLUGIN_CGRAUTH_IDENTITY:?missing identity}"
curl -o chainctl https://dl.enforce.dev/chainctl/latest/chainctl_$(uname -s | tr "[:upper:]" "[:lower:]")_$(uname -m)
chmod +x chainctl
mv chainctl /usr/bin
token=$(buildkite-agent oidc request-token --audience issuer.enforce.dev)
chainctl auth login --identity-token $token --identity <your-buildkite-identity>
chainctl auth configure-docker --identity-token $token --identity <your-buildkite-identity>
EOF
```

Be sure to replace `<your-buildkite-identity>` with the UIDP of the assumable identity you created earlier.

After merging these new files into your code repository, update your pipeline to use the plugin. The following example is useful for testing that the pipeline can read the identity from the plugin and use it to retrieve a list of your organization's image repositories:

```Pipeline
steps:
  - label: "Buildkite test"
    plugins:
      - "./.buildkite/plugins/cgrauth":
          identity: "<your-buildkite-identity>"
    command:
      - 'chainctl images repos list'
```

Assuming everything works as expected, your pipeline will be able to assume the identity and run the `chainctl images repos list` command, returning a list of images available to your Chainguard organization:

```Pipeline
. . .
$ .buildkite/plugins/cgrauth/hooks/pre-command
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 98.6M  100 98.6M    0     0   177M      0 --:--:-- --:--:-- --:--:--  177M
Successfully exchanged token.
Valid! Id: 45a0c61ea6fd9EXAMPLE5fb9ac06a69eed764595/9753EXAMPLE6d0c8
Updated auth config for cgr.dev
Running commands
$ chainctl images repos list
[cgr.dev/example.com]
├ [adoptium-jdk-fips]
├ [aws-efs-csi-driver]

. . .
```

If you'd like to experiment further with this identity and what the pipeline can do with it, there are a few parts of this setup that you can tweak. For instance, if you'd like to give this identity different permissions you can change the role data source to the role you would like to grant:

```hcl
data "chainguard_roles" "editor" {
  name = "editor"
}
```

You can also edit the pipeline itself to change its behavior. For example, instead of listing repos, you could have the workflow inspect the organization with the `chainctl iam organizations ls` command.

Of course, the Buildkite pipeline is only able to perform certain actions on certain resources depending on what kind of access you grant it.


## Removing Sample Resources

To remove the resources Terraform created, run the `terraform destroy` command:

```sh
terraform destroy
```

This destroys the role-binding and the identity created in this guide. It will not delete the organization.

You can then remove the working directory to clean up your system.

```sh
rm -r ~/buildkite-id/
```

This removes the Terraform configuration files you used to create the example Buildkite resources.


## Learn More

For more information about how assumable identities work in Chainguard, check out our [conceptual overview of assumable identities](/chainguard/administration/iam-organizations/assumable-ids/). Additionally, the Terraform documentation includes a section on [recommended best practices](https://developer.hashicorp.com/terraform/cloud-docs/recommended-practices) which you can refer to if you'd like to build on this Terraform configuration for a production environment. Likewise, for more information on using Buildkite, we encourage you to check out the [official project documentation](https://buildkite.com/docs), particularly their [documentation on Buildkite OIDC](https://buildkite.com/docs/agent/v3/cli-oidc).
