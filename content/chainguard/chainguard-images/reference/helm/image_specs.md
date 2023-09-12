---
title: "helm Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public helm Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/helm/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/helm/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/helm/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/helm/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **helm** Image.

## Variants Compared
The **helm** Chainguard Image currently has 6 public variants: 

- `chartmuseum-latest-dev`
- `chartmuseum-latest`
- `controller-latest-dev`
- `controller-latest`
- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | chartmuseum-latest-dev | chartmuseum-latest     | controller-latest-dev      | controller-latest          | latest-dev      | latest          |
|--------------|------------------------|------------------------|----------------------------|----------------------------|-----------------|-----------------|
| Default User | `65532`                | `65532`                | `65532`                    | `65532`                    | `65532`         | `65532`         |
| Entrypoint   | `/usr/bin/chartmuseum` | `/usr/bin/chartmuseum` | `/usr/bin/helm-controller` | `/usr/bin/helm-controller` | `/usr/bin/helm` | `/usr/bin/helm` |
| CMD          | not specified          | not specified          | not specified              | not specified              | `help`          | `help`          |
| Workdir      | not specified          | not specified          | not specified              | not specified              | not specified   | not specified   |
| Has apk?     | yes                    | no                     | yes                        | no                         | yes             | no              |
| Has a shell? | yes                    | no                     | yes                        | no                         | yes             | no              |

Check the [tags history page](/chainguard/chainguard-images/reference/helm/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | chartmuseum-latest-dev | chartmuseum-latest | controller-latest-dev | controller-latest | latest-dev | latest |
|--------------------------|------------------------|--------------------|-----------------------|-------------------|------------|--------|
| `apk-tools`              | X                      |                    | X                     |                   | X          |        |
| `bash`                   | X                      |                    | X                     |                   | X          |        |
| `busybox`                | X                      |                    | X                     |                   | X          |        |
| `ca-certificates-bundle` | X                      | X                  | X                     | X                 | X          | X      |
| `chartmuseum`            | X                      | X                  |                       |                   |            |        |
| `git`                    | X                      |                    | X                     |                   | X          |        |
| `glibc`                  | X                      |                    | X                     |                   | X          |        |
| `glibc-locale-posix`     | X                      |                    | X                     | X                 | X          |        |
| `ld-linux`               | X                      |                    | X                     |                   | X          |        |
| `libbrotlicommon1`       | X                      |                    | X                     |                   | X          |        |
| `libbrotlidec1`          | X                      |                    | X                     |                   | X          |        |
| `libcrypt1`              | X                      |                    |                       |                   | X          |        |
| `libcrypto3`             | X                      |                    | X                     |                   | X          |        |
| `libcurl-openssl4`       | X                      |                    | X                     |                   | X          |        |
| `libexpat1`              | X                      |                    |                       |                   | X          |        |
| `libnghttp2-14`          | X                      |                    | X                     |                   | X          |        |
| `libpcre2-8-0`           | X                      |                    | X                     |                   | X          |        |
| `libssl3`                | X                      |                    | X                     |                   | X          |        |
| `ncurses`                | X                      |                    | X                     |                   | X          |        |
| `ncurses-terminfo-base`  | X                      |                    | X                     |                   | X          |        |
| `openssl-config`         | X                      |                    | X                     |                   | X          |        |
| `wolfi-baselayout`       | X                      | X                  | X                     | X                 | X          | X      |
| `zlib`                   | X                      |                    | X                     |                   | X          |        |
| `expat`                  |                        |                    | X                     |                   |            |        |
| `flux-helm-controller`   |                        |                    | X                     | X                 |            |        |
| `helm`                   |                        |                    |                       |                   | X          | X      |
| `kubectl-1.28`           |                        |                    |                       |                   | X          | X      |
| `kubectl-latest`         |                        |                    |                       |                   | X          | X      |

