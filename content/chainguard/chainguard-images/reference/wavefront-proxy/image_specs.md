---
title: "wavefront-proxy Image Variants"
type: "article"
description: "Detailed specs for wavefront-proxy Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "wavefront-proxy"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **wavefront-proxy** Image.

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
| Has apk?     | no                      | yes                     |
| Has a shell? | yes                     | yes                     |

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
| `apk-tools`                      |        | X          |
| `git`                            |        | X          |

