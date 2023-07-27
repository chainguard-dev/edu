---
title: "Pulumi Image Variants"
type: "article"
description: "Detailed information about the Pulumi Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Pulumi"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Pulumi** Image.

## Variants Compared
The **pulumi** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest            | latest-dev        |
|--------------|-------------------|-------------------|
| Default User | `root`            | `root`            |
| Entrypoint   | `/usr/bin/pulumi` | `/usr/bin/pulumi` |
| CMD          | `-h`              | `-h`              |
| Workdir      | not specified     | not specified     |
| Has apk?     | no                | yes               |
| Has a shell? | yes               | yes               |

Check the [tags history page](/chainguard/chainguard-images/reference/pulumi/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                           | latest | latest-dev |
|---------------------------|--------|------------|
| `pulumi`                  | X      | X          |
| `pulumi-watch`            | X      | X          |
| `busybox`                 | X      | X          |
| `pulumi-language-go`      | X      | X          |
| `go`                      | X      | X          |
| `pulumi-language-dotnet`  | X      | X          |
| `dotnet-7`                | X      | X          |
| `dotnet-7-runtime`        | X      | X          |
| `dotnet-7-sdk`            | X      | X          |
| `aspnet-7-runtime`        | X      | X          |
| `aspnet-7-targeting-pack` | X      | X          |
| `pulumi-language-python`  | X      | X          |
| `python-3.11`             | X      | X          |
| `py3.11-pip`              | X      | X          |
| `python-3.11-dev`         | X      | X          |
| `pulumi-language-nodejs`  | X      | X          |
| `nodejs`                  | X      | X          |
| `nghttp2`                 | X      | X          |
| `pulumi-language-java`    | X      | X          |
| `glibc-locale-en`         | X      | X          |
| `openjdk-17-jre`          | X      | X          |
| `openjdk-17-default-jvm`  | X      | X          |
| `openjdk-17`              | X      | X          |
| `libstdc++`               | X      | X          |
| `maven`                   | X      | X          |
| `pulumi-language-yaml`    | X      | X          |
| `git`                     | X      | X          |
| `bash`                    | X      | X          |
| `openssh`                 | X      | X          |
| `openssh-keyscan`         | X      | X          |
