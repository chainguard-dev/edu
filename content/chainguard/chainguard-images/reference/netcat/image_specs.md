---
title: "netcat Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public netcat Chainguard Image variants"
date: 2023-12-06 17:47:48
lastmod: 2023-12-06 17:47:48
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/netcat/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/netcat/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/netcat/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/netcat/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **netcat** Image.

## Variants Compared
The **netcat** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest        |
|--------------|---------------|
| Default User | `nonroot`     |
| Entrypoint   | `/usr/bin/nc` |
| CMD          | `-h`          |
| Workdir      | `/home/nc`    |
| Has apk?     | no            |
| Has a shell? | yes           |

Check the [tags history page](/chainguard/chainguard-images/reference/netcat/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest |
|--------------------------|--------|
| `busybox`                | X      |
| `ca-certificates-bundle` | X      |
| `glibc`                  | X      |
| `glibc-locale-posix`     | X      |
| `ld-linux`               | X      |
| `libbsd`                 | X      |
| `libcrypt1`              | X      |
| `libmd`                  | X      |
| `netcat-openbsd`         | X      |
| `wolfi-baselayout`       | X      |

