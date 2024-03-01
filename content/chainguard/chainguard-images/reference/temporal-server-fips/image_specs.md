---
title: "temporal-server-fips Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public temporal-server-fips Chainguard Image."
date: 2024-02-29 16:25:55
lastmod: 2024-02-29 16:25:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/temporal-server-fips/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/temporal-server-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/temporal-server-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/temporal-server-fips/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **temporal-server-fips** Image.

|              | latest-dev                    | latest                        |
|--------------|-------------------------------|-------------------------------|
| Default User | `temporal`                    | `temporal`                    |
| Entrypoint   | `/etc/temporal/entrypoint.sh` | `/etc/temporal/entrypoint.sh` |
| CMD          | not specified                 | not specified                 |
| Workdir      | `/etc/temporal`               | `/etc/temporal`               |
| Has apk?     | yes                           | no                            |
| Has a shell? | yes                           | yes                           |

Check the [tags history page](/chainguard/chainguard-images/reference/temporal-server-fips/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                         | latest-dev | latest |
|-----------------------------------------|------------|--------|
| `apk-tools`                             | X          |        |
| `bash`                                  | X          | X      |
| `busybox`                               | X          |        |
| `ca-certificates-bundle`                | X          | X      |
| `chainguard-baselayout`                 | X          | X      |
| `dockerize-fips`                        | X          | X      |
| `git`                                   | X          |        |
| `glibc`                                 | X          | X      |
| `glibc-locale-posix`                    | X          | X      |
| `ld-linux`                              | X          | X      |
| `libbrotlicommon1`                      | X          |        |
| `libbrotlidec1`                         | X          |        |
| `libcrypt1`                             | X          |        |
| `libcrypto3`                            | X          |        |
| `libcurl-openssl4`                      | X          |        |
| `libexpat1`                             | X          |        |
| `libidn2`                               | X          |        |
| `libnghttp2-14`                         | X          |        |
| `libpcre2-8-0`                          | X          |        |
| `libpsl`                                | X          |        |
| `libssl3`                               | X          |        |
| `libunistring`                          | X          |        |
| `ncurses`                               | X          | X      |
| `ncurses-terminfo-base`                 | X          | X      |
| `openssl-config-fipshardened`           | X          | X      |
| `openssl-provider-fips`                 | X          | X      |
| `posix-libc-utils`                      | X          | X      |
| `tctl-authorization-plugin-fips-compat` | X          | X      |
| `tctl-fips`                             | X          | X      |
| `tctl-fips-compat`                      | X          | X      |
| `temporal-compat-fips`                  | X          | X      |
| `temporal-docker-builds`                | X          | X      |
| `temporal-fips`                         | X          | X      |
| `temporal-server-fips`                  | X          | X      |
| `temporal-server-fips-compat`           | X          | X      |
| `temporal-server-oci-entrypoint-fips`   | X          | X      |
| `wget`                                  | X          |        |
| `wolfi-baselayout`                      | X          | X      |
| `zlib`                                  | X          |        |

