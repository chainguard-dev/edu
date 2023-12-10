---
title: "kubeflow-pipelines-metadata-envoy Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public kubeflow-pipelines-metadata-envoy Chainguard Image variants"
date: 2023-12-10 00:31:12
lastmod: 2023-12-10 00:31:12
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/kubeflow-pipelines-metadata-envoy/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/kubeflow-pipelines-metadata-envoy/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/kubeflow-pipelines-metadata-envoy/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kubeflow-pipelines-metadata-envoy/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **kubeflow-pipelines-metadata-envoy** Image.

## Variants Compared
The **kubeflow-pipelines-metadata-envoy** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

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
| `envoy`                                    | X          | X      |
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
| `libnghttp2-14`                            | X          |        |
| `libpcre2-8-0`                             | X          |        |
| `libssl3`                                  | X          | X      |
| `libstdc++`                                | X          | X      |
| `libunistring`                             | X          | X      |
| `libxml2`                                  | X          | X      |
| `ncurses`                                  | X          | X      |
| `ncurses-terminfo-base`                    | X          | X      |
| `openssl`                                  | X          | X      |
| `openssl-config`                           | X          | X      |
| `openssl-provider-legacy`                  | X          | X      |
| `wolfi-baselayout`                         | X          | X      |
| `xz`                                       | X          | X      |
| `zlib`                                     | X          | X      |

