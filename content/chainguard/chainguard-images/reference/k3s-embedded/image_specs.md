---
title: "k3s-embedded Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public k3s-embedded Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/k3s-embedded/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/k3s-embedded/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/k3s-embedded/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/k3s-embedded/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **k3s-embedded** Image.

## Variants Compared
The **k3s-embedded** Chainguard Image currently has 2 public variants: 

- `latest-embedded`
- `latest`

The table has detailed information about each of these variants.

|              | latest-embedded | latest        |
|--------------|-----------------|---------------|
| Default User | `0`             | `0`           |
| Entrypoint   | `/bin/k3s`      | `/bin/k3s`    |
| CMD          | `agent`         | `agent`       |
| Workdir      | not specified   | not specified |
| Has apk?     | no              | no            |
| Has a shell? | yes             | yes           |

Check the [tags history page](/chainguard/chainguard-images/reference/k3s-embedded/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-embedded | latest |
|--------------------------|-----------------|--------|
| `busybox`                | X               | X      |
| `ca-certificates-bundle` | X               | X      |
| `conntrack-tools`        | X               | X      |
| `glibc`                  | X               | X      |
| `glibc-locale-posix`     | X               | X      |
| `ip6tables`              | X               | X      |
| `iptables`               | X               | X      |
| `k3s-embedded`           | X               | X      |
| `kmod`                   | X               | X      |
| `ld-linux`               | X               | X      |
| `libblkid`               | X               | X      |
| `libcrypto3`             | X               | X      |
| `libmnl`                 | X               | X      |
| `libmount`               | X               | X      |
| `libnetfilter_conntrack` | X               | X      |
| `libnetfilter_cthelper`  | X               | X      |
| `libnetfilter_cttimeout` | X               | X      |
| `libnetfilter_queue`     | X               | X      |
| `libnfnetlink`           | X               | X      |
| `libnftnl`               | X               | X      |
| `libseccomp`             | X               | X      |
| `libzstd1`               | X               | X      |
| `mount`                  | X               | X      |
| `openssl-config`         | X               | X      |
| `umount`                 | X               | X      |
| `wolfi-baselayout`       | X               | X      |
| `xz`                     | X               | X      |
| `zlib`                   | X               | X      |
| `libcrypt1`              |                 | X      |

