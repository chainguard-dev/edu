---
title: "secrets-store-csi-driver Image Variants"
type: "article"
description: "Detailed specs for secrets-store-csi-driver Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "secrets-store-csi-driver"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **secrets-store-csi-driver** Image.

## Variants Compared
The **secrets-store-csi-driver** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest                       | latest-dev                   |
|--------------|------------------------------|------------------------------|
| Default User | `root`                       | `root`                       |
| Entrypoint   | `/usr/bin/secrets-store-csi` | `/usr/bin/secrets-store-csi` |
| CMD          | not specified                | not specified                |
| Workdir      | not specified                | not specified                |
| Has apk?     | no                           | yes                          |
| Has a shell? | no                           | yes                          |

## Image Dependencies
The table shows package distribution across all variants.

|                            | latest | latest-dev |
|----------------------------|--------|------------|
| `ca-certificates-bundle`   | X      | X          |
| `wolfi-baselayout`         | X      | X          |
| `secrets-store-csi-driver` | X      | X          |
| `util-linux-misc`          | X      | X          |
| `apk-tools`                |        | X          |
| `bash`                     |        | X          |
| `busybox`                  |        | X          |
| `git`                      |        | X          |

