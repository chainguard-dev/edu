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
|  `latest`     | July 18th    | `sha256:65b1c1bda7ad7524945fc7b68a14d5c9df3d1c091e8b28685493e80dac275db5` |
|  `latest-dev` | July 18th    | `sha256:f47e604a3390b236c15a6292143f1d4c5ec769376853af8140cd0db5ef2edeec` |
|               | June 30th    | `sha256:1e99d5de37e9141e97f8880b14417de7bf9b8d9e9929818b94ba7edf338e8f8a` |
|               | June 30th    | `sha256:1b14456a9aec9d51e6089fce3b73fc3073d9d04b552a492377a3127a80413850` |
|               | June 29th    | `sha256:60350073ba18f36e669ecb31b6d42bdb2f9286423d104b3b0bdca673777a0b0f` |
|               | June 29th    | `sha256:b32271017437677ccf906eb37fb0c8bc05be68bda06baac3317e44546154a1a3` |
|               | June 28th    | `sha256:0c4f10ac12064be40de00f84afc9f35ac21a0d0903a88f228dbadff552f2a584` |
|               | June 28th    | `sha256:0dfcf5b46f3c30e29cbb12194fa61274ca47dd6f4c2308fcfbc3f79a9392bcea` |
|               | June 27th    | `sha256:5060c4783e6299b807184c9350f0ec7f93494f4220e516b68719e0999b4f1943` |
|               | June 27th    | `sha256:540819044569c4d82156bb06f8a87324326384b584b6cef7ca0309b462ade8eb` |
|               | June 26th    | `sha256:20f83f002f05ecc72e206ba4774674fcb6dd16db5dc3e71b831b97dfc40163d5` |
|               | June 26th    | `sha256:26b18780d6dbbe0641a6893bad4303ae85a1a838dffb4f2394eb18b7f3ba2c4c` |
|               | June 22nd    | `sha256:cbb518827f8210b13609441b0fb860abfbdd3fa749fa971da49234272ff8f58d` |
|               | June 22nd    | `sha256:6f6e87ed28ac41f2e331d75179407ddca18f265ff6b8e9b94e430fcc06449261` |
|               | June 21st    | `sha256:5510642de5c9f279de63b43f9ee1322dbffaeec84b1ef9a24054f7491766f0c6` |
|               | June 21st    | `sha256:49814871ddc6e51a42fec215109f23ba86d4da97659d7cff0f56c9753a8f5f41` |
|               | June 20th    | `sha256:b676cf153abe92eec1c9ff9980e999ec3aafa9ccc93c3df15a7be516b14393c1` |
|               | June 20th    | `sha256:f97e5800ade868bacb4e663b31df08fea6c8ee604f3edd26496fd9b172efebfc` |
|               | June 19th    | `sha256:d9da71927050ed50545b58b1634cb831d571c6dadc47bf93ae0ae5039a0ffb40` |
|               | June 19th    | `sha256:b63d07a443cb78498298c6616a957f6255a19799a0038b714dc87dd5c4fdc1b1` |



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

