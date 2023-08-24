---
title: "Image Overview: aws-cli"
type: "article"
description: "Overview: aws-cli Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2022-11-01T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "images-reference"
weight: 500
toc: true
---

[cgr.dev/chainguard/aws-cli](https://github.com/chainguard-images/images/tree/main/images/aws-cli)

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | August 23rd  | `sha256:0c6ae22491e0ccaf41d62e16207c96c4a6593dbe378216cdbc3db5602adde85b` |
|  `latest-dev` | August 23rd  | `sha256:82ee078e1d313db45df2537cd9389ac68968ba753144d908e454ce1c5ec044f8` |



Minimal [aws-cli](https://github.com/aws/aws-cli) container image.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/aws-cli
```

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

