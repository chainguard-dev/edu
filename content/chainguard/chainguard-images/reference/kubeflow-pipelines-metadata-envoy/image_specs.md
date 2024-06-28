---
title: "kubeflow-pipelines-metadata-envoy Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public kubeflow-pipelines-metadata-envoy Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-06-28 00:31:38
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/kubeflow-pipelines-metadata-envoy/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/kubeflow-pipelines-metadata-envoy/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/kubeflow-pipelines-metadata-envoy/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kubeflow-pipelines-metadata-envoy/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **kubeflow-pipelines-metadata-envoy** Image.

|              | latest-dev                                         | latest                                             |
|--------------|----------------------------------------------------|----------------------------------------------------|
| Default User | `nonroot`                                          | `nonroot`                                          |
| Entrypoint   | `/usr/bin/envoy -c /etc/envoy/metadata-envoy.yaml` | `/usr/bin/envoy -c /etc/envoy/metadata-envoy.yaml` |
| CMD          | not specified                                      | not specified                                      |
| Workdir      | not specified                                      | not specified                                      |
| Has apk?     | yes                                                | no                                                 |
| Has a shell? | yes                                                | no                                                 |

Check the [tags history page](/chainguard/chainguard-images/reference/kubeflow-pipelines-metadata-envoy/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                            | latest-dev | latest |
|--------------------------------------------|------------|--------|
| `apk-tools`                                | X          |        |
| `bash`                                     | X          |        |
| `busybox`                                  | X          |        |
| `ca-certificates-bundle`                   | X          | X      |
| `chainguard-baselayout`                    | X          | X      |
| `envoy-1.30`                               | X          | X      |
| `gettext`                                  | X          | X      |
| `git`                                      | X          |        |
| `glibc`                                    | X          | X      |
| `glibc-iconv`                              | X          | X      |
| `glibc-locale-posix`                       | X          | X      |
| `kubeflow-pipelines-metadata-envoy-config` | X          | X      |
| `ld-linux`                                 | X          | X      |
| `libbrotlicommon1`                         | X          |        |
| `libbrotlidec1`                            | X          |        |
| `libcrypt1`                                | X          |        |
| `libcrypto3`                               | X          | X      |
| `libcurl-openssl4`                         | X          |        |
| `libexpat1`                                | X          |        |
| `libgcc`                                   | X          | X      |
| `libgomp`                                  | X          | X      |
| `libidn2`                                  | X          |        |
| `libnghttp2-14`                            | X          |        |
| `libpcre2-8-0`                             | X          |        |
| `libpsl`                                   | X          |        |
| `libssl3`                                  | X          | X      |
| `libstdc++`                                | X          | X      |
| `libunistring`                             | X          | X      |
| `libxcrypt`                                | X          |        |
| `libxml2`                                  | X          | X      |
| `ncurses`                                  | X          |        |
| `ncurses-terminfo-base`                    | X          |        |
| `openssl`                                  | X          | X      |
| `openssl-provider-legacy`                  | X          | X      |
| `wget`                                     | X          |        |
| `wolfi-baselayout`                         | X          | X      |
| `xz`                                       | X          | X      |
| `zlib`                                     | X          | X      |

