---
title: "buildkit Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public buildkit Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-03-28 00:50:32
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/buildkit/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/buildkit/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/buildkit/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/buildkit/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **buildkit** Image.

|              | latest-dev           | latest-root-dev      | latest-root          | latest               |
|--------------|----------------------|----------------------|----------------------|----------------------|
| Default User | `root`               | `root`               | `root`               | `root`               |
| Entrypoint   | `/usr/bin/buildkitd` | `/usr/bin/buildkitd` | `/usr/bin/buildkitd` | `/usr/bin/buildkitd` |
| CMD          | not specified        | not specified        | not specified        | not specified        |
| Workdir      | not specified        | not specified        | not specified        | not specified        |
| Has apk?     | yes                  | yes                  | no                   | no                   |
| Has a shell? | yes                  | yes                  | no                   | no                   |

Check the [tags history page](/chainguard/chainguard-images/reference/buildkit/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-dev | latest-root-dev | latest-root | latest |
|--------------------------|------------|-----------------|-------------|--------|
| `apk-tools`              | X          | X               |             |        |
| `bash`                   | X          | X               |             |        |
| `buildctl`               | X          | X               | X           | X      |
| `buildkitd`              | X          | X               | X           | X      |
| `busybox`                | X          | X               |             |        |
| `ca-certificates-bundle` | X          | X               | X           | X      |
| `chainguard-baselayout`  | X          | X               | X           | X      |
| `git`                    | X          | X               |             |        |
| `glibc`                  | X          | X               | X           | X      |
| `glibc-locale-posix`     | X          | X               | X           | X      |
| `ld-linux`               | X          | X               | X           | X      |
| `libbrotlicommon1`       | X          | X               |             |        |
| `libbrotlidec1`          | X          | X               |             |        |
| `libcrypt1`              | X          | X               |             |        |
| `libcrypto3`             | X          | X               |             |        |
| `libcurl-openssl4`       | X          | X               |             |        |
| `libexpat1`              | X          | X               |             |        |
| `libidn2`                | X          | X               |             |        |
| `libnghttp2-14`          | X          | X               |             |        |
| `libpcre2-8-0`           | X          | X               |             |        |
| `libpsl`                 | X          | X               |             |        |
| `libseccomp`             | X          | X               | X           | X      |
| `libssl3`                | X          | X               |             |        |
| `libunistring`           | X          | X               |             |        |
| `libxcrypt`              | X          |                 |             |        |
| `ncurses`                | X          | X               |             |        |
| `ncurses-terminfo-base`  | X          | X               |             |        |
| `openssl-config`         | X          | X               |             |        |
| `runc`                   | X          | X               | X           | X      |
| `wget`                   | X          | X               |             |        |
| `wolfi-baselayout`       | X          | X               | X           | X      |
| `zlib`                   | X          | X               |             |        |

