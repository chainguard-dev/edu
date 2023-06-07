---
title: "oidc-discovery-provider Image Variants"
type: "article"
description: "Detailed specs for oidc-discovery-provider Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "oidc-discovery-provider"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **oidc-discovery-provider** Image.

## Variants Compared
The **oidc-discovery-provider** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest                             | latest-dev                         |
|--------------|------------------------------------|------------------------------------|
| Default User | `nonroot`                          | `nonroot`                          |
| Entrypoint   | `/usr/bin/oidc-discovery-provider` | `/usr/bin/oidc-discovery-provider` |
| CMD          | `--help`                           | `--help`                           |
| Workdir      | not specified                      | not specified                      |
| Has apk?     | no                                 | yes                                |
| Has a shell? | no                                 | yes                                |

## Image Dependencies
The table shows package distribution across all variants.

|                                 | latest | latest-dev |
|---------------------------------|--------|------------|
| `wolfi-baselayout`              | X      | X          |
| `ca-certificates-bundle`        | X      | X          |
| `spire-oidc-discovery-provider` | X      | X          |
| `apk-tools`                     |        | X          |
| `bash`                          |        | X          |
| `busybox`                       |        | X          |
| `git`                           |        | X          |

