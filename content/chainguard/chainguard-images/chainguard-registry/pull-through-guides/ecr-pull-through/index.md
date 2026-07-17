---
title: "How to set up pull through from Chainguard's registry to Amazon ECR"
linktitle: "Amazon ECR"
type: "article"
description: "Tutorial outlining how to set up an Amazon ECR pull through cache rule for pulling Containers from Chainguard's registry."
date: 2026-03-31T00:00:00+00:00
lastmod: 2026-07-17T00:00:00+00:00
draft: false
tags: ["Chainguard Containers", "Registry"]
images: []
menu:
  docs:
    parent: "pull-through-guides"
toc: true
weight: 007
---

In March 2026, AWS [announced support](https://aws.amazon.com/about-aws/whats-new/2026/03/amazon-ecr-pull-through-cache-chainguard/) for using Amazon Elastic Container Registry (ECR) as a pull through cache for Chainguard's registry. By configuring a pull through cache rule, you can pull Chainguard Containers through your own ECR private registry. ECR caches each image on the first pull and checks the upstream registry for a newer version at most once every 24 hours, which reduces your workloads' direct dependency on Chainguard's registry.

This tutorial outlines how to configure a pull through cache rule for [Chainguard's registry](/chainguard/chainguard-registry/overview/) with [Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html). Unlike some other registries, ECR treats Chainguard as an upstream that requires authentication. This means you store a Chainguard pull token in AWS Secrets Manager and reference it from a cache rule. This guide scopes that rule to your organization's private namespace, so it caches your [Production Containers](/chainguard/chainguard-images/about/images-categories/#production-containers) and lets you pull them with short image paths.

## Prerequisites

To complete this tutorial, you need the following:

* An AWS account with permissions to create ECR pull through cache rules and AWS Secrets Manager secrets. Refer to the AWS guide on [IAM permissions for pull through cache](https://docs.aws.amazon.com/AmazonECR/latest/userguide/pull-through-cache-iam.html) for details.
* The [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) installed and configured, if you plan to follow the command line examples. You can complete every step in the [Amazon ECR console](https://console.aws.amazon.com/ecr/) instead.
* Docker installed on your local machine. Refer to [the official documentation](https://docs.docker.com/engine/install/) to set this up.
* `chainctl`, Chainguard's command-line interface tool, installed on your local machine. If you haven't already installed it, follow our [`chainctl` installation guide](/chainguard/chainctl-usage/how-to-install-chainctl/).

To pull Production Containers, you also need permissions to pull images from your organization's private Chainguard registry. At minimum, you must be granted the `registry.pull` role, though other built-in roles like `owner`, `editor`, or `viewer` also work. Refer to our [Built-in Roles and Capabilities Reference](/chainguard/administration/iam-organizations/roles-role-bindings/capabilities-reference/#pull-token-creator-roles) for more details. If you don't already have access to Production Containers, you can [contact our sales team](https://www.chainguard.dev/contact?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement).

## Creating a Chainguard pull token

Because ECR authenticates to Chainguard's registry on your behalf, you must supply it with credentials. Chainguard [pull tokens](/chainguard/chainguard-registry/authenticating/#authenticating-with-a-pull-token) are longer-lived tokens designed for environments that don't support OIDC, such as CI systems, Kubernetes clusters, or registry mirroring tools like ECR.

First, log in with `chainctl`:

```sh
chainctl auth login
```

Then create a pull token:

```sh
chainctl auth configure-docker --pull-token
```

If you belong to more than one organization, this command prompts you to select one. Choose the organization whose Production Containers you want to pull through ECR. By default, the token expires in 30 days; you can adjust this with the `--ttl` flag (for example, `--ttl=8760h` for one year).

This command prints a `docker login` command that includes `--username` and `--password` arguments:

```output
. . .

    docker login "cgr.dev" --username "<pull_token_ID>" --password "<password>"
```

You don't need to run this `docker login` command, but note down the `<pull_token_ID>` and `<password>` values. You'll supply them to AWS Secrets Manager in the next step.

## Storing your pull token in AWS Secrets Manager

ECR reads your Chainguard credentials from an AWS Secrets Manager secret rather than from the cache rule itself. The secret's name must begin with the `ecr-pullthroughcache/` prefix, and it must be in the same account and Region where you'll create the cache rule.

To create the secret with the AWS CLI, run the following command. Replace `<pull_token_ID>` and `<password>` with the values from the previous step, and set the Region to match the one where you'll create the cache rule:

```sh
aws secretsmanager create-secret \
    --name ecr-pullthroughcache/chainguard \
    --secret-string '{"username":"<pull_token_ID>","accessToken":"<password>"}' \
    --region us-east-2
```

The secret must use the two keys `username` and `accessToken`, and it must be encrypted with the default `aws/secretsmanager` KMS key. ECR doesn't support customer managed keys for pull through cache secrets. The `create-secret` command uses the default key unless you specify otherwise.

Note down the secret's Amazon Resource Name (ARN) from the command's output, as you'll need it when creating the cache rule with the CLI. The ARN has a format like the following:

```ARN
arn:aws:secretsmanager:us-east-2:111122223333:secret:ecr-pullthroughcache/chainguard-a1b2c3
```

Alternatively, you can create the secret in the [AWS Secrets Manager console](https://console.aws.amazon.com/secretsmanager/). Choose **Store a new secret**, select **Other type of secret**, and add two key/value pairs: `username` set to your pull token ID and `accessToken` set to your pull token password. Keep the default `aws/secretsmanager` encryption key, and give the secret a name beginning with `ecr-pullthroughcache/`. You can also create the secret as part of the cache rule workflow described in the next section.

## Creating a pull through cache rule

With your credentials stored, you can create a pull through cache rule that points at Chainguard's registry.

To create the rule with the AWS CLI, run the following command. Replace `--upstream-repository-prefix` with your organization's name (this guide uses `example.com`), replace the `--credential-arn` value with the ARN of the secret you created, and set the Region to match:

```sh
aws ecr create-pull-through-cache-rule \
    --ecr-repository-prefix cg-ecr \
    --upstream-registry-url cgr.dev \
    --upstream-repository-prefix example.com \
    --credential-arn arn:aws:secretsmanager:us-east-2:111122223333:secret:ecr-pullthroughcache/chainguard-a1b2c3 \
    --region us-east-2
```

This command creates a rule scoped to a single Chainguard namespace:

* `--upstream-repository-prefix example.com` limits the rule to your organization's private namespace at `cgr.dev/example.com`. Replace `example.com` with your organization's name or ID, which you can find by running `chainctl iam organizations list -o table`. When you pull an image, ECR matches this prefix and drops it from the image path, so you don't repeat the namespace on every pull.
* `--ecr-repository-prefix cg-ecr` sets the local namespace for the repositories ECR creates, following the scheme `cg-ecr/<image-name>`. You can use any prefix you like; this guide uses `cg-ecr` to keep the local prefix distinct from Chainguard's namespaces.
* `--upstream-registry-url` **must** be set to `cgr.dev`.

Alternatively, you can create the rule in the [Amazon ECR console](https://console.aws.amazon.com/ecr/):

1. From the navigation bar, choose the Region in which to configure your private registry.
2. In the navigation pane, click **Private registry**, then select **Pull through cache** under **Features & Settings**.
3. On the **Pull through cache rules** page, click **Add rule**.
4. On the **Specify upstream** page, select **Chainguard**, then click **Next**.
5. On the **Configure authentication** page, choose **Use an existing AWS secret** and select the secret you created. To create the secret here instead, choose **Create an AWS secret** and enter your pull token ID and password. Click **Next**.
6. On the **Specify namespaces** page, set the **Cache namespace** to `cg-ecr`. ECR populates a default of `chainguard`, but this guide uses `cg-ecr` to keep the local prefix distinct from Chainguard's namespaces. For the **Upstream namespace**, select **A specific prefix** and enter your organization's name (this guide uses `example.com`) to scope the rule to your private namespace. Click **Next**.
7. On the **Review and create** page, review the configuration and click **Create**.

After creating the rule, you can [validate it](https://docs.aws.amazon.com/AmazonECR/latest/userguide/pull-through-cache-working-validating.html) from the console or CLI. Validation confirms that ECR can reach Chainguard's registry and authenticate with your stored credentials.

{{< note >}}
Scoping the rule to a single namespace keeps pull paths short, but it limits the rule to that one namespace. To cache any repository your credentials can access — including your other private namespaces and [Free Containers](/chainguard/chainguard-images/about/images-categories/#free-containers) from the public `chainguard` namespace — omit `--upstream-repository-prefix` on the CLI, or select **No prefix** for the **Upstream namespace** in the console. ECR then defaults to `ROOT` and caches any repository. With an unscoped rule, include the full upstream namespace in each pull path, such as `cg-ecr/example.com/chainguard-base:latest` or `cg-ecr/chainguard/go:latest`.
{{< /note >}}

## Testing pull through from Chainguard's registry to Amazon ECR

Before pulling an image, authenticate Docker to your ECR private registry. Replace `<aws_account_id>` and the Region to match your setup:

```sh
aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.us-east-2.amazonaws.com
```

After logging in, you can pull a Chainguard Container through ECR. Because the rule is scoped to your organization's namespace, ECR drops that namespace from the pull path. Container images pulled through the rule use the following URI format, where the first path element is the repository prefix you configured (`cg-ecr`) and the remainder is the image name:

```
<aws_account_id>.dkr.ecr.<region>.amazonaws.com/cg-ecr/<image-name>:<tag>
```

The following example pulls the `chainguard-base` Production Container from the `example.com` namespace the rule is scoped to:

```sh
docker pull <aws_account_id>.dkr.ecr.us-east-2.amazonaws.com/cg-ecr/chainguard-base:latest
```

Here, `cg-ecr` is your ECR repository prefix and `chainguard-base` is the image name. ECR resolves this to `cgr.dev/example.com/chainguard-base` in Chainguard's registry. You don't include `example.com` in the pull path because the rule is already scoped to it.

On the first pull of an image, ECR creates a repository under the `cg-ecr/` prefix and caches the image. ECR serves subsequent pulls from that cache.

## Debugging pull through from Chainguard's registry to Amazon ECR

If you run into issues when pulling Containers from Chainguard's registry through ECR, check the following:

* Confirm that your environment meets all [Containers network requirements](/chainguard/chainguard-images/network-requirements/). The first pull of an image requires a route to the internet, even if you access ECR through a VPC endpoint.
* When creating the cache rule, ensure the upstream registry URL is set to `cgr.dev`. This field **must not** contain additional components.
* Confirm that your Secrets Manager secret uses the `username` and `accessToken` keys, and that its name begins with the `ecr-pullthroughcache/` prefix. The secret must be in the same account and Region as the cache rule.
* Confirm that the pull token stored in the secret has not expired and that its identity has permission to pull the container images you're requesting.
* If you scoped the rule to a namespace, confirm your pull path omits that namespace. For a rule scoped to `example.com`, pull `cg-ecr/chainguard-base:latest`, not `cg-ecr/example.com/chainguard-base:latest`.
* You can troubleshoot by running `docker login` from another machine (using the pull token credentials) and pulling directly from `cgr.dev/example.com/<image name>`, or from `cgr.dev/chainguard/<image name>` for Free Containers.
* Refer to the AWS guide on [troubleshooting pull through cache issues](https://docs.aws.amazon.com/AmazonECR/latest/userguide/error-pullthroughcache.html) for common errors and their resolutions.

## Learn more

If you haven't already done so, you may find it useful to review our [Registry Overview](/chainguard/chainguard-registry/overview/) to learn more about Chainguard's registry. You can also learn more about Chainguard Containers by checking out our [Containers documentation](/chainguard/chainguard-images/overview/). If you'd like to learn more about Amazon ECR pull through cache rules, refer to the [official AWS documentation](https://docs.aws.amazon.com/AmazonECR/latest/userguide/pull-through-cache.html).
