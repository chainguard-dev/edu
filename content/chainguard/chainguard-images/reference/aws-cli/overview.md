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
|  `latest`     | August 16th  | `sha256:7057cd1e1927f00dd2d46461d63529afe66b28699c600e36350216be4cdf5084` |
|  `latest-dev` | August 16th  | `sha256:f1fd022f4bd66e6eb2a0c695845fdf2c4efd0d1678fd7529913eec21c0bb50bf` |



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

