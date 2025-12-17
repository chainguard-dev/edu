---
title : "Create an Assumable Identity to Authenticate from AWS"
linktitle: "AWS"
lead: ""
description: "Tutorial outlining how to create a Chainguard identity that can be assumed by an AWS user or role."
type: "article"
date: 2025-11-28T16:00:00+00:00
lastmod: 2025-11-28T16:00:00+00:00
draft: false
tags: ["Chainguard Containers"]
images: []
weight: 011
---

Chainguard's [*assumable identities*](/chainguard/administration/assumable-ids/assumable-ids/) are identities that can be assumed by external applications or workflows in order to access Chainguard resources or perform certain actions.

This tutorial outlines how to create a Chainguard identity that can be assumed by an AWS user or IAM role and used to authorize requests from AWS services and workloads hosted on platforms like EC2, ECS, Lambda, and EKS.

## Prerequisites

To complete this guide, you will need the following tools.

* The AWS CLI. Review the official documentation for information on [how to install or update to the latest version of the tool](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).
* To create the assumable identity, you will need one of the following tools:
    * [`chainctl`](/chainguard/chainctl-usage/getting-started-with-chainctl/) — the Chainguard command line interface tool. Follow our guide on [How to Install `chainctl`](/chainguard/chainctl-usage/how-to-install-chainctl/) to set this up.
    * [`terraform`](https://developer.hashicorp.com/terraform) — an Infrastructure as Code tool developed by Hashicorp. Follow [the official Terraform documentation](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli) for instructions on installing the tool.


## Create the Assumable Identity

This guide outlines two methods for creating an identity that can be assumed by an AWS user or IAM role: one using `chainctl` over a command-line interface, and another using Terraform.

### CLI

This example creates an identity for an IAM role and binds it to the `registry.pull` role. Replace `<identity-name>` with the name you'd like to give the identity, `<account-id>` with your AWS account ID, and `<role-name>` with the name of your IAM role.

```shell
chainctl iam id create aws role <identity-name> --aws-account-id=<account-id> --aws-role-name=<role-name> --role=registry.pull
```

For an IAM user, use this command. Replace `<identity-name>` with the name you'd like to give the identity, `<account-id>` with your AWS account ID and `<user-name>` with the name of your IAM user.

```shell
chainctl iam id create aws user <identity-name> --aws-account-id=<account-id> --aws-user-name=<user-name> --role=registry.pull
```

If your IAM resources are in the `aws-cn` or `aws-us-gov` [partitions](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/partitions.html), you must specify that with the `--aws-partition` flag. For instance, for a role:

```shell
chainctl iam id create aws role <identity-name> --aws-partition=aws-us-gov --aws-account-id=<account-id> --aws-role-name=<role-name> --role=registry.pull
```

These commands will return the identity's [UIDP (unique identity path)](/chainguard/administration/cloudevents/events-reference/#uidp-identifiers). Note this value down, as you'll need it to assume the identity later.

If you need to retrieve the UIDP later on, you can always run the following `chainctl` command to list the identity.

```sh
chainctl iam identities list --name=<identity-name>
```

If you're unsure which IAM identity your AWS resource is using, you can run `aws sts get-caller-identity` to get the details of the current AWS session. You must run this from the AWS environment you are trying to assume the identity from. For example, if you run this command from an EC2 instance with an assumed role, you might see output like this:

```sh
aws sts get-caller-identity
```
```output
{
	"UserId": "AROAEXAMPLEC2UL7LUB:i-05a6373examplehd2",
	"Account": "452example43",
	"Arn": "arn:aws:sts::452example43:assumed-role/AmazonSSMRoleForInstancesQuickSetup/i-05a6373examplehd2"
}
```

In this example, the role name is `AmazonSSMRoleForInstancesQuickSetup`.

### Terraform

You can also create an assumable identity with the [Chainguard Terraform provider](https://registry.terraform.io/providers/chainguard-dev/chainguard/latest).

The following example demonstrates creating an identity that can be assumed by an IAM role. It binds the `registry.pull` role to the identity.

Substitute your Chainguard organization name for `<org-name>`.

```hcl
data "aws_caller_identity" "current" {}

resource "aws_iam_role" "example" {
  # Configuration omitted for brevity
}

data "chainguard_group" "org" {
  name = "<org-name>"
}

resource "chainguard_identity" "my_identity_name" {
  parent_id   = data.chainguard_group.org.id
  name        = "my-identity-name"

  aws_identity {
    aws_account         = data.aws_caller_identity.current.account_id
    aws_user_id_pattern = "^${aws_iam_role.example.unique_id}:(.+)$"
    aws_arn_pattern     = "^arn:aws:sts::${data.aws_caller_identity.current.account_id}:assumed-role/${aws_iam_role.example.name}/(.+)$"
  }
}

data "chainguard_roles" "registry_pull" {
  name = "registry.pull"
}

resource "chainguard_rolebinding" "my_identity_name_registry_pull" {
  identity = chainguard_identity.my_identity_name.id
  role     = data.chainguard_roles.registry_pull.items[0].id
  group    = data.chainguard_group.org.id
}

output "my_identity_name_id" {
  value = chainguard_identity.my_identity_name.id
}
```

The `my_identity_name_id` output provides the identity’s [UIDP (unique identity path)](/chainguard/administration/cloudevents/events-reference/#uidp-identifiers). You’ll need this value to assume the identity later.

For a full example, refer to the [`aws-auth` example](https://github.com/chainguard-dev/platform-examples/tree/main/aws-auth) in Chainguard's public `platform-examples` repository.


## Assume the Identity

Unlike other supported platforms, AWS does not issue OIDC tokens for its IAM entities. To facilitate assumable identities from AWS workloads, Chainguard accepts a custom token format that is constructed by Base64 encoding a signed AWS API request to [`GetCallerIdentity`](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetCallerIdentity.html).

Chainguard can then use that request and verify that it returns a caller identity that is permitted to assume the Chainguard identity. To better understand the verification logic, refer to the [`aws.VerifyToken`](https://pkg.go.dev/chainguard.dev/sdk@v0.1.44/auth/aws#VerifyToken) function from the [Chainguard SDK For Go](https://pkg.go.dev/chainguard.dev/sdk).

The following sections outline different methods of generating the token, assuming the identity, and using it to interact with the Chainguard API from your AWS resources.

### CLI

You should be able to follow these instructions from any environment, including AWS services like EC2 and EKS, as long as the AWS CLI [can fetch credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) and both `curl` and `chainctl` are installed.

First, use the AWS CLI to retrieve credentials and export them as the `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` and `AWS_SESSION_TOKEN` environment variables:

```shell
eval "$(aws configure export-credentials --format env)"
```

Next, use `curl` to sign a HTTP request with the credentials and base64 encode it. Store the result in the variable `${TOK}`. Substitute `<identity-id>` with the UIDP of your Chainguard identity which you created previously:

```shell
TOK=$(curl -X POST "https://sts.amazonaws.com/?Action=GetCallerIdentity&Version=2011-06-15" \
  --aws-sigv4 "aws:amz:us-east-1:sts" \
  --user "${AWS_ACCESS_KEY_ID}:${AWS_SECRET_ACCESS_KEY}" \
  -H "x-amz-security-token: ${AWS_SESSION_TOKEN}" \
  -H "Chainguard-Identity: <identity-id>" \
  -H "Chainguard-Audience: https://issuer.enforce.dev" \
  -H "Accept: application/json" \
  -v 2>&1 > /dev/null \
  | grep '^> ' \
  | sed 's/> //' \
  | base64 -w0)
```

Finally, use the token to login with `chainctl`. Provide the UIDP of the identity as `<identity-id>`:

```shell
chainctl auth login \
  --identity <identity-id> \
  --identity-token "${TOK}"
```

Now you will be able to issue `chainctl` commands under this assumed identity. For instance, you could list the container image repositories available to your organization:

```shell
chainctl image repo list
```

### Go SDK

The [Chainguard SDK For Go](https://pkg.go.dev/chainguard.dev/sdk) provides an [`aws.GenerateToken`](https://pkg.go.dev/chainguard.dev/sdk@v0.1.44/auth/aws#GenerateToken) function that makes it straightforward to generate a token from AWS credentials that can be exchanged for a Chainguard API token.

For an example of how to leverage this function, refer to the [`aws-auth` example](https://github.com/chainguard-dev/platform-examples/tree/main/aws-auth) in Chainguard's public `platform-examples` repository.

### EC2 instance metadata

If you don't have the AWS CLI installed on your EC2 instance, you can use the [instance metadata service](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html) to retrieve credentials.

Refer to [our AWS EC2 Assumable Identity guide](/chainguard/administration/assumable-ids/identity-examples/aws-ec2-identity/) for more details.

## Learn More

By following this guide, you will have created a Chainguard identity that you can use to authenticate to Chainguard from AWS. For more information about how assumable identities work in Chainguard, check out our [conceptual overview of assumable identities](/chainguard/administration/assumable-ids/assumable-ids/). Additionally, we encourage you to read through the rest of our documentation on [Administering Chainguard resources](/chainguard/administration/).
