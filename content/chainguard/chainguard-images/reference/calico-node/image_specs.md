---
title: "calico-node Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public calico-node Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-02-29 16:25:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/calico-node/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/calico-node/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/calico-node/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/calico-node/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **calico-node** Image.

|              | latest-dev              | latest                  |
|--------------|-------------------------|-------------------------|
| Default User | `root`                  | `root`                  |
| Entrypoint   | `/usr/sbin/start_runit` | `/usr/sbin/start_runit` |
| CMD          | not specified           | not specified           |
| Workdir      | not specified           | not specified           |
| Has apk?     | yes                     | no                      |
| Has a shell? | yes                     | yes                     |

Check the [tags history page](/chainguard/chainguard-images/reference/calico-node/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-dev | latest |
|--------------------------|------------|--------|
| `apk-tools`              | X          |        |
| `bash`                   | X          | X      |
| `busybox`                | X          | X      |
| `ca-certificates-bundle` | X          | X      |
| `calico-node`            | X          | X      |
| `chainguard-baselayout`  | X          | X      |
| `conntrack-tools`        | X          | X      |
| `git`                    | X          |        |
| `glibc`                  | X          | X      |
| `glibc-locale-posix`     | X          | X      |
| `ip6tables`              | X          | X      |
| `iproute2`               | X          | X      |
| `ipset`                  | X          | X      |
| `iptables`               | X          | X      |
| `ld-linux`               | X          | X      |
| `libbpf`                 | X          | X      |
| `libbrotlicommon1`       | X          |        |
| `libbrotlidec1`          | X          |        |
| `libbz2-1`               | X          | X      |
| `libcrypt1`              | X          | X      |
| `libcrypto3`             | X          |        |
| `libcurl-openssl4`       | X          |        |
| `libelf`                 | X          | X      |
| `libexpat1`              | X          |        |
| `libidn2`                | X          |        |
| `libmnl`                 | X          | X      |
| `libnetfilter_conntrack` | X          | X      |
| `libnetfilter_cthelper`  | X          | X      |
| `libnetfilter_cttimeout` | X          | X      |
| `libnetfilter_queue`     | X          | X      |
| `libnfnetlink`           | X          | X      |
| `libnftnl`               | X          | X      |
| `libnghttp2-14`          | X          |        |
| `libpcap`                | X          | X      |
| `libpcre2-8-0`           | X          |        |
| `libproc-2-0`            | X          | X      |
| `libpsl`                 | X          |        |
| `libssl3`                | X          |        |
| `libunistring`           | X          |        |
| `libzstd1`               | X          | X      |
| `ncurses`                | X          | X      |
| `ncurses-terminfo-base`  | X          | X      |
| `openssl-config`         | X          |        |
| `procps`                 | X          | X      |
| `runit`                  | X          | X      |
| `wget`                   | X          |        |
| `wolfi-baselayout`       | X          | X      |
| `xz`                     | X          | X      |
| `zlib`                   | X          | X      |

