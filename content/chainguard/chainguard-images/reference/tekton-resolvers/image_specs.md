---
title: "tekton-resolvers Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public tekton-resolvers Chainguard Image variants"
date: 2023-12-06 17:47:48
lastmod: 2023-12-06 17:47:48
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/tekton-resolvers/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/tekton-resolvers/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/tekton-resolvers/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/tekton-resolvers/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **tekton-resolvers** Image.

## Variants Compared
The **tekton-resolvers** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev                            | latest                                |
|--------------|---------------------------------------|---------------------------------------|
| Default User | `nonroot`                             | `nonroot`                             |
| Entrypoint   | `/usr/bin/tekton-pipelines-resolvers` | `/usr/bin/tekton-pipelines-resolvers` |
| CMD          | not specified                         | not specified                         |
| Workdir      | not specified                         | not specified                         |
| Has apk?     | yes                                   | no                                    |
| Has a shell? | yes                                   | no                                    |

Check the [tags history page](/chainguard/chainguard-images/reference/tekton-resolvers/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                              | latest-dev | latest |
|------------------------------|------------|--------|
| `apk-tools`                  | X          |        |
| `bash`                       | X          |        |
| `busybox`                    | X          |        |
| `ca-certificates-bundle`     | X          | X      |
| `git`                        | X          |        |
| `glibc`                      | X          |        |
| `glibc-locale-posix`         | X          |        |
| `ld-linux`                   | X          |        |
| `libbrotlicommon1`           | X          |        |
| `libbrotlidec1`              | X          |        |
| `libcrypt1`                  | X          |        |
| `libcrypto3`                 | X          |        |
| `libcurl-openssl4`           | X          |        |
| `libexpat1`                  | X          |        |
| `libnghttp2-14`              | X          |        |
| `libpcre2-8-0`               | X          |        |
| `libssl3`                    | X          |        |
| `ncurses`                    | X          |        |
| `ncurses-terminfo-base`      | X          |        |
| `openssl-config`             | X          |        |
| `tekton-pipelines-resolvers` | X          | X      |
| `wolfi-baselayout`           | X          | X      |
| `zlib`                       | X          |        |

