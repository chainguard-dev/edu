---
title: "kubeflow-pipelines Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public kubeflow-pipelines Chainguard Image."
date: 2024-02-29 16:25:55
lastmod: 2024-02-29 16:25:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/kubeflow-pipelines/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/kubeflow-pipelines/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/kubeflow-pipelines/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kubeflow-pipelines/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **kubeflow-pipelines** Image.

|              | latest-dev                                                                                    | latest                                                                                        |
|--------------|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| Default User | `nonroot`                                                                                     | `nonroot`                                                                                     |
| Entrypoint   | not specified                                                                                 | not specified                                                                                 |
| CMD          | `/usr/bin/viewer-crd-controller -logtostderr=true -max_num_viewers=50 --namespace="kubeflow"` | `/usr/bin/viewer-crd-controller -logtostderr=true -max_num_viewers=50 --namespace="kubeflow"` |
| Workdir      | not specified                                                                                 | not specified                                                                                 |
| Has apk?     | yes                                                                                           | no                                                                                            |
| Has a shell? | yes                                                                                           | yes                                                                                           |

Check the [tags history page](/chainguard/chainguard-images/reference/kubeflow-pipelines/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                            | latest-dev | latest |
|--------------------------------------------|------------|--------|
| `apk-tools`                                | X          |        |
| `bash`                                     | X          |        |
| `busybox`                                  | X          | X      |
| `ca-certificates-bundle`                   | X          | X      |
| `chainguard-baselayout`                    | X          | X      |
| `git`                                      | X          |        |
| `glibc`                                    | X          | X      |
| `glibc-locale-posix`                       | X          | X      |
| `kubeflow-pipelines-viewer-crd-controller` | X          | X      |
| `ld-linux`                                 | X          | X      |
| `libbrotlicommon1`                         | X          |        |
| `libbrotlidec1`                            | X          |        |
| `libcrypt1`                                | X          | X      |
| `libcrypto3`                               | X          |        |
| `libcurl-openssl4`                         | X          |        |
| `libexpat1`                                | X          |        |
| `libidn2`                                  | X          |        |
| `libnghttp2-14`                            | X          |        |
| `libpcre2-8-0`                             | X          |        |
| `libpsl`                                   | X          |        |
| `libssl3`                                  | X          |        |
| `libunistring`                             | X          |        |
| `ncurses`                                  | X          |        |
| `ncurses-terminfo-base`                    | X          |        |
| `openssl-config`                           | X          |        |
| `wget`                                     | X          |        |
| `wolfi-baselayout`                         | X          | X      |
| `zlib`                                     | X          |        |

