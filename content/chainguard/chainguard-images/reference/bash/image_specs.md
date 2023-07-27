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
The **bash** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest         | latest-dev     |
|--------------|----------------|----------------|
| Default User | `root`         | `root`         |
| Entrypoint   | `/bin/bash -c` | `/bin/bash -c` |
| CMD          | not specified  | not specified  |
| Workdir      | not specified  | not specified  |
| Has apk?     | no             | yes            |
| Has a shell? | yes            | yes            |

Check the [tags history page](/chainguard/chainguard-images/reference/bash/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|           | latest | latest-dev |
|-----------|--------|------------|
| `curl`    | X      | X          |
| `bash`    | X      | X          |
| `busybox` | X      | X          |
