---
title: "mattermost Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public mattermost Chainguard Image."
date: 2024-07-09 00:39:12
lastmod: 2024-07-09 00:39:12
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/mattermost/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/mattermost/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/mattermost/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/mattermost/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **mattermost** Image.

|              | latest-dev       | latest           |
|--------------|------------------|------------------|
| Default User | `mattermost`     | `mattermost`     |
| Entrypoint   | `/entrypoint.sh` | `/entrypoint.sh` |
| CMD          | `mattermost`     | `mattermost`     |
| Workdir      | `/mattermost`    | `/mattermost`    |
| Has apk?     | yes              | no               |
| Has a shell? | yes              | yes              |

Check the [tags history page](/chainguard/chainguard-images/reference/mattermost/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-dev | latest |
|--------------------------|------------|--------|
| `apk-tools`              | X          |        |
| `bash`                   | X          | X      |
| `busybox`                | X          |        |
| `ca-certificates-bundle` | X          | X      |
| `chainguard-baselayout`  | X          | X      |
| `git`                    | X          |        |
| `glibc`                  | X          | X      |
| `glibc-locale-posix`     | X          | X      |
| `ld-linux`               | X          | X      |
| `libbrotlicommon1`       | X          |        |
| `libbrotlidec1`          | X          |        |
| `libcrypt1`              | X          |        |
| `libcrypto3`             | X          |        |
| `libcurl-openssl4`       | X          |        |
| `libexpat1`              | X          |        |
| `libidn2`                | X          |        |
| `libnghttp2-14`          | X          |        |
| `libpcre2-8-0`           | X          |        |
| `libpsl`                 | X          |        |
| `libssl3`                | X          |        |
| `libunistring`           | X          |        |
| `libxcrypt`              | X          |        |
| `mattermost-9`           | X          | X      |
| `mattermost-9-compat`    | X          | X      |
| `ncurses`                | X          | X      |
| `ncurses-terminfo-base`  | X          | X      |
| `tzdata`                 | X          | X      |
| `wget`                   | X          |        |
| `wolfi-baselayout`       | X          | X      |
| `zlib`                   | X          |        |

