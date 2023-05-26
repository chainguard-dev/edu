---
title: "pulumi Image Variants"
type: "article"
description: "Detailed specs for pulumi Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "pulumi"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **pulumi** Image.

## Variants Compared
The **pulumi** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest            |
|--------------|-------------------|
| Default User | `pulumi`          |
| Entrypoint   | `/usr/bin/pulumi` |
| CMD          | `-h`              |
| Workdir      | not specified     |
| Has apk?     | no                |
| Has a shell? | yes               |

## Image Dependencies
The table shows package distribution across all variants.

|                           | latest |
|---------------------------|--------|
| `pulumi`                  | X      |
| `pulumi-watch`            | X      |
| `wolfi-baselayout`        | X      |
| `ca-certificates-bundle`  | X      |
| `busybox`                 | X      |
| `pulumi-language-go`      | X      |
| `go`                      | X      |
| `pulumi-language-dotnet`  | X      |
| `dotnet-7`                | X      |
| `dotnet-7-runtime`        | X      |
| `dotnet-7-sdk`            | X      |
| `aspnet-7-runtime`        | X      |
| `aspnet-7-targeting-pack` | X      |
| `pulumi-language-python`  | X      |
| `python-3.11`             | X      |
| `py3.11-pip`              | X      |
| `python-3.11-dev`         | X      |
| `pulumi-language-nodejs`  | X      |
| `nodejs`                  | X      |
| `nghttp2`                 | X      |
| `pulumi-language-java`    | X      |
| `glibc-locale-en`         | X      |
| `openjdk-17-jre`          | X      |
| `openjdk-17-default-jvm`  | X      |
| `openjdk-17`              | X      |
| `libstdc++`               | X      |
| `maven`                   | X      |
| `pulumi-language-yaml`    | X      |

