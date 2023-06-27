---
title: "Curl Image Variants"
type: "article"
description: "Detailed information about the CurlChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Curl"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Curl** Image.

## Variants Compared
The **curl** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest          |
|--------------|-----------------|
| Default User | `curl`          |
| Entrypoint   | `/usr/bin/curl` |
| CMD          | not specified   |
| Workdir      | not specified   |
| Has apk?     | no              |
| Has a shell? | no              |

Check the [tags history page](/chainguard/chainguard-images/reference/curl/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                          | latest |
|--------------------------|--------|
| `curl`                   | X      |
| `libcurl-rustls4`        | X      |
| `ca-certificates-bundle` | X      |
