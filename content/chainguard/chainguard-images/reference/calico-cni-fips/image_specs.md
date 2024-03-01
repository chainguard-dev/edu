---
title: "calico-cni-fips Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public calico-cni-fips Chainguard Image."
date: 2024-02-29 16:25:55
lastmod: 2024-02-29 16:25:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/calico-cni-fips/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/calico-cni-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/calico-cni-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/calico-cni-fips/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **calico-cni-fips** Image.

|              | latest-dev             | latest                 |
|--------------|------------------------|------------------------|
| Default User | `root`                 | `root`                 |
| Entrypoint   | `/opt/cni/bin/install` | `/opt/cni/bin/install` |
| CMD          | not specified          | not specified          |
| Workdir      | not specified          | not specified          |
| Has apk?     | yes                    | no                     |
| Has a shell? | yes                    | no                     |

Check the [tags history page](/chainguard/chainguard-images/reference/calico-cni-fips/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                 | latest-dev | latest |
|---------------------------------|------------|--------|
| `apk-tools`                     | X          |        |
| `bash`                          | X          |        |
| `busybox`                       | X          |        |
| `ca-certificates-bundle`        | X          | X      |
| `calico-cni-fips-compat`        | X          | X      |
| `calico-fips-cni`               | X          | X      |
| `chainguard-baselayout`         | X          | X      |
| `cni-plugins-bandwidth`         | X          | X      |
| `cni-plugins-bandwidth-compat`  | X          | X      |
| `cni-plugins-host-local`        | X          | X      |
| `cni-plugins-host-local-compat` | X          | X      |
| `cni-plugins-loopback`          | X          | X      |
| `cni-plugins-loopback-compat`   | X          | X      |
| `cni-plugins-portmap`           | X          | X      |
| `cni-plugins-portmap-compat`    | X          | X      |
| `cni-plugins-tuning`            | X          | X      |
| `cni-plugins-tuning-compat`     | X          | X      |
| `flannel-cni-plugin`            | X          | X      |
| `flannel-cni-plugin-compat`     | X          | X      |
| `git`                           | X          |        |
| `glibc`                         | X          | X      |
| `glibc-locale-posix`            | X          | X      |
| `ld-linux`                      | X          | X      |
| `libbrotlicommon1`              | X          |        |
| `libbrotlidec1`                 | X          |        |
| `libcrypt1`                     | X          |        |
| `libcrypto3`                    | X          |        |
| `libcurl-openssl4`              | X          |        |
| `libexpat1`                     | X          |        |
| `libidn2`                       | X          |        |
| `libnghttp2-14`                 | X          |        |
| `libpcre2-8-0`                  | X          |        |
| `libpsl`                        | X          |        |
| `libssl3`                       | X          |        |
| `libunistring`                  | X          |        |
| `ncurses`                       | X          |        |
| `ncurses-terminfo-base`         | X          |        |
| `openssl-config-fipshardened`   | X          | X      |
| `openssl-provider-fips`         | X          | X      |
| `wget`                          | X          |        |
| `wolfi-baselayout`              | X          | X      |
| `zlib`                          | X          |        |

