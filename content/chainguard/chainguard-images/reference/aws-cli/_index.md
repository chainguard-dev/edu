---
title: "Image Overview: aws-cli"
linktitle: "aws-cli"
type: "article"
layout: "single"
description: "Overview: aws-cli Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2023-11-28 00:31:13
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu: 
  docs: 
    parent: "images-reference"
weight: 500
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/aws-cli/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/aws-cli/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/aws-cli/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/aws-cli/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal [aws-cli](https://github.com/aws/aws-cli) container image.
<!--overview:end-->

<!--getting:start-->
## Get It!
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/aws-cli:latest
```
<!--getting:end-->

<!--body:start-->
## Usage

Before using aws-cli, you need to tell it about your [AWS credentials](https://github.com/aws/aws-cli/tree/v2#getting-started).

Jump to official [Getting Started](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-help.html) guide.

```shell
usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help
```

You can get help with any command when using the AWS Command Line Interface (AWS CLI). To do so, simply type help at the end of a command name.

For example, the following command displays help for the general AWS CLI options and the available top-level commands.

```shell
aws help
```
<!--body:end-->

