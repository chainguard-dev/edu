---
title: "Openai Image Variants"
type: "article"
description: "Detailed information about the Openai Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Openai"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Openai** Image.

## Variants Compared
The **openai** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest            | latest-dev        |
|--------------|-------------------|-------------------|
| Default User | `nonroot`         | `nonroot`         |
| Entrypoint   | `/usr/bin/openai` | `/usr/bin/openai` |
| CMD          | `--help`          | `--help`          |
| Workdir      | not specified     | not specified     |
| Has apk?     | no                | yes               |
| Has a shell? | yes               | yes               |

Check the [tags history page](/chainguard/chainguard-images/reference/openai/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|           | latest | latest-dev |
|-----------|--------|------------|
| `busybox` | X      | X          |
| `openai`  | X      | X          |
