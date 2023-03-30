---
title: "prometheus-mysqld-exporter Image Variants"
type: "article"
description: "Detailed specs for prometheus-mysqld-exporter Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "prometheus-mysqld-exporter"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **prometheus-mysqld-exporter** Image.

## Variants Compared
The **prometheus-mysqld-exporter** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest                     |
|--------------|----------------------------|
| Default User | `mysqld_exporter`          |
| Entrypoint   | `/usr/bin/mysqld_exporter` |
| CMD          | not specified              |
| Workdir      | not specified              |
| Has apk?     | yes                        |
| Has a shell? | yes                        |

## Image Dependencies
The table shows package distribution across all variants.

|                              | latest |
|------------------------------|--------|
| `prometheus-mysqld-exporter` | X      |
| `wolfi-base`                 | X      |
| `ca-certificates-bundle`     | X      |
| `busybox`                    | X      |

