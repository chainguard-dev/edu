---
title: "kubeflow-pipelines-viewer-crd-controller Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public kubeflow-pipelines-viewer-crd-controller Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-07-05 00:42:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/kubeflow-pipelines-viewer-crd-controller/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/kubeflow-pipelines-viewer-crd-controller/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/kubeflow-pipelines-viewer-crd-controller/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kubeflow-pipelines-viewer-crd-controller/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **kubeflow-pipelines-viewer-crd-controller** Image.

|              | latest-dev                                                                                    | latest                                                                                        |
|--------------|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| Default User | `nonroot`                                                                                     | `nonroot`                                                                                     |
| Entrypoint   | not specified                                                                                 | not specified                                                                                 |
| CMD          | `/usr/bin/viewer-crd-controller -logtostderr=true -max_num_viewers=50 --namespace="kubeflow"` | `/usr/bin/viewer-crd-controller -logtostderr=true -max_num_viewers=50 --namespace="kubeflow"` |
| Workdir      | not specified                                                                                 | not specified                                                                                 |
| Has apk?     | yes                                                                                           | no                                                                                            |
| Has a shell? | yes                                                                                           | yes                                                                                           |

Check the [tags history page](/chainguard/chainguard-images/reference/kubeflow-pipelines-viewer-crd-controller/tags_history/) for the full list of available tags.

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
| `libxcrypt`                                | X          | X      |
| `ncurses`                                  | X          |        |
| `ncurses-terminfo-base`                    | X          |        |
| `wget`                                     | X          |        |
| `wolfi-baselayout`                         | X          | X      |
| `zlib`                                     | X          |        |

