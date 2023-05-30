---
title: "prometheus-config-reloader Image Variants"
type: "article"
description: "Detailed specs for prometheus-config-reloader Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "prometheus-config-reloader"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **prometheus-config-reloader** Image.

## Variants Compared
The **prometheus-config-reloader** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest                            | latest-dev                        |
|--------------|-----------------------------------|-----------------------------------|
| Default User | `prometheus-config-reloader`      | `prometheus-config-reloader`      |
| Entrypoint   | `/bin/prometheus-config-reloader` | `/bin/prometheus-config-reloader` |
| CMD          | not specified                     | not specified                     |
| Workdir      | not specified                     | not specified                     |
| Has apk?     | no                                | yes                               |
| Has a shell? | no                                | yes                               |

## Image Dependencies
The table shows package distribution across all variants.

|                                                    | latest | latest-dev |
|----------------------------------------------------|--------|------------|
| `wolfi-baselayout`                                 | X      | X          |
| `prometheus-config-reloader`                       | X      | X          |
| `prometheus-config-reloader-oci-entrypoint-compat` | X      | X          |
| `apk-tools`                                        |        | X          |
| `bash`                                             |        | X          |
| `busybox`                                          |        | X          |
| `git`                                              |        | X          |

