---
title: "datadog-cluster-agent Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public datadog-cluster-agent Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-06-07 00:46:50
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/datadog-cluster-agent/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/datadog-cluster-agent/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/datadog-cluster-agent/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/datadog-cluster-agent/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **datadog-cluster-agent** Image.

|              | latest-dev                    | latest                        |
|--------------|-------------------------------|-------------------------------|
| Default User | `nonroot`                     | `nonroot`                     |
| Entrypoint   | `/entrypoint.sh`              | `/entrypoint.sh`              |
| CMD          | `datadog-cluster-agent start` | `datadog-cluster-agent start` |
| Workdir      | not specified                 | not specified                 |
| Has apk?     | yes                           | no                            |
| Has a shell? | yes                           | yes                           |

Check the [tags history page](/chainguard/chainguard-images/reference/datadog-cluster-agent/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                         | latest-dev | latest |
|-----------------------------------------|------------|--------|
| `apk-tools`                             | X          |        |
| `bash`                                  | X          | X      |
| `busybox`                               | X          |        |
| `ca-certificates-bundle`                | X          | X      |
| `chainguard-baselayout`                 | X          | X      |
| `coreutils`                             | X          | X      |
| `datadog-cluster-agent-fips`            | X          | X      |
| `datadog-cluster-agent-oci-compat-fips` | X          | X      |
| `git`                                   | X          |        |
| `glibc`                                 | X          | X      |
| `glibc-locale-posix`                    | X          | X      |
| `ld-linux`                              | X          | X      |
| `libacl1`                               | X          | X      |
| `libattr1`                              | X          | X      |
| `libbrotlicommon1`                      | X          |        |
| `libbrotlidec1`                         | X          |        |
| `libcrypt1`                             | X          |        |
| `libcrypto3`                            | X          | X      |
| `libcurl-openssl4`                      | X          |        |
| `libexpat1`                             | X          |        |
| `libidn2`                               | X          |        |
| `libnghttp2-14`                         | X          |        |
| `libpcre2-8-0`                          | X          |        |
| `libpsl`                                | X          |        |
| `libseccomp`                            | X          | X      |
| `libssl3`                               | X          | X      |
| `libunistring`                          | X          |        |
| `libxcrypt`                             | X          |        |
| `ncurses`                               | X          | X      |
| `ncurses-terminfo-base`                 | X          | X      |
| `openssl-config-fipshardened`           | X          | X      |
| `openssl-provider-fips`                 | X          | X      |
| `tzdata`                                | X          | X      |
| `wget`                                  | X          |        |
| `wolfi-baselayout`                      | X          | X      |
| `zlib`                                  | X          |        |

