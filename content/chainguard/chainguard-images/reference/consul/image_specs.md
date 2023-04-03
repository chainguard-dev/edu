---
title: "consul Image Variants"
type: "article"
description: "Detailed specs for consul Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "consul"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **consul** Image.

## Variants Compared
The **consul** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest                          | latest-dev                      |
|--------------|---------------------------------|---------------------------------|
| Default User | `root`                          | `root`                          |
| Entrypoint   | `/usr/bin/docker-entrypoint.sh` | `/usr/bin/docker-entrypoint.sh` |
| CMD          | `agent -dev -client 0.0.0.0`    | `agent -dev -client 0.0.0.0`    |
| Workdir      | not specified                   | not specified                   |
| Has apk?     | no                              | yes                             |
| Has a shell? | yes                             | yes                             |

## Image Dependencies
The table shows package distribution across all variants.

|                          | latest | latest-dev |
|--------------------------|--------|------------|
| `ca-certificates-bundle` | X      | X          |
| `wolfi-baselayout`       | X      | X          |
| `consul`                 | X      | X          |
| `su-exec`                | X      | X          |
| `consul-oci-entrypoint`  | X      | X          |
| `busybox`                | X      | X          |
| `apk-tools`              |        | X          |
| `bash`                   |        | X          |
| `git`                    |        | X          |

