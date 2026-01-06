---
title : "Create an Assumable Identity to Authenticate from AWS"
linktitle: "AWS"
lead: ""
description: "Tutorial outlining how to create a Chainguard identity that can be assumed by an AWS user or role using outbound identity federation."
type: "article"
date: 2026-01-05T09:00:00+00:00
lastmod: 2026-01-05T09:00:00+00:00
draft: false
tags: ["Chainguard Containers"]
images: []
weight: 011
---

Chainguard's [*assumable identities*](/chainguard/administration/assumable-ids/assumable-ids/) are identities that can be assumed by external applications or workflows in order to access Chainguard resources or perform certain actions.

This tutorial outlines how to create a Chainguard identity that can be assumed by an AWS IAM user or IAM role using [AWS IAM outbound identity federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_outbound.html).

## Prerequisites

To complete this guide, outbound identity federation must be enabled for your AWS account. Follow [the official AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_outbound_getting_started.html#enable-outbound-federation) to set this up.

You will also need the following tools.

* The AWS CLI. Review the official documentation for information on [how to install or update to the latest version of the tool](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).
* To create the assumable identity, you will need one of the following tools:
    * [`chainctl`](/chainguard/chainctl-usage/getting-started-with-chainctl/) — the Chainguard command line interface tool. Follow our guide on [How to Install `chainctl`](/chainguard/chainctl-usage/how-to-install-chainctl/) to set this up.
    * [`terraform`](https://developer.hashicorp.com/terraform) — an Infrastructure as Code tool developed by Hashicorp. Follow [the official Terraform documentation](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli) for instructions on installing the tool.

## Retrieve Token Issuer URL

Each AWS account has a different issuer URL for outbound identity federation. You can retrieve it from the AWS Console UI by navigating to `IAM > Account settings > STS` as described in [the official getting started guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_outbound_getting_started.html).

The token issuer URL will align with the following format:

```
https://<uuid>.tokens.sts.global.api.aws
```

## Create the Identity

This guide outlines two methods for creating an identity that can be assumed by an AWS user or IAM role: one using `chainctl` over a command-line interface, and another using Terraform.

### CLI

Firstly, attach a policy to your AWS role or user that allows it to call `sts:GetWebIdentityToken` for the `https://issuer.enforce.dev` audience. The following example is a minimal policy that allows this:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "sts:GetWebIdentityToken",
            "Resource": "*",
            "Condition": {
                "ForAnyValue:StringEquals": {
                    "sts:IdentityTokenAudience": "https://issuer.enforce.dev"
                },
                "NumericLessThanEquals": {
                    "sts:DurationSeconds": 300
                }
            }
        }
    ]
}
```

Then, run this command which uses `chainctl` to create a Chainguard identity and assign it the `registry.pull` role. Substitute `<identity-name>`, `<issuer-url>` and `<aws-arn>` with the name you want to give the identity, the issuer URL you just retrieved and the ARN of the AWS user or role you want to assume the identity with, respectively.

```shell
chainctl iam id create <identity-name> --identity-issuer=<issuer-url> --subject=<aws-arn> --role=registry.pull
```

This command should return the identity's [UIDP (unique identity path)](/chainguard/administration/cloudevents/events-reference/#uidp-identifiers). Note this value down, as you'll need it to assume the identity later.

If you need to retrieve the UIDP later on, you can always run the following `chainctl` command to list the identity.

```sh
chainctl iam identities list --name=<identity-name>
```

If you're unsure which ARN or issuer URL to provide to `chainctl iam id create`, you can issue a token with `aws sts get-web-identity-token` and inspect the claims with `jwt`. To complete this command, you must install `jwt` as described on [this page](https://github.com/mike-engel/jwt-cli#installation).

```shell
aws sts get-web-identity-token \
  --audience=https://issuer.enforce.dev \
  --signing-algorithm=ES384 \
  --query WebIdentityToken \
  --output text \
  | jwt decode -j - \
```

The output will look like this:

```json
{
  "header": {
    "typ": "JWT",
    "alg": "ES384",
    "kid": "EC384_0"
  },
  "payload": {
    "aud": "https://issuer.enforce.dev",
    "exp": 1766915543,
    "https://sts.amazonaws.com/": {
      "aws_account": "123456789012",
      "org_id": "o-anih79mrvn",
      "original_session_exp": "2025-12-28T10:45:29Z",
      "ou_path": [
        "o-anih79mrvn/r-amv9/ou-amv9-ndi0nlgq/"
      ],
      "principal_id": "arn:aws:iam::123456789012:role/example",
      "source_region": "us-west-2"
    },
    "iat": 1766915243,
    "iss": "https://00000000-0000-0000-0000-000000000000.tokens.sts.global.api.aws",
    "jti": "00000000-0000-0000-0000-000000000000",
    "sub": "arn:aws:iam::123456789012:role/example"
  }
}
```

The `sub` and `iss` claims are the values you should provide to `--subject` and `--identity-issuer`, respectively.

### Terraform

You can also create an assumable identity with the [Chainguard Terraform provider](https://registry.terraform.io/providers/chainguard-dev/chainguard/latest). The following example demonstrates creating an identity that can be assumed by an IAM role. It binds the `registry.pull` role to the identity.

Substitute your Chainguard organization name for `<org-name>` and the issuer URL for `<issuer-url>`.

```hcl
terraform {
  required_providers {
    aws        = { source = "hashicorp/aws" }
    chainguard = { source = "chainguard-dev/chainguard" }
  }
}

data "aws_caller_identity" "current" {}

resource "aws_iam_role" "example" {
  name = "example-role"

  # Configuration omitted for brevity
}

resource "aws_iam_role_policy" "example_policy" {
  name = "web-identity-token-policy"
  role = aws_iam_role.example.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect   = "Allow"
        Action   = "sts:GetWebIdentityToken"
        Resource = "*"
        Condition = {
          "ForAnyValue:StringEquals" = {
            "sts:IdentityTokenAudience" = "https://issuer.enforce.dev"
          }
          "NumericLessThanEquals" : {
            "sts:DurationSeconds" : 300
          }
        }
      }
    ]
  })
}

data "chainguard_group" "org" {
  name = "<org-name>"
}

resource "chainguard_identity" "my_identity_name" {
  parent_id = data.chainguard_group.org.id
  name      = "my-identity-name"
  claim_match {
    issuer  = "<issuer-url>"
    subject = aws_iam_role.example.arn
  }
}

data "chainguard_role" "registry_pull" {
  name = "registry.pull"
}

resource "chainguard_rolebinding" "my_identity_name_registry_pull" {
  identity = chainguard_identity.my_identity_name.id
  role     = data.chainguard_role.registry_pull.items[0].id
  group    = data.chainguard_group.org.id
}

output "my_identity_name_id" {
  value = chainguard_identity.my_identity_name.id
}
```

The `my_identity_name_id` output provides the identity’s [UIDP (unique identity path)](/chainguard/administration/cloudevents/events-reference/#uidp-identifiers). You’ll need this value to assume the identity later.

## Assume the Identity

After creating an identity with either method outlined previously, generate a token with `aws sts get-web-identity-token`:

```shell
TOK=$(aws sts get-web-identity-token --audience=https://issuer.enforce.dev --signing-algorithm=ES384 --query WebIdentityToken --output text)
```

Then use the token to log in with `chainctl`. Provide the UIDP of the identity as `<identity-id>`:

```shell
chainctl auth login \
  --identity <identity-id> \
  --identity-token "${TOK}"
```

Now you will be able to issue `chainctl` commands under this assumed identity. For instance, you could list the container image repositories available to your organization:

```shell
chainctl image repo list
```

## Learn More

By following this guide, you will have created a Chainguard identity that you can use to authenticate to Chainguard from AWS. For more information about how assumable identities work in Chainguard, check out our [conceptual overview of assumable identities](/chainguard/administration/assumable-ids/assumable-ids/). Additionally, we encourage you to read through the rest of our documentation on [Administering Chainguard resources](/chainguard/administration/).
