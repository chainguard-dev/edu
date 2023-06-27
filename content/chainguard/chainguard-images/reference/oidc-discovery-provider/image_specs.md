---
title: "Oidc-discovery-provider Image Variants"
type: "article"
description: "Detailed information about the Oidc-discovery-providerChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Oidc-discovery-provider"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Oidc-discovery-provider** Image.

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
| Has apk?     | no                                 | no                                 |
| Has a shell? | no                                 | no                                 |

Check the [tags history page](/chainguard/chainguard-images/reference/oidc-discovery-provider/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                                 | latest | latest-dev |
|---------------------------------|--------|------------|
| `wolfi-baselayout`              | X      | X          |
| `ca-certificates-bundle`        | X      | X          |
| `spire-oidc-discovery-provider` | X      | X          |
