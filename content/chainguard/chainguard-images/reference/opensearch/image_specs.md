---
title: "Opensearch Image Variants"
type: "article"
description: "Detailed information about the Opensearch Chainguard Image variants"
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

## Default Image Settings
`USER`:		`opensearch`

`WORKDIR`:	not specified

`ENTRYPOINT`:	`/usr/bin/docker-entrypoint.sh`

`CMD`:		`opensearchwrapper`

The following table has additional information about each of these variants.

|              | latest | latest-dev |
|--------------|--------|------------|
| Has apk?     | no     | yes        |
| Has a shell? | yes    | yes        |

Check the [tags history page](/chainguard/chainguard-images/reference/opensearch/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                          | latest | latest-dev |
|--------------------------|--------|------------|
| `busybox`                | X      | X          |
| `opensearch-2`           | X      | X          |
| `openjdk-11-default-jvm` | X      | X          |
