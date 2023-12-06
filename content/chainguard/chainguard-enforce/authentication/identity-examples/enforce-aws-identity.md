---
title : "Create an Assumable Identity for an AWS role"
linktitle: "AWS Assumable Identity"
lead: ""
description: "Procedural tutorial outlining how to create a Chainguard Enforce identity that can be assumed by an AWS role."
type: "article"
date: 2023-11-28T08:48:45+00:00
lastmod: 2023-11-28T08:48:45+00:00
draft: false
tags: ["Enforce", "Product", "Procedural"]
images: []
weight: 010
---

In Chainguard Enforce, [*assumable identities*](/chainguard/chainguard-enforce/iam-groups/assumable-ids/) are identities that can be assumed by external applications or workflows in order to perform certain tasks that would otherwise have to be done by a human.

This procedural tutorial outlines how to create an identity using Terraform, and then create an AWS role that will assume the identity to interact with Chainguard resources. This can be used to authorize requests from AWS Lambda, ECS, EKS, or any other AWS service that supports [IAM roles for service accounts](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html).


## Prerequisites

To complete this guide, you will need the following.

* `terraform` installed on your local machine. Terraform is an open-source Infrastructure as Code tool which this guide will use to create various cloud resources. Follow [the official Terraform documentation](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli) for instructions on installing the tool.
* `chainctl` — the Chainguard Enforce command line interface tool — installed on your local machine. Follow our guide on [How to Install `chainctl`](/chainguard/chainguard-enforce/how-to-install-chainctl/) to set this up.
* An AWS account with the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) installed and configured. The [Terraform provider for AWS](https://registry.terraform.io/providers/hashicorp/aws/latest/docs) uses credentials configured via the AWS CLI.
* A recent version of [Go](https://go.dev/dl/) to test the identity with AWS Lambda.

## Creating Terraform Files

We will be using Terraform to create an identity for an AWS role to assume. This step outlines how to create the Terraform configuration files that, together, will produce such an identity.

These files are available here: https://github.com/chainguard-dev/platform-examples/tree/main/aws-auth

To help explain each configuration file's purpose, we will go over what they do one by one. First, though, create a directory to hold the Terraform configuration and navigate into it.

```sh
mkdir ~/enforce-aws && cd $_
```

This will help make it easier to clean up your system at the end of this guide.

### `main.tf`

The first file, which we will call `main.tf`, will serve as the scaffolding for our Terraform infrastructure.

The file will consist of the following content.

```
terraform {
  required_providers {
    aws        = { source = "hashicorp/aws" }
    chainguard = { source = "chainguard-dev/chainguard" }
    ko         = { source = "ko-build/ko" }
  }
}
```

This is a fairly barebones Terraform configuration file, but we will define the rest of the resources in the other two files. In `main.tf`, we declare and initialize the Chainguard Terraform provider.

Next, you can look at the `chainguard.tf` file.

### `chainguard.tf`

`chainguard.tf` will create a couple of structures that will help us test out the identity in a workflow.

This Terraform configuration consists of two main parts. The first part of the file will contain the following lines.

```
resource "chainguard_group" "user-group" {
  name   	 = "user-group"
  description = <<EOF
    This group simulates an end-user group, which the AWS role identity
    can interact with via the identity in aws.tf.
  EOF
}
```

This section creates a Chainguard IAM group named `example-group`, as well as a description of the group. This will serve as some data for the identity — which will be created by the `lambda.tf` file — to access when we test it out later on.

Now you can move on to creating the last of our Terraform configuration files, `aws.tf`.

### `lambda.tf`

The `lambda.tf` describes the AWS role that a Lambda function will run as.

```hcl
data "aws_iam_policy_document" "lambda" {
  statement {
    effect  = "Allow"
    actions = ["sts:AssumeRole"]
    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }
  }
}

data "aws_iam_policy" "lambda" {
  name = "AWSLambdaBasicExecutionRole"
}

resource "aws_iam_role" "lambda" {
  name                = "aws-auth"
  assume_role_policy  = data.aws_iam_policy_document.lambda.json
  managed_policy_arns = [data.aws_iam_policy.lambda.arn]
}
```

This describes an AWS role that a Lambda function will run as. The Lambda function will assume this role, and then use the Chainguard identity to interact with Chainguard resources.

In `chainguard.tf`, we define a Chainguard identity that can be assumed by the AWS role:

```hcl
resource "chainguard_identity" "aws" {
  parent_id   = chainguard_group.user-group.id
  name        = "aws-auth-identity"
  description = "Identity for AWS Lambda"

  aws_identity {
    aws_account         = data.aws_caller_identity.current.account_id
    aws_user_id_pattern = "^AROA(.*):${local.lambda_name}$"

    // NB: This role will be assumed so can't use the role ARN directly. We must use the ARN of the assumed role
    aws_arn = "arn:aws:sts::${data.aws_caller_identity.current.account_id}:assumed-role/${aws_iam_role.lambda.name}/${local.lambda_name}"
  }
}
```

The most important part of this section is the `aws_identity` block. When the AWS role tries to assume this identity later on, it must present a token matching the `aws_account`, `aws_user_id_pattern`, and `aws_arn` specified here in order to do so.

The `aws_user_id_pattern` field configures the identity to be assumable only by the AWS role with the specified name, which is itself assumed by another execution role, which we'll configure below. This role will be assumed so can't use the role ARN directly in `aws_arn`; We must used the ARN of the assumed role.

The section after that looks up the `viewer` role.

```
data "chainguard_roles" "viewer" {
  name = "viewer"
}
```

The final section grants this role to the identity on the `example-group`.

```
resource "chainguard_rolebinding" "view-stuff" {
  identity = chainguard_identity.aws.id
  group	= chainguard_group.example-group.id
  role 	= data.chainguard_roles.viewer.items[0].id
}
```

After defining these resources, there are some other resources in the example directory that build and deploy a Lambda function that assumes the identity. We'll describe that code in the next section.

After defining these resources, your Terraform configuration will be ready. Now you can run a few `terraform` commands to create the resources defined in your `.tf` files.

### `lambda.tf`

The file file, `lambda.tf`, will create an AWS Lambda function that will assume the identity you created in the previous section. This function will then use the identity to interact with Chainguard resources.

First, define the following resources in a `lambda.tf` file. The file will consist of three sections, which we'll go over one by one.

This section defines an IAM policy document that will allow the AWS Lambda service to assume the role you'll create in the next section:

```hcl
data "aws_iam_policy_document" "assume_role" {
  statement {
    effect = "Allow"

    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }

    actions = ["sts:AssumeRole"]
  }
}
```

This section defines the role that the AWS Lambda service will assume:

```hcl
resource "aws_iam_role" "iam_for_lambda" {
  name               = "iam_for_lambda"
  assume_role_policy = data.aws_iam_policy_document.assume_role.json
}
```

The final section defines a AWS lambda function implemented in Go that will assume the identity you created in the previous section:

```hcl
resource "aws_lambda_function" "test_lambda" {
  filename      = "lambda_function_payload.zip"
  function_name = "lambda_function_name"
  role          = aws_iam_role.iam_for_lambda.arn
  handler       = "bootstra"

  source_code_hash = data.archive_file.lambda.output_base64sha256

  runtime = "go1.x"

  environment {
    variables = {
      foo = "bar"
    }
  }
}
```

See [this basic example](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lambda_function#basic-example) for configuring AWS Lambda using Terraform, and the docs for [deploying Go Lambda functions with .zip file archives](https://docs.aws.amazon.com/lambda/latest/dg/golang-package.html) for more information on how to configure the `filename` and `source_code_hash` fields.

After it's deployed, when this function is invoked, it will assume the AWS role you created in the previous section. It will then be able to present credentials as that AWS role that will allow it to assume the Chainguard identity you created in the previous section, to view and manage Chainguard resources.

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

Plan: 8 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + aws-identity = (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value:
```

After typing `yes` and pressing `ENTER`, the command will complete and will output an `aws-identity` value.

```
...

Apply complete! Resources: 8 added, 0 changed, 0 destroyed.

Outputs:

aws-identity = "<your identity>"
```

This is the identity's [UIDP (unique identity path)](/chainguard/chainguard-enforce/reference/events/#uidp-identifiers), which you configured the `aws.tf` file to emit in the previous section. Note this value down, as you'll need it to set up the AWS role you'll use to test the identity. If you need to retrieve this UIDP later on, though, you can always run the following `chainctl` command to obtain a list of the UIDPs of all your existing identities.

```sh
chainctl iam identities ls
```

### Testing the Identity

When the AWS Lambda function is invoked, first it needs to get its credentials, which assert that it is the AWS IAM role defined earlier.

The example code in Go does this with `aws-sdk-go-v2`:

```go
// Get AWS credentials.
cfg, err := config.LoadDefaultConfig(ctx)
if err != nil {
  return "", fmt.Errorf("failed to load configuration, %w", err)
}
creds, err := cfg.Credentials.Retrieve(ctx)
if err != nil {
  return "", fmt.Errorf("failed to retrieve credentials, %w", err)
}
```

These credentials represent the AWS role assumed by the Lambda function.

You can use the Chainguard SDK for Go to generate a token that Chainguard understands to authenticate the Lambda function as the Chainguard identity you created earlier, by its UIDP:

```go
// Generate a token and exchange it for a Chainguard token.
awsTok, err := aws.GenerateToken(ctx, creds, env.Issuer, env.Identity)
if err != nil {
  return "", fmt.Errorf("generating AWS token: %w", err)
}
exch := sts.New(env.Issuer, env.APIEndpoint, sts.WithIdentity(env.Identity))
cgtok, err := exch.Exchange(ctx, awsTok)
if err != nil {
  return "", fmt.Errorf("exchanging token: %w", err)
}
```

The resulting token, `cgtok`, can be used to authenticate requests to Chainguard API calls:

```go
// Use the token to list repos in the group.
clients, err := registry.NewClients(ctx, env.APIEndpoint, cgtok)
if err != nil {
  return "", fmt.Errorf("creating clients: %w", err)
}
ls, err := clients.Registry().ListRepos(ctx, &registry.RepoFilter{
  Uidp: &common.UIDPFilter{
    ChildrenOf: env.Group,
  },
})
```

## Removing Sample Resources

To remove the resources Terraform created, you can run the `terraform destroy` command.

```sh
terraform destroy
```

This will destroy the role-binding, and the identity created in this guide. However, you'll need to destroy the `example-group` group yourself with `chainctl`. It will also delete all the AWS resources defined earlier in `chainguard.tf` and `lambda.tf`.

```sh
chainctl iam groups rm example-group
```

You can then remove the working directory to clean up your system.

```sh
rm -r ~/enforce-aws/
```

Following that, all of the example resources created in this guide will be removed from your system.

## Learn more

For more information about how assumable identities work in Chainguard Enforce, check out our [conceptual overview of assumable identities](/chainguard/chainguard-enforce/iam-groups/assumable-ids/). Additionally, the Terraform documentation includes a section on [recommended best practices](https://developer.hashicorp.com/terraform/cloud-docs/recommended-practices) which you can refer to if you'd like to build on this Terraform configuration for a production environment.
