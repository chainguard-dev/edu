---
title: "dotnet-sdk Image Variants"
type: "article"
description: "Detailed specs for dotnet-sdk Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "dotnet-sdk"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **dotnet-sdk** Image.

## Variants Compared
The **dotnet-sdk** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest        | latest-dev    |
|--------------|---------------|---------------|
| Default User | `nonroot`     | `nonroot`     |
| Entrypoint   | not specified | not specified |
| CMD          | `/bin/sh -l`  | `/bin/sh -l`  |
| Workdir      | not specified | not specified |
| Has apk?     | no            | yes           |
| Has a shell? | yes           | yes           |

## Image Dependencies
The table shows package distribution across all variants.

|                           | latest | latest-dev |
|---------------------------|--------|------------|
| `busybox`                 | X      | X          |
| `ca-certificates-bundle`  | X      | X          |
| `dotnet-7-sdk`            | X      | X          |
| `aspnet-7-runtime`        | X      | X          |
| `aspnet-7-targeting-pack` | X      | X          |
| `apk-tools`               |        | X          |
| `bash`                    |        | X          |
| `git`                     |        | X          |

