---
title: "cfssl-self-sign-fips Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public cfssl-self-sign-fips Chainguard Image."
date: 2024-07-10 00:36:03
lastmod: 2024-07-10 00:36:03
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/cfssl-self-sign-fips/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/cfssl-self-sign-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/cfssl-self-sign-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/cfssl-self-sign-fips/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **cfssl-self-sign-fips** Image.

|              | latest-dev                       | latest                           |
|--------------|----------------------------------|----------------------------------|
| Default User | `nonroot`                        | `nonroot`                        |
| Entrypoint   | not specified                    | not specified                    |
| CMD          | `/scripts/generate-certificates` | `/scripts/generate-certificates` |
| Workdir      | not specified                    | not specified                    |
| Has apk?     | yes                              | no                               |
| Has a shell? | yes                              | yes                              |

Check the [tags history page](/chainguard/chainguard-images/reference/cfssl-self-sign-fips/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                                   | latest-dev | latest |
|---------------------------------------------------|------------|--------|
| `apk-tools`                                       | X          |        |
| `bash`                                            | X          |        |
| `busybox`                                         | X          | X      |
| `ca-certificates-bundle`                          | X          | X      |
| `cfssl-fips`                                      | X          | X      |
| `cfssl-json-fips`                                 | X          | X      |
| `chainguard-baselayout`                           | X          | X      |
| `git`                                             | X          |        |
| `gitlab-cng-ee-fips-17.1-cfssl-self-sign-scripts` | X          | X      |
| `glibc`                                           | X          | X      |
| `glibc-locale-posix`                              | X          | X      |
| `ld-linux`                                        | X          | X      |
| `libbrotlicommon1`                                | X          |        |
| `libbrotlidec1`                                   | X          |        |
| `libcrypt1`                                       | X          | X      |
| `libcrypto3`                                      | X          | X      |
| `libcurl-openssl4`                                | X          |        |
| `libexpat1`                                       | X          |        |
| `libidn2`                                         | X          |        |
| `libnghttp2-14`                                   | X          |        |
| `libpcre2-8-0`                                    | X          |        |
| `libpsl`                                          | X          |        |
| `libssl3`                                         | X          | X      |
| `libunistring`                                    | X          |        |
| `libxcrypt`                                       | X          | X      |
| `ncurses`                                         | X          |        |
| `ncurses-terminfo-base`                           | X          |        |
| `openssl-config-fipshardened`                     | X          | X      |
| `openssl-provider-fips`                           | X          | X      |
| `wget`                                            | X          |        |
| `wolfi-baselayout`                                | X          | X      |
| `zlib`                                            | X          |        |

