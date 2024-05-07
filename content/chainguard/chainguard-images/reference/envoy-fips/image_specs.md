---
title: "envoy-fips Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public envoy-fips Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-05-07 00:45:47
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/envoy-fips/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/envoy-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/envoy-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/envoy-fips/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **envoy-fips** Image.

|              | latest-dev                                | latest                                    |
|--------------|-------------------------------------------|-------------------------------------------|
| Default User | `envoy`                                   | `envoy`                                   |
| Entrypoint   | `/var/lib/envoy/init/envoy-entrypoint.sh` | `/var/lib/envoy/init/envoy-entrypoint.sh` |
| CMD          | not specified                             | not specified                             |
| Workdir      | not specified                             | not specified                             |
| Has apk?     | yes                                       | no                                        |
| Has a shell? | yes                                       | yes                                       |

Check the [tags history page](/chainguard/chainguard-images/reference/envoy-fips/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                               | latest-dev | latest |
|-------------------------------|------------|--------|
| `apk-tools`                   | X          |        |
| `bash`                        | X          |        |
| `busybox`                     | X          | X      |
| `ca-certificates-bundle`      | X          | X      |
| `chainguard-baselayout`       | X          | X      |
| `envoy-1.29-config`           | X          | X      |
| `envoy-1.29-oci-entrypoint`   | X          | X      |
| `envoy-fips-1.28`             | X          |        |
| `git`                         | X          |        |
| `glibc`                       | X          | X      |
| `glibc-locale-posix`          | X          | X      |
| `ld-linux`                    | X          | X      |
| `libbrotlicommon1`            | X          |        |
| `libbrotlidec1`               | X          |        |
| `libcrypt1`                   | X          | X      |
| `libcrypto3`                  | X          |        |
| `libcurl-openssl4`            | X          |        |
| `libexpat1`                   | X          |        |
| `libidn2`                     | X          |        |
| `libnghttp2-14`               | X          |        |
| `libpcre2-8-0`                | X          |        |
| `libpsl`                      | X          |        |
| `libssl3`                     | X          |        |
| `libunistring`                | X          |        |
| `libxcrypt`                   | X          | X      |
| `ncurses`                     | X          |        |
| `ncurses-terminfo-base`       | X          |        |
| `openssl-config-fipshardened` | X          | X      |
| `openssl-provider-fips`       | X          | X      |
| `su-exec`                     | X          | X      |
| `wget`                        | X          |        |
| `wolfi-baselayout`            | X          | X      |
| `zlib`                        | X          |        |
| `envoy-fips-1.27`             |            | X      |

