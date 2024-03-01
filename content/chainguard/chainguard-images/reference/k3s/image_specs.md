---
title: "k3s Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public k3s Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-03-01 12:14:22
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/k3s/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/k3s/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/k3s/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/k3s/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **k3s** Image.

|              | latest-dev    | latest        |
|--------------|---------------|---------------|
| Default User | `root`        | `root`        |
| Entrypoint   | `/bin/k3s`    | `/bin/k3s`    |
| CMD          | `agent`       | `agent`       |
| Workdir      | not specified | not specified |
| Has apk?     | yes           | no            |
| Has a shell? | yes           | yes           |

Check the [tags history page](/chainguard/chainguard-images/reference/k3s/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                              | latest-dev | latest |
|------------------------------|------------|--------|
| `apk-tools`                  | X          |        |
| `bash`                       | X          |        |
| `busybox`                    | X          | X      |
| `ca-certificates-bundle`     | X          | X      |
| `chainguard-baselayout`      | X          | X      |
| `conntrack-tools`            | X          | X      |
| `containerd-shim-runc-v2`    | X          | X      |
| `fuse-overlayfs`             | X          | X      |
| `fuse-overlayfs-snapshotter` | X          | X      |
| `fuse3`                      | X          | X      |
| `fuse3-libs`                 | X          | X      |
| `git`                        | X          |        |
| `glibc`                      | X          | X      |
| `glibc-locale-posix`         | X          | X      |
| `ip6tables`                  | X          | X      |
| `iptables`                   | X          | X      |
| `k3s`                        | X          | X      |
| `kmod`                       | X          | X      |
| `ld-linux`                   | X          | X      |
| `libblkid`                   | X          | X      |
| `libbrotlicommon1`           | X          |        |
| `libbrotlidec1`              | X          |        |
| `libcrypt1`                  | X          | X      |
| `libcrypto3`                 | X          | X      |
| `libcurl-openssl4`           | X          |        |
| `libexpat1`                  | X          |        |
| `libidn2`                    | X          |        |
| `libmnl`                     | X          | X      |
| `libmount`                   | X          | X      |
| `libnetfilter_conntrack`     | X          | X      |
| `libnetfilter_cthelper`      | X          | X      |
| `libnetfilter_cttimeout`     | X          | X      |
| `libnetfilter_queue`         | X          | X      |
| `libnfnetlink`               | X          | X      |
| `libnftnl`                   | X          | X      |
| `libnghttp2-14`              | X          |        |
| `libpcre2-8-0`               | X          |        |
| `libpsl`                     | X          |        |
| `libseccomp`                 | X          | X      |
| `libssl3`                    | X          |        |
| `libunistring`               | X          |        |
| `libzstd1`                   | X          | X      |
| `mount`                      | X          | X      |
| `ncurses`                    | X          |        |
| `ncurses-terminfo-base`      | X          |        |
| `openssl-config`             | X          | X      |
| `runc`                       | X          | X      |
| `umount`                     | X          | X      |
| `wget`                       | X          |        |
| `wolfi-baselayout`           | X          | X      |
| `xz`                         | X          | X      |
| `zlib`                       | X          | X      |

