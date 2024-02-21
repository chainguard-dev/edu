---
title: "opensearch-dashboards Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public opensearch-dashboards Chainguard Image variants"
date: 2024-02-21 00:39:53
lastmod: 2024-02-21 00:39:53
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/opensearch-dashboards/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/opensearch-dashboards/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/opensearch-dashboards/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/opensearch-dashboards/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **opensearch-dashboards** Image.

## Variants Compared
The **opensearch-dashboards** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev                                                                    | latest                                                                        |
|--------------|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| Default User | `nonroot`                                                                     | `nonroot`                                                                     |
| Entrypoint   | `/usr/bin/dumb-init --`                                                       | `/usr/bin/dumb-init --`                                                       |
| CMD          | `/usr/share/opensearch-dashboards/opensearch-dashboards-docker-entrypoint.sh` | `/usr/share/opensearch-dashboards/opensearch-dashboards-docker-entrypoint.sh` |
| Workdir      | `/usr/share/opensearch-dashboards`                                            | `/usr/share/opensearch-dashboards`                                            |
| Has apk?     | yes                                                                           | no                                                                            |
| Has a shell? | yes                                                                           | yes                                                                           |

Check the [tags history page](/chainguard/chainguard-images/reference/opensearch-dashboards/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                                                | latest-dev | latest |
|----------------------------------------------------------------|------------|--------|
| `apk-tools`                                                    | X          |        |
| `bash`                                                         | X          | X      |
| `busybox`                                                      | X          | X      |
| `c-ares`                                                       | X          | X      |
| `ca-certificates-bundle`                                       | X          | X      |
| `dumb-init`                                                    | X          | X      |
| `font-misc`                                                    | X          | X      |
| `font-misc-cyrillic`                                           | X          | X      |
| `fontconfig`                                                   | X          | X      |
| `fontconfig-config`                                            | X          | X      |
| `freetype`                                                     | X          | X      |
| `git`                                                          | X          |        |
| `glibc`                                                        | X          | X      |
| `glibc-locale-posix`                                           | X          | X      |
| `icu`                                                          | X          | X      |
| `ld-linux`                                                     | X          | X      |
| `libbrotlicommon1`                                             | X          | X      |
| `libbrotlidec1`                                                | X          | X      |
| `libbrotlienc1`                                                | X          | X      |
| `libbz2-1`                                                     | X          | X      |
| `libcrypt1`                                                    | X          | X      |
| `libcrypto3`                                                   | X          | X      |
| `libcurl-openssl4`                                             | X          |        |
| `libexpat1`                                                    | X          | X      |
| `libfontconfig1`                                               | X          | X      |
| `libfontenc`                                                   | X          | X      |
| `libgcc`                                                       | X          | X      |
| `libidn2`                                                      | X          |        |
| `libnghttp2-14`                                                | X          | X      |
| `libpcre2-8-0`                                                 | X          |        |
| `libpng`                                                       | X          | X      |
| `libpsl`                                                       | X          |        |
| `libssl3`                                                      | X          | X      |
| `libstdc++`                                                    | X          | X      |
| `libunistring`                                                 | X          |        |
| `libuv`                                                        | X          | X      |
| `libxfont`                                                     | X          | X      |
| `ncurses`                                                      | X          | X      |
| `ncurses-terminfo-base`                                        | X          | X      |
| `nodejs-18`                                                    | X          | X      |
| `npm`                                                          | X          | X      |
| `nss`                                                          | X          | X      |
| `opensearch-dashboards-2`                                      | X          | X      |
| `opensearch-dashboards-2-alerting-dashboards-plugin`           | X          | X      |
| `opensearch-dashboards-2-anomaly-detection-dashboards-plugin`  | X          | X      |
| `opensearch-dashboards-2-config`                               | X          | X      |
| `opensearch-dashboards-2-dashboards-maps`                      | X          | X      |
| `opensearch-dashboards-2-dashboards-notifications`             | X          | X      |
| `opensearch-dashboards-2-dashboards-observability`             | X          | X      |
| `opensearch-dashboards-2-dashboards-query-workbench`           | X          | X      |
| `opensearch-dashboards-2-dashboards-reporting`                 | X          | X      |
| `opensearch-dashboards-2-dashboards-search-relevance`          | X          | X      |
| `opensearch-dashboards-2-dashboards-visualizations`            | X          | X      |
| `opensearch-dashboards-2-index-management-dashboards-plugin`   | X          | X      |
| `opensearch-dashboards-2-ml-commons-dashboards`                | X          | X      |
| `opensearch-dashboards-2-security-analytics-dashboards-plugin` | X          | X      |
| `opensearch-dashboards-2-security-dashboards-plugin`           | X          | X      |
| `openssl-config`                                               | X          | X      |
| `wget`                                                         | X          |        |
| `wolfi-baselayout`                                             | X          | X      |
| `zlib`                                                         | X          | X      |

