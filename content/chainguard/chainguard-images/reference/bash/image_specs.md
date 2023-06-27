---
title: "Bash Image Variants"
type: "article"
description: "Detailed information about the BashChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Bash"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Bash** Image.

## Variants Compared
The **bash** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest         |
|--------------|----------------|
| Default User | `root`         |
| Entrypoint   | `/bin/bash -c` |
| CMD          | not specified  |
| Workdir      | not specified  |
| Has apk?     | no             |
| Has a shell? | yes            |

Check the [tags history page](/chainguard/chainguard-images/reference/bash/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                          | latest |
|--------------------------|--------|
| `curl`                   | X      |
| `bash`                   | X      |
| `busybox`                | X      |
| `ca-certificates-bundle` | X      |
