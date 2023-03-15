---
title: "prometheus-node-exporter Image Variants"
type: "article"
description: "Detailed specs for prometheus-node-exporter Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
images: []
menu:
  docs:
    parent: "prometheus-node-exporter"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **prometheus-node-exporter** Image.

## Variants Compared
The **prometheus-node-exporter** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest                   |
|--------------|--------------------------|
| Default User | `node_exporter`          |
| Entrypoint   | `/usr/bin/node_exporter` |
| CMD          | not specified            |
| Workdir      | not specified            |
| Has apk?     | no                       |
| Has a shell? | yes                      |

## Image Dependencies
The table shows package distribution across all variants.

|                            | latest |
|----------------------------|--------|
| `prometheus-node-exporter` | X      |
| `wolfi-baselayout`         | X      |
| `busybox`                  | X      |
