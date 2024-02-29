---
title: "netcat Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public netcat Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-02-29 16:25:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/netcat/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/netcat/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/netcat/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/netcat/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **netcat** Image.

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
| `chainguard-baselayout`  | X      |
| `glibc`                  | X      |
| `glibc-locale-posix`     | X      |
| `ld-linux`               | X      |
| `libbsd`                 | X      |
| `libcrypt1`              | X      |
| `libmd`                  | X      |
| `netcat-openbsd`         | X      |
| `wolfi-baselayout`       | X      |

