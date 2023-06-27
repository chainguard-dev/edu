---
title: "Fluent-bit Image Variants"
type: "article"
description: "Detailed information about the Fluent-bitChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Fluent-bit"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Fluent-bit** Image.

## Variants Compared
The **fluent-bit** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest                               |
|--------------|--------------------------------------|
| Default User | `nonroot`                            |
| Entrypoint   | `/usr/bin/fluent-bit`                |
| CMD          | `-c /fluent-bit/etc/fluent-bit.conf` |
| Workdir      | not specified                        |
| Has apk?     | no                                   |
| Has a shell? | no                                   |

Check the [tags history page](/chainguard/chainguard-images/reference/fluent-bit/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                    | latest |
|--------------------|--------|
| `fluent-bit`       | X      |
| `wolfi-baselayout` | X      |
