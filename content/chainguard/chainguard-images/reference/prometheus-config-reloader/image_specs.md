---
title: "Prometheus-config-reloader Image Variants"
type: "article"
description: "Detailed information about the Prometheus-config-reloaderChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Prometheus-config-reloader"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Prometheus-config-reloader** Image.

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
| Has apk?     | no                                | no                                |
| Has a shell? | no                                | no                                |

Check the [tags history page](/chainguard/chainguard-images/reference/prometheus-config-reloader/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                                                    | latest | latest-dev |
|----------------------------------------------------|--------|------------|
| `wolfi-baselayout`                                 | X      | X          |
| `prometheus-config-reloader`                       | X      | X          |
| `prometheus-config-reloader-oci-entrypoint-compat` | X      | X          |
