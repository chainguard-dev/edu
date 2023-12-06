---
title: "calico-csi Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public calico-csi Chainguard Image variants"
date: 2023-12-06 17:47:48
lastmod: 2023-12-06 17:47:48
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/calico-csi/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/calico-csi/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/calico-csi/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/calico-csi/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **calico-csi** Image.

## Variants Compared
The **calico-csi** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest                                 |
|--------------|----------------------------------------|
| Default User | `root`                                 |
| Entrypoint   | `/usr/bin/calico-pod2daemon-csidriver` |
| CMD          | not specified                          |
| Workdir      | not specified                          |
| Has apk?     | no                                     |
| Has a shell? | no                                     |

Check the [tags history page](/chainguard/chainguard-images/reference/calico-csi/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest |
|--------------------------|--------|
| `ca-certificates-bundle` | X      |
| `calico-pod2daemon`      | X      |
| `glibc`                  | X      |
| `glibc-locale-posix`     | X      |
| `ld-linux`               | X      |
| `wolfi-baselayout`       | X      |

