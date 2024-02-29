---
title: "opensearch Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public opensearch Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-02-29 16:25:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/opensearch/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/opensearch/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/opensearch/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/opensearch/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **opensearch** Image.

|              | latest-dev                                 | latest                                     |
|--------------|--------------------------------------------|--------------------------------------------|
| Default User | `nonroot`                                  | `nonroot`                                  |
| Entrypoint   | `/usr/bin/opensearch-docker-entrypoint.sh` | `/usr/bin/opensearch-docker-entrypoint.sh` |
| CMD          | not specified                              | not specified                              |
| Workdir      | `/usr/share/opensearch`                    | `/usr/share/opensearch`                    |
| Has apk?     | yes                                        | no                                         |
| Has a shell? | yes                                        | yes                                        |

Check the [tags history page](/chainguard/chainguard-images/reference/opensearch/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                          | latest-dev | latest |
|------------------------------------------|------------|--------|
| `apk-tools`                              | X          |        |
| `bash`                                   | X          | X      |
| `busybox`                                | X          | X      |
| `ca-certificates`                        | X          | X      |
| `ca-certificates-bundle`                 | X          | X      |
| `chainguard-baselayout`                  | X          | X      |
| `fontconfig-config`                      | X          | X      |
| `freetype`                               | X          | X      |
| `git`                                    | X          |        |
| `glibc`                                  | X          | X      |
| `glibc-locale-posix`                     | X          | X      |
| `grep`                                   | X          | X      |
| `java-cacerts`                           | X          | X      |
| `java-common`                            | X          | X      |
| `ld-linux`                               | X          | X      |
| `libbrotlicommon1`                       | X          | X      |
| `libbrotlidec1`                          | X          | X      |
| `libbz2-1`                               | X          | X      |
| `libcrypt1`                              | X          | X      |
| `libcrypto3`                             | X          | X      |
| `libcurl-openssl4`                       | X          |        |
| `libexpat1`                              | X          | X      |
| `libffi`                                 | X          | X      |
| `libfontconfig1`                         | X          | X      |
| `libidn2`                                | X          |        |
| `libnghttp2-14`                          | X          |        |
| `libpcre2-8-0`                           | X          | X      |
| `libpng`                                 | X          | X      |
| `libpsl`                                 | X          |        |
| `libssl3`                                | X          | X      |
| `libtasn1`                               | X          | X      |
| `libunistring`                           | X          |        |
| `ncurses`                                | X          | X      |
| `ncurses-terminfo-base`                  | X          | X      |
| `openjdk-17-default-jvm`                 | X          | X      |
| `openjdk-17-jre`                         | X          | X      |
| `openjdk-17-jre-base`                    | X          | X      |
| `opensearch-2`                           | X          | X      |
| `opensearch-2-alerting`                  | X          | X      |
| `opensearch-2-anomaly-detection`         | X          | X      |
| `opensearch-2-asynchronous-search`       | X          | X      |
| `opensearch-2-cross-cluster-replication` | X          | X      |
| `opensearch-2-custom-codecs`             | X          | X      |
| `opensearch-2-geospatial`                | X          | X      |
| `opensearch-2-index-management`          | X          | X      |
| `opensearch-2-job-scheduler`             | X          | X      |
| `opensearch-2-k-nn`                      | X          | X      |
| `opensearch-2-ml-commons`                | X          | X      |
| `opensearch-2-neural-search`             | X          | X      |
| `opensearch-2-notifications`             | X          | X      |
| `opensearch-2-observability`             | X          | X      |
| `opensearch-2-performance-analyzer`      | X          | X      |
| `opensearch-2-reporting`                 | X          | X      |
| `opensearch-2-security`                  | X          | X      |
| `opensearch-2-security-analytics`        | X          | X      |
| `opensearch-2-sql`                       | X          | X      |
| `openssl`                                | X          | X      |
| `openssl-config`                         | X          | X      |
| `openssl-provider-legacy`                | X          | X      |
| `p11-kit`                                | X          | X      |
| `p11-kit-trust`                          | X          | X      |
| `wget`                                   | X          |        |
| `wolfi-baselayout`                       | X          | X      |
| `zlib`                                   | X          | X      |

