---
title: "temporal-admin-tools-fips Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public temporal-admin-tools-fips Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-04-05 00:47:12
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/temporal-admin-tools-fips/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/temporal-admin-tools-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/temporal-admin-tools-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/temporal-admin-tools-fips/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **temporal-admin-tools-fips** Image.

|              | latest-dev       | latest           |
|--------------|------------------|------------------|
| Default User | `temporal`       | `temporal`       |
| Entrypoint   | `/sbin/tini --`  | `/sbin/tini --`  |
| CMD          | `sleep infinity` | `sleep infinity` |
| Workdir      | `/etc/temporal`  | `/etc/temporal`  |
| Has apk?     | yes              | no               |
| Has a shell? | yes              | yes              |

Check the [tags history page](/chainguard/chainguard-images/reference/temporal-admin-tools-fips/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                         | latest-dev | latest |
|-----------------------------------------|------------|--------|
| `apk-tools`                             | X          |        |
| `bash`                                  | X          | X      |
| `busybox`                               | X          | X      |
| `ca-certificates-bundle`                | X          | X      |
| `chainguard-baselayout`                 | X          | X      |
| `git`                                   | X          |        |
| `glibc`                                 | X          | X      |
| `glibc-locale-posix`                    | X          | X      |
| `ld-linux`                              | X          | X      |
| `libbrotlicommon1`                      | X          |        |
| `libbrotlidec1`                         | X          |        |
| `libcrypt1`                             | X          | X      |
| `libcrypto3`                            | X          | X      |
| `libcurl-openssl4`                      | X          |        |
| `libexpat1`                             | X          |        |
| `libidn2`                               | X          |        |
| `libnghttp2-14`                         | X          |        |
| `libpcre2-8-0`                          | X          |        |
| `libpsl`                                | X          |        |
| `libssl3`                               | X          | X      |
| `libunistring`                          | X          |        |
| `libxcrypt`                             | X          | X      |
| `ncurses`                               | X          | X      |
| `ncurses-terminfo-base`                 | X          | X      |
| `openssl-config-fipshardened`           | X          | X      |
| `openssl-provider-fips`                 | X          | X      |
| `tctl-authorization-plugin-fips`        | X          | X      |
| `tctl-authorization-plugin-fips-compat` | X          | X      |
| `tctl-fips`                             | X          | X      |
| `tctl-fips-compat`                      | X          | X      |
| `tdbg-fips`                             | X          | X      |
| `tdbg-fips-compat`                      | X          | X      |
| `temporal-cassandra-tool-fips`          | X          | X      |
| `temporal-cassandra-tool-fips-compat`   | X          | X      |
| `temporal-compat-fips`                  | X          | X      |
| `temporal-fips`                         | X          | X      |
| `temporal-server-schema-fips`           | X          | X      |
| `temporal-sql-tool-fips`                | X          | X      |
| `temporal-sql-tool-fips-compat`         | X          | X      |
| `tini`                                  | X          | X      |
| `wget`                                  | X          |        |
| `wolfi-baselayout`                      | X          | X      |
| `zlib`                                  | X          |        |

