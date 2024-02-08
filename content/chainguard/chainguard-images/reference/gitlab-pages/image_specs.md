---
title: "gitlab-pages Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public gitlab-pages Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-02-08 00:18:32
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/gitlab-pages/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/gitlab-pages/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/gitlab-pages/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/gitlab-pages/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **gitlab-pages** Image.

## Variants Compared
The **gitlab-pages** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev                                    | latest                                        |
|--------------|-----------------------------------------------|-----------------------------------------------|
| Default User | `nonroot`                                     | `nonroot`                                     |
| Entrypoint   | `/scripts/entrypoint.sh /scripts/start-pages` | `/scripts/entrypoint.sh /scripts/start-pages` |
| CMD          | not specified                                 | not specified                                 |
| Workdir      | not specified                                 | not specified                                 |
| Has apk?     | yes                                           | no                                            |
| Has a shell? | yes                                           | yes                                           |

Check the [tags history page](/chainguard/chainguard-images/reference/gitlab-pages/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                            | latest-dev | latest |
|----------------------------|------------|--------|
| `apk-tools`                | X          |        |
| `bash`                     | X          | X      |
| `busybox`                  | X          | X      |
| `ca-certificates-bundle`   | X          | X      |
| `curl`                     | X          | X      |
| `git`                      | X          |        |
| `gitlab-cng-base`          | X          | X      |
| `gitlab-cng-pages-scripts` | X          | X      |
| `gitlab-logger`            | X          | X      |
| `gitlab-pages`             | X          | X      |
| `glibc`                    | X          | X      |
| `glibc-locale-posix`       | X          | X      |
| `gomplate`                 | X          | X      |
| `ld-linux`                 | X          | X      |
| `libbrotlicommon1`         | X          | X      |
| `libbrotlidec1`            | X          | X      |
| `libcrypt1`                | X          | X      |
| `libcrypto3`               | X          | X      |
| `libcurl-openssl4`         | X          | X      |
| `libexpat1`                | X          |        |
| `libidn2`                  | X          | X      |
| `libnghttp2-14`            | X          | X      |
| `libpcre2-8-0`             | X          |        |
| `libproc-2-0`              | X          | X      |
| `libpsl`                   | X          | X      |
| `libssl3`                  | X          | X      |
| `libunistring`             | X          | X      |
| `ncurses`                  | X          | X      |
| `ncurses-terminfo-base`    | X          | X      |
| `openssl-config`           | X          | X      |
| `procps`                   | X          | X      |
| `wget`                     | X          |        |
| `wolfi-baselayout`         | X          | X      |
| `xtail`                    | X          | X      |
| `zlib`                     | X          | X      |

