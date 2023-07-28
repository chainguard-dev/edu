---
title: "Minio Image Variants"
type: "article"
description: "Detailed information about the Minio Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Minio"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Minio** Image.

## Variants Compared
The **minio** Chainguard Image currently has 4 public variants: 

- `latest.minio`
- `latest.minio-dev`
- `latest.minio-client`
- `latest.minio-client-dev`

## Default Image Settings
`USER`:		`minio`

`WORKDIR`:	not specified

`ENTRYPOINT`:	`/usr/bin/mc`

`CMD`:		not specified

The following table has additional information about each of these variants.

|              | latest.minio | latest.minio-dev | latest.minio-client | latest.minio-client-dev |
|--------------|--------------|------------------|---------------------|-------------------------|
| Has apk?     | no           | yes              | no                  | yes                     |
| Has a shell? | no           | yes              | yes                 | yes                     |

Check the [tags history page](/chainguard/chainguard-images/reference/minio/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|         | latest.minio | latest.minio-dev | latest.minio-client | latest.minio-client-dev |
|---------|--------------|------------------|---------------------|-------------------------|
| `minio` | X            | X                |                     |                         |
| `mc`    |              |                  | X                   | X                       |
| `bash`  |              |                  | X                   | X                       |
