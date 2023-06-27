---
title: "Envoy Image Variants"
type: "article"
description: "Detailed information about the EnvoyChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Envoy"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Envoy** Image.

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

Check the [tags history page](/chainguard/chainguard-images/reference/envoy/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                          | latest |
|--------------------------|--------|
| `ca-certificates-bundle` | X      |
| `su-exec`                | X      |
| `envoy`                  | X      |
| `envoy-oci-entrypoint`   | X      |
| `envoy-config`           | X      |
