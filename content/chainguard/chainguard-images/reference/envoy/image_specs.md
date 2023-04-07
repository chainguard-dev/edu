---
title: "envoy Image Variants"
type: "article"
description: "Detailed specs for envoy Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "envoy"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **envoy** Image.

## Variants Compared
The **envoy** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest                                    |
|--------------|-------------------------------------------|
| Default User | `envoy`                                   |
| Entrypoint   | `/var/lib/envoy/init/envoy-entrypoint.sh` |
| CMD          | not specified                             |
| Workdir      | not specified                             |
| Has apk?     | no                                        |
| Has a shell? | no                                        |

## Image Dependencies
The table shows package distribution across all variants.

|                          | latest |
|--------------------------|--------|
| `ca-certificates-bundle` | X      |
| `su-exec`                | X      |
| `envoy`                  | X      |
| `envoy-oci-entrypoint`   | X      |
| `envoy-config`           | X      |
| `wolfi-baselayout`       | X      |

