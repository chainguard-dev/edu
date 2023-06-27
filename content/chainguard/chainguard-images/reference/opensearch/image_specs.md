---
title: "Opensearch Image Variants"
type: "article"
description: "Detailed information about the OpensearchChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Opensearch"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Opensearch** Image.

## Variants Compared
The **opensearch** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest                          | latest-dev                      |
|--------------|---------------------------------|---------------------------------|
| Default User | `opensearch`                    | `opensearch`                    |
| Entrypoint   | `/usr/bin/docker-entrypoint.sh` | `/usr/bin/docker-entrypoint.sh` |
| CMD          | `opensearchwrapper`             | `opensearchwrapper`             |
| Workdir      | not specified                   | not specified                   |
| Has apk?     | no                              | no                              |
| Has a shell? | yes                             | yes                             |

Check the [tags history page](/chainguard/chainguard-images/reference/opensearch/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                          | latest | latest-dev |
|--------------------------|--------|------------|
| `ca-certificates-bundle` | X      | X          |
| `wolfi-baselayout`       | X      | X          |
| `busybox`                | X      | X          |
| `opensearch-2`           | X      | X          |
| `openjdk-11-default-jvm` | X      | X          |
