---
title: "oauth2-proxy Image Variants"
type: "article"
description: "Detailed specs for oauth2-proxy Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "oauth2-proxy"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **oauth2-proxy** Image.

## Variants Compared
The **oauth2-proxy** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest              | latest-dev          |
|--------------|---------------------|---------------------|
| Default User | `oauth2-proxy`      | `oauth2-proxy`      |
| Entrypoint   | `/bin/oauth2-proxy` | `/bin/oauth2-proxy` |
| CMD          | not specified       | not specified       |
| Workdir      | not specified       | not specified       |
| Has apk?     | no                  | yes                 |
| Has a shell? | no                  | yes                 |

## Image Dependencies
The table shows package distribution across all variants.

|                          | latest | latest-dev |
|--------------------------|--------|------------|
| `wolfi-baselayout`       | X      | X          |
| `oauth2-proxy`           | X      | X          |
| `ca-certificates-bundle` | X      | X          |
| `apk-tools`              |        | X          |
| `bash`                   |        | X          |
| `busybox`                |        | X          |
| `git`                    |        | X          |

