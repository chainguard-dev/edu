---
title: "calico-typha Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public calico-typha Chainguard Image variants"
date: 2023-12-06 17:47:48
lastmod: 2023-12-06 17:47:48
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/calico-typha/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/calico-typha/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/calico-typha/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/calico-typha/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **calico-typha** Image.

## Variants Compared
The **calico-typha** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest                  |
|--------------|-------------------------|
| Default User | `nonroot`               |
| Entrypoint   | `/sbin/tini --`         |
| CMD          | `/usr/bin/calico-typha` |
| Workdir      | not specified           |
| Has apk?     | no                      |
| Has a shell? | no                      |

Check the [tags history page](/chainguard/chainguard-images/reference/calico-typha/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest |
|--------------------------|--------|
| `ca-certificates-bundle` | X      |
| `calico-typhad`          | X      |
| `glibc`                  | X      |
| `glibc-locale-posix`     | X      |
| `ld-linux`               | X      |
| `tini`                   | X      |
| `wolfi-baselayout`       | X      |

