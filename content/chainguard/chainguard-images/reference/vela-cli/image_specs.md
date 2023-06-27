---
title: "Vela-cli Image Variants"
type: "article"
description: "Detailed information about the Vela-cliChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Vela-cli"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Vela-cli** Image.

## Variants Compared
The **vela-cli** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest          |
|--------------|-----------------|
| Default User | `nonroot`       |
| Entrypoint   | `/usr/bin/vela` |
| CMD          | not specified   |
| Workdir      | not specified   |
| Has apk?     | no              |
| Has a shell? | yes             |

Check the [tags history page](/chainguard/chainguard-images/reference/vela-cli/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                          | latest |
|--------------------------|--------|
| `ca-certificates-bundle` | X      |
| `kubevela`               | X      |
| `bash`                   | X      |
| `expat`                  | X      |
