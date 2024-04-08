---
title: "temporal-admin-tools Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public temporal-admin-tools Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-04-08 00:38:35
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/temporal-admin-tools/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/temporal-admin-tools/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/temporal-admin-tools/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/temporal-admin-tools/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **temporal-admin-tools** Image.

|              | latest-dev       | latest           |
|--------------|------------------|------------------|
| Default User | `temporal`       | `temporal`       |
| Entrypoint   | `/sbin/tini --`  | `/sbin/tini --`  |
| CMD          | `sleep infinity` | `sleep infinity` |
| Workdir      | `/etc/temporal`  | `/etc/temporal`  |
| Has apk?     | yes              | no               |
| Has a shell? | yes              | yes              |

Check the [tags history page](/chainguard/chainguard-images/reference/temporal-admin-tools/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                    | latest-dev | latest |
|------------------------------------|------------|--------|
| `apk-tools`                        | X          |        |
| `bash`                             | X          | X      |
| `busybox`                          | X          | X      |
| `ca-certificates-bundle`           | X          | X      |
| `chainguard-baselayout`            | X          | X      |
| `curl`                             | X          | X      |
| `git`                              | X          |        |
| `glibc`                            | X          | X      |
| `glibc-locale-posix`               | X          | X      |
| `ld-linux`                         | X          | X      |
| `libbrotlicommon1`                 | X          | X      |
| `libbrotlidec1`                    | X          | X      |
| `libcrypt1`                        | X          | X      |
| `libcrypto3`                       | X          | X      |
| `libcurl-openssl4`                 | X          | X      |
| `libexpat1`                        | X          |        |
| `libidn2`                          | X          | X      |
| `libnghttp2-14`                    | X          | X      |
| `libpcre2-8-0`                     | X          |        |
| `libpsl`                           | X          | X      |
| `libssl3`                          | X          | X      |
| `libunistring`                     | X          | X      |
| `libxcrypt`                        | X          | X      |
| `ncurses`                          | X          | X      |
| `ncurses-terminfo-base`            | X          | X      |
| `openssl-config`                   | X          | X      |
| `tctl`                             | X          | X      |
| `tctl-authorization-plugin`        | X          | X      |
| `tctl-authorization-plugin-compat` | X          | X      |
| `tctl-compat`                      | X          | X      |
| `tdbg`                             | X          | X      |
| `tdbg-compat`                      | X          | X      |
| `temporal`                         | X          | X      |
| `temporal-cassandra-tool`          | X          | X      |
| `temporal-cassandra-tool-compat`   | X          | X      |
| `temporal-compat`                  | X          | X      |
| `temporal-server-schema`           | X          | X      |
| `temporal-sql-tool`                | X          | X      |
| `temporal-sql-tool-compat`         | X          | X      |
| `tini`                             | X          | X      |
| `wget`                             | X          |        |
| `wolfi-baselayout`                 | X          | X      |
| `zlib`                             | X          | X      |

