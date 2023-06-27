---
title: "Kyvernopre Image Variants"
type: "article"
description: "Detailed information about the KyvernopreChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Kyvernopre"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Kyvernopre** Image.

## Variants Compared
The **kyvernopre** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest                |
|--------------|-----------------------|
| Default User | `nonroot`             |
| Entrypoint   | `/usr/bin/kyvernopre` |
| CMD          | `help`                |
| Workdir      | not specified         |
| Has apk?     | no                    |
| Has a shell? | no                    |

Check the [tags history page](/chainguard/chainguard-images/reference/kyvernopre/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                          | latest |
|--------------------------|--------|
| `ca-certificates-bundle` | X      |
| `kyverno-init-container` | X      |
| `wolfi-baselayout`       | X      |
| `kubectl`                | X      |
