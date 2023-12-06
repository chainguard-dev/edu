---
title: "buildkit Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public buildkit Chainguard Image variants"
date: 2023-12-06 18:44:36
lastmod: 2023-12-06 18:44:36
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/buildkit/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/buildkit/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/buildkit/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/buildkit/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **buildkit** Image.

## Variants Compared
The **buildkit** Chainguard Image currently has 2 public variants: 

- `latest-root-dev`
- `latest-root`

The table has detailed information about each of these variants.

|              | latest-root-dev      | latest-root          |
|--------------|----------------------|----------------------|
| Default User | `root`               | `root`               |
| Entrypoint   | `/usr/bin/buildkitd` | `/usr/bin/buildkitd` |
| CMD          | not specified        | not specified        |
| Workdir      | not specified        | not specified        |
| Has apk?     | yes                  | no                   |
| Has a shell? | yes                  | no                   |

Check the [tags history page](/chainguard/chainguard-images/reference/buildkit/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-root-dev | latest-root |
|--------------------------|-----------------|-------------|
| `apk-tools`              | X               |             |
| `bash`                   | X               |             |
| `buildctl`               | X               | X           |
| `buildkitd`              | X               | X           |
| `busybox`                | X               |             |
| `ca-certificates-bundle` | X               | X           |
| `git`                    | X               |             |
| `glibc`                  | X               | X           |
| `glibc-locale-posix`     | X               | X           |
| `ld-linux`               | X               | X           |
| `libbrotlicommon1`       | X               |             |
| `libbrotlidec1`          | X               |             |
| `libcrypt1`              | X               |             |
| `libcrypto3`             | X               |             |
| `libcurl-openssl4`       | X               |             |
| `libexpat1`              | X               |             |
| `libnghttp2-14`          | X               |             |
| `libpcre2-8-0`           | X               |             |
| `libseccomp`             | X               | X           |
| `libssl3`                | X               |             |
| `ncurses`                | X               |             |
| `ncurses-terminfo-base`  | X               |             |
| `openssl-config`         | X               |             |
| `runc`                   | X               | X           |
| `wolfi-baselayout`       | X               | X           |
| `zlib`                   | X               |             |

