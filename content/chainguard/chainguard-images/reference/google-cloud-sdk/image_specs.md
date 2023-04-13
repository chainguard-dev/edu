---
title: "google-cloud-sdk Image Variants"
type: "article"
description: "Detailed specs for google-cloud-sdk Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "google-cloud-sdk"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **google-cloud-sdk** Image.

## Variants Compared
The **google-cloud-sdk** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest            |
|--------------|-------------------|
| Default User | `gcloud`          |
| Entrypoint   | not specified     |
| CMD          | `/usr/bin/gcloud` |
| Workdir      | not specified     |
| Has apk?     | yes               |
| Has a shell? | yes               |

## Image Dependencies
The table shows package distribution across all variants.

|                          | latest |
|--------------------------|--------|
| `ca-certificates-bundle` | X      |
| `wolfi-baselayout`       | X      |
| `google-cloud-sdk`       | X      |
| `apk-tools`              | X      |
| `busybox`                | X      |

