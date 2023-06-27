---
title: "Wavefront-proxy Image Variants"
type: "article"
description: "Detailed information about the Wavefront-proxyChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Wavefront-proxy"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Wavefront-proxy** Image.

## Variants Compared
The **wavefront-proxy** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest                  | latest-dev              |
|--------------|-------------------------|-------------------------|
| Default User | `wavefront`             | `wavefront`             |
| Entrypoint   | `/usr/local/bin/run.sh` | `/usr/local/bin/run.sh` |
| CMD          | not specified           | not specified           |
| Workdir      | not specified           | not specified           |
| Has apk?     | no                      | no                      |
| Has a shell? | yes                     | yes                     |

Check the [tags history page](/chainguard/chainguard-images/reference/wavefront-proxy/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                                  | latest | latest-dev |
|----------------------------------|--------|------------|
| `wolfi-baselayout`               | X      | X          |
| `ca-certificates-bundle`         | X      | X          |
| `openjdk-11-jre`                 | X      | X          |
| `openjdk-11-default-jvm`         | X      | X          |
| `wavefront-proxy`                | X      | X          |
| `wavefront-proxy-config`         | X      | X          |
| `wavefront-proxy-licenses`       | X      | X          |
| `wavefront-proxy-oci-entrypoint` | X      | X          |
| `bash`                           | X      | X          |
| `busybox`                        | X      | X          |
