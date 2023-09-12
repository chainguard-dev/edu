---
title: "tekton-workingdirinit Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public tekton-workingdirinit Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/tekton-workingdirinit/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/tekton-workingdirinit/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/tekton-workingdirinit/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/tekton-workingdirinit/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **tekton-workingdirinit** Image.

## Variants Compared
The **tekton-workingdirinit** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev                                 | latest                                     |
|--------------|--------------------------------------------|--------------------------------------------|
| Default User | `65532`                                    | `65532`                                    |
| Entrypoint   | `/usr/bin/tekton-pipelines-workingdirinit` | `/usr/bin/tekton-pipelines-workingdirinit` |
| CMD          | not specified                              | not specified                              |
| Workdir      | not specified                              | not specified                              |
| Has apk?     | yes                                        | no                                         |
| Has a shell? | yes                                        | no                                         |

Check the [tags history page](/chainguard/chainguard-images/reference/tekton-workingdirinit/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                   | latest-dev | latest |
|-----------------------------------|------------|--------|
| `apk-tools`                       | X          |        |
| `bash`                            | X          |        |
| `busybox`                         | X          |        |
| `ca-certificates-bundle`          | X          | X      |
| `git`                             | X          |        |
| `glibc`                           | X          |        |
| `glibc-locale-posix`              | X          |        |
| `ld-linux`                        | X          |        |
| `libbrotlicommon1`                | X          |        |
| `libbrotlidec1`                   | X          |        |
| `libcrypt1`                       | X          |        |
| `libcrypto3`                      | X          |        |
| `libcurl-openssl4`                | X          |        |
| `libexpat1`                       | X          |        |
| `libnghttp2-14`                   | X          |        |
| `libpcre2-8-0`                    | X          |        |
| `libssl3`                         | X          |        |
| `ncurses`                         | X          |        |
| `ncurses-terminfo-base`           | X          |        |
| `openssl-config`                  | X          |        |
| `tekton-pipelines-workingdirinit` | X          | X      |
| `wolfi-baselayout`                | X          | X      |
| `zlib`                            | X          |        |

