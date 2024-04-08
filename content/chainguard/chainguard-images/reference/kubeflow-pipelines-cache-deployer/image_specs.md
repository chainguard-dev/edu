---
title: "kubeflow-pipelines-cache-deployer Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public kubeflow-pipelines-cache-deployer Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-03-28 00:50:32
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/kubeflow-pipelines-cache-deployer/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/kubeflow-pipelines-cache-deployer/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/kubeflow-pipelines-cache-deployer/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kubeflow-pipelines-cache-deployer/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **kubeflow-pipelines-cache-deployer** Image.

|              | latest-dev                                              | latest                                                  |
|--------------|---------------------------------------------------------|---------------------------------------------------------|
| Default User | `nonroot`                                               | `nonroot`                                               |
| Entrypoint   | `/bin/bash /kfp/cache/deployer/deploy-cache-service.sh` | `/bin/bash /kfp/cache/deployer/deploy-cache-service.sh` |
| CMD          | not specified                                           | not specified                                           |
| Workdir      | `/kfp/cache/deployer`                                   | `/kfp/cache/deployer`                                   |
| Has apk?     | yes                                                     | no                                                      |
| Has a shell? | yes                                                     | yes                                                     |

Check the [tags history page](/chainguard/chainguard-images/reference/kubeflow-pipelines-cache-deployer/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                            | latest-dev | latest |
|--------------------------------------------|------------|--------|
| `apk-tools`                                | X          |        |
| `bash`                                     | X          | X      |
| `busybox`                                  | X          | X      |
| `ca-certificates-bundle`                   | X          | X      |
| `chainguard-baselayout`                    | X          | X      |
| `git`                                      | X          |        |
| `glibc`                                    | X          | X      |
| `glibc-locale-posix`                       | X          | X      |
| `kubectl-1.29`                             | X          | X      |
| `kubectl-latest`                           | X          | X      |
| `kubeflow-pipelines-cache-deployer`        | X          | X      |
| `kubeflow-pipelines-cache-deployer-compat` | X          | X      |
| `ld-linux`                                 | X          | X      |
| `libbrotlicommon1`                         | X          |        |
| `libbrotlidec1`                            | X          |        |
| `libcrypt1`                                | X          | X      |
| `libcrypto3`                               | X          | X      |
| `libcurl-openssl4`                         | X          |        |
| `libexpat1`                                | X          |        |
| `libidn2`                                  | X          |        |
| `libnghttp2-14`                            | X          |        |
| `libpcre2-8-0`                             | X          |        |
| `libpsl`                                   | X          |        |
| `libssl3`                                  | X          | X      |
| `libunistring`                             | X          |        |
| `libxcrypt`                                | X          | X      |
| `ncurses`                                  | X          | X      |
| `ncurses-terminfo-base`                    | X          | X      |
| `openssl`                                  | X          | X      |
| `openssl-config`                           | X          | X      |
| `openssl-provider-legacy`                  | X          | X      |
| `wget`                                     | X          |        |
| `wolfi-baselayout`                         | X          | X      |
| `zlib`                                     | X          |        |

