---
title: "Google-cloud-sdk Image Variants"
type: "article"
description: "Detailed information about the Google-cloud-sdk Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Google-cloud-sdk"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Google-cloud-sdk** Image.

## Variants Compared
The **google-cloud-sdk** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest            | latest-dev        |
|--------------|-------------------|-------------------|
| Default User | `gcloud`          | `gcloud`          |
| Entrypoint   | not specified     | not specified     |
| CMD          | `/usr/bin/gcloud` | `/usr/bin/gcloud` |
| Workdir      | not specified     | not specified     |
| Has apk?     | yes               | yes               |
| Has a shell? | yes               | yes               |

Check the [tags history page](/chainguard/chainguard-images/reference/google-cloud-sdk/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                    | latest | latest-dev |
|--------------------|--------|------------|
| `google-cloud-sdk` | X      | X          |
| `apk-tools`        | X      | X          |
| `busybox`          | X      | X          |
| `bash`             | X      | X          |
