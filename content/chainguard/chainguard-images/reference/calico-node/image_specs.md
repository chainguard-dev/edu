---
title: "calico-node Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public calico-node Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/calico-node/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/calico-node/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/calico-node/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/calico-node/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **calico-node** Image.

## Variants Compared
The **calico-node** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest                  |
|--------------|-------------------------|
| Default User | `root`                  |
| Entrypoint   | `/usr/sbin/start_runit` |
| CMD          | not specified           |
| Workdir      | not specified           |
| Has apk?     | no                      |
| Has a shell? | yes                     |

Check the [tags history page](/chainguard/chainguard-images/reference/calico-node/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest |
|--------------------------|--------|
| `bash`                   | X      |
| `busybox`                | X      |
| `ca-certificates-bundle` | X      |
| `calico-node`            | X      |
| `conntrack-tools`        | X      |
| `glibc`                  | X      |
| `glibc-locale-posix`     | X      |
| `ip6tables`              | X      |
| `iproute2`               | X      |
| `ipset`                  | X      |
| `iptables`               | X      |
| `ld-linux`               | X      |
| `libbpf`                 | X      |
| `libbz2-1`               | X      |
| `libcrypt1`              | X      |
| `libelf`                 | X      |
| `libmnl`                 | X      |
| `libnetfilter_conntrack` | X      |
| `libnetfilter_cthelper`  | X      |
| `libnetfilter_cttimeout` | X      |
| `libnetfilter_queue`     | X      |
| `libnfnetlink`           | X      |
| `libnftnl`               | X      |
| `libpcap`                | X      |
| `libproc-2-0`            | X      |
| `ncurses`                | X      |
| `ncurses-terminfo-base`  | X      |
| `procps`                 | X      |
| `runit`                  | X      |
| `wolfi-baselayout`       | X      |
| `xz`                     | X      |
| `zlib`                   | X      |

