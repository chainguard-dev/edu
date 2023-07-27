---
title: "Dex Image Variants"
type: "article"
description: "Detailed information about the Dex Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Dex"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Dex** Image.

## Variants Compared
The **dex** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest                                  | latest-dev                              |
|--------------|-----------------------------------------|-----------------------------------------|
| Default User | `nonroot`                               | `nonroot`                               |
| Entrypoint   | `/usr/bin/docker-entrypoint`            | `/usr/bin/docker-entrypoint`            |
| CMD          | `dex serve /etc/dex/config.docker.yaml` | `dex serve /etc/dex/config.docker.yaml` |
| Workdir      | not specified                           | not specified                           |
| Has apk?     | no                                      | yes                                     |
| Has a shell? | no                                      | yes                                     |

Check the [tags history page](/chainguard/chainguard-images/reference/dex/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|            | latest | latest-dev |
|------------|--------|------------|
| `dex`      | X      | X          |
| `gomplate` | X      | X          |
