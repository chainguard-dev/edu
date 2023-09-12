---
title: "calico-pod2daemon Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public calico-pod2daemon Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/calico-pod2daemon/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/calico-pod2daemon/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/calico-pod2daemon/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/calico-pod2daemon/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **calico-pod2daemon** Image.

## Variants Compared
The **calico-pod2daemon** Chainguard Image currently has 2 public variants: 

- `flexvol-latest`
- `latest`

The table has detailed information about each of these variants.

|              | flexvol-latest        | latest                |
|--------------|-----------------------|-----------------------|
| Default User | `0`                   | `0`                   |
| Entrypoint   | `/usr/bin/flexvol.sh` | `/usr/bin/flexvol.sh` |
| CMD          | not specified         | not specified         |
| Workdir      | not specified         | not specified         |
| Has apk?     | no                    | no                    |
| Has a shell? | yes                   | yes                   |

Check the [tags history page](/chainguard/chainguard-images/reference/calico-pod2daemon/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                    | flexvol-latest | latest |
|------------------------------------|----------------|--------|
| `busybox`                          | X              | X      |
| `ca-certificates-bundle`           | X              | X      |
| `calico-pod2daemon`                | X              | X      |
| `calico-pod2daemon-flexvol-compat` | X              |        |
| `glibc`                            | X              | X      |
| `glibc-locale-posix`               | X              | X      |
| `ld-linux`                         | X              | X      |
| `libcrypt1`                        | X              | X      |
| `wolfi-baselayout`                 | X              | X      |

