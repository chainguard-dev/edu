---
title: "prometheus-alertmanager Image Variants"
type: "article"
description: "Detailed specs for prometheus-alertmanager Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "prometheus-alertmanager"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **prometheus-alertmanager** Image.

## Variants Compared
The **prometheus-alertmanager** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest                                                                          |
|--------------|---------------------------------------------------------------------------------|
| Default User | `alertmanager`                                                                  |
| Entrypoint   | `/usr/bin/alertmanager`                                                         |
| CMD          | `--config.file=/etc/alertmanager/alertmanager.yml --storage.path=/alertmanager` |
| Workdir      | not specified                                                                   |
| Has apk?     | yes                                                                             |
| Has a shell? | yes                                                                             |

## Image Dependencies
The table shows package distribution across all variants.

|                           | latest |
|---------------------------|--------|
| `prometheus-alertmanager` | X      |
| `wolfi-base`              | X      |
| `ca-certificates-bundle`  | X      |
| `busybox`                 | X      |

