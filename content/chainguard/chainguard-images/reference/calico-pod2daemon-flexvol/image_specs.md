---
title: "calico-pod2daemon-flexvol Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public calico-pod2daemon-flexvol Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/calico-pod2daemon-flexvol/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/calico-pod2daemon-flexvol/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/calico-pod2daemon-flexvol/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/calico-pod2daemon-flexvol/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **calico-pod2daemon-flexvol** Image.

## Variants Compared
The **calico-pod2daemon-flexvol** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest                |
|--------------|-----------------------|
| Default User | `root`                |
| Entrypoint   | `/usr/bin/flexvol.sh` |
| CMD          | not specified         |
| Workdir      | not specified         |
| Has apk?     | no                    |
| Has a shell? | yes                   |

Check the [tags history page](/chainguard/chainguard-images/reference/calico-pod2daemon-flexvol/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                    | latest |
|------------------------------------|--------|
| `busybox`                          | X      |
| `ca-certificates-bundle`           | X      |
| `calico-pod2daemon`                | X      |
| `calico-pod2daemon-flexvol-compat` | X      |
| `glibc`                            | X      |
| `glibc-locale-posix`               | X      |
| `ld-linux`                         | X      |
| `libcrypt1`                        | X      |
| `wolfi-baselayout`                 | X      |

