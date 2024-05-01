---
title: "temporal-server Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public temporal-server Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-05-01 00:46:56
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/temporal-server/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/temporal-server/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/temporal-server/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/temporal-server/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **temporal-server** Image.

|              | latest-dev                    | latest                        |
|--------------|-------------------------------|-------------------------------|
| Default User | `temporal`                    | `temporal`                    |
| Entrypoint   | `/etc/temporal/entrypoint.sh` | `/etc/temporal/entrypoint.sh` |
| CMD          | not specified                 | not specified                 |
| Workdir      | `/etc/temporal`               | `/etc/temporal`               |
| Has apk?     | yes                           | no                            |
| Has a shell? | yes                           | yes                           |

Check the [tags history page](/chainguard/chainguard-images/reference/temporal-server/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                    | latest-dev | latest |
|------------------------------------|------------|--------|
| `apk-tools`                        | X          |        |
| `bash`                             | X          | X      |
| `busybox`                          | X          |        |
| `ca-certificates-bundle`           | X          | X      |
| `chainguard-baselayout`            | X          | X      |
| `dockerize`                        | X          | X      |
| `git`                              | X          |        |
| `glibc`                            | X          | X      |
| `glibc-locale-posix`               | X          | X      |
| `ld-linux`                         | X          | X      |
| `libbrotlicommon1`                 | X          |        |
| `libbrotlidec1`                    | X          |        |
| `libcrypt1`                        | X          |        |
| `libcrypto3`                       | X          |        |
| `libcurl-openssl4`                 | X          |        |
| `libexpat1`                        | X          |        |
| `libidn2`                          | X          |        |
| `libnghttp2-14`                    | X          |        |
| `libpcre2-8-0`                     | X          |        |
| `libpsl`                           | X          |        |
| `libssl3`                          | X          |        |
| `libunistring`                     | X          |        |
| `libxcrypt`                        | X          |        |
| `ncurses`                          | X          | X      |
| `ncurses-terminfo-base`            | X          | X      |
| `posix-libc-utils`                 | X          | X      |
| `tctl`                             | X          | X      |
| `tctl-authorization-plugin-compat` | X          | X      |
| `tctl-compat`                      | X          | X      |
| `temporal`                         | X          | X      |
| `temporal-compat`                  | X          | X      |
| `temporal-docker-builds`           | X          | X      |
| `temporal-server`                  | X          | X      |
| `temporal-server-compat`           | X          | X      |
| `temporal-server-oci-entrypoint`   | X          | X      |
| `wget`                             | X          |        |
| `wolfi-baselayout`                 | X          | X      |
| `zlib`                             | X          |        |

