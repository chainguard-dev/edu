---
title: "haproxy-fips Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public haproxy-fips Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-05-03 00:45:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/haproxy-fips/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/haproxy-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/haproxy-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/haproxy-fips/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **haproxy-fips** Image.

|              | latest-dev                                      | latest                                          |
|--------------|-------------------------------------------------|-------------------------------------------------|
| Default User | `haproxy`                                       | `haproxy`                                       |
| Entrypoint   | `/usr/local/bin/docker-entrypoint.sh`           | `/usr/local/bin/docker-entrypoint.sh`           |
| CMD          | `haproxy -f /usr/local/etc/haproxy/haproxy.cfg` | `haproxy -f /usr/local/etc/haproxy/haproxy.cfg` |
| Workdir      | not specified                                   | not specified                                   |
| Has apk?     | yes                                             | no                                              |
| Has a shell? | yes                                             | yes                                             |

Check the [tags history page](/chainguard/chainguard-images/reference/haproxy-fips/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                               | latest-dev | latest |
|-------------------------------|------------|--------|
| `apk-tools`                   | X          |        |
| `bash`                        | X          | X      |
| `busybox`                     | X          | X      |
| `ca-certificates-bundle`      | X          | X      |
| `chainguard-baselayout`       | X          | X      |
| `dataplaneapi`                | X          | X      |
| `git`                         | X          |        |
| `glibc`                       | X          | X      |
| `glibc-locale-posix`          | X          | X      |
| `haproxy`                     | X          | X      |
| `haproxy-2.9-oci-entrypoint`  | X          | X      |
| `ld-linux`                    | X          | X      |
| `libbrotlicommon1`            | X          |        |
| `libbrotlidec1`               | X          |        |
| `libcrypt1`                   | X          | X      |
| `libcrypto3`                  | X          | X      |
| `libcurl-openssl4`            | X          |        |
| `libexpat1`                   | X          |        |
| `libgcc`                      | X          | X      |
| `libidn2`                     | X          |        |
| `libnghttp2-14`               | X          |        |
| `libpcre2-8-0`                | X          | X      |
| `libpcre2-posix-3`            | X          | X      |
| `libpsl`                      | X          |        |
| `libssl3`                     | X          | X      |
| `libunistring`                | X          |        |
| `libxcrypt`                   | X          | X      |
| `ncurses`                     | X          | X      |
| `ncurses-terminfo-base`       | X          | X      |
| `openssl`                     | X          |        |
| `openssl-config-fipshardened` | X          | X      |
| `openssl-provider-fips`       | X          | X      |
| `openssl-provider-legacy`     | X          |        |
| `posix-libc-utils`            | X          | X      |
| `wget`                        | X          |        |
| `wolfi-baselayout`            | X          | X      |
| `zlib`                        | X          |        |

