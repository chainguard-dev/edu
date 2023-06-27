---
title: "Aspnet-runtime Image Variants"
type: "article"
description: "Detailed information about the Aspnet-runtimeChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Aspnet-runtime"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Aspnet-runtime** Image.

## Variants Compared
The **aspnet-runtime** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest            |
|--------------|-------------------|
| Default User | `nonroot`         |
| Entrypoint   | `/usr/bin/dotnet` |
| CMD          | `--help`          |
| Workdir      | not specified     |
| Has apk?     | no                |
| Has a shell? | no                |

Check the [tags history page](/chainguard/chainguard-images/reference/aspnet-runtime/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                    | latest |
|--------------------|--------|
| `dotnet-7`         | X      |
| `dotnet-7-runtime` | X      |
| `aspnet-7-runtime` | X      |
