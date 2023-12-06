---
title: "kubeflow-pipelines-frontend Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public kubeflow-pipelines-frontend Chainguard Image variants"
date: 2023-12-06 17:47:48
lastmod: 2023-12-06 17:47:48
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/kubeflow-pipelines-frontend/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/kubeflow-pipelines-frontend/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/kubeflow-pipelines-frontend/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kubeflow-pipelines-frontend/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **kubeflow-pipelines-frontend** Image.

## Variants Compared
The **kubeflow-pipelines-frontend** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev                                   | latest                                       |
|--------------|----------------------------------------------|----------------------------------------------|
| Default User | `nonroot`                                    | `nonroot`                                    |
| Entrypoint   | not specified                                | not specified                                |
| CMD          | `node ./server/dist/server.js ./client 3000` | `node ./server/dist/server.js ./client 3000` |
| Workdir      | not specified                                | not specified                                |
| Has apk?     | yes                                          | no                                           |
| Has a shell? | yes                                          | no                                           |

Check the [tags history page](/chainguard/chainguard-images/reference/kubeflow-pipelines-frontend/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                               | latest-dev | latest |
|-------------------------------|------------|--------|
| `apk-tools`                   | X          |        |
| `bash`                        | X          |        |
| `busybox`                     | X          |        |
| `c-ares`                      | X          | X      |
| `ca-certificates-bundle`      | X          | X      |
| `git`                         | X          |        |
| `glibc`                       | X          | X      |
| `glibc-locale-posix`          | X          | X      |
| `icu`                         | X          | X      |
| `kubeflow-pipelines-frontend` | X          | X      |
| `ld-linux`                    | X          | X      |
| `libbrotlicommon1`            | X          | X      |
| `libbrotlidec1`               | X          | X      |
| `libbrotlienc1`               | X          | X      |
| `libcrypt1`                   | X          |        |
| `libcrypto3`                  | X          | X      |
| `libcurl-openssl4`            | X          |        |
| `libexpat1`                   | X          |        |
| `libgcc`                      | X          | X      |
| `libnghttp2-14`               | X          | X      |
| `libpcre2-8-0`                | X          |        |
| `libssl3`                     | X          | X      |
| `libstdc++`                   | X          | X      |
| `ncurses`                     | X          |        |
| `ncurses-terminfo-base`       | X          |        |
| `nodejs-20`                   | X          | X      |
| `npm`                         | X          | X      |
| `openssl-config`              | X          | X      |
| `wget`                        | X          | X      |
| `wolfi-baselayout`            | X          | X      |
| `zlib`                        | X          | X      |

