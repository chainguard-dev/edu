---
title: "k3s Image Variants"
type: "article"
description: "Detailed information about the public k3s Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "k3s"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **k3s** Image.

## Variants Compared
The **k3s** Chainguard Image currently has 10 public variants: 

- `allinone-latest-dev`
- `allinone-latest`
- `embedded-latest-embedded`
- `embedded-latest`
- `images-latest-dev`
- `images-latest-images-dev`
- `images-latest-images`
- `images-latest`
- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | allinone-latest-dev | allinone-latest | embedded-latest-embedded | embedded-latest | images-latest-dev | images-latest-images-dev | images-latest-images | images-latest | latest-dev    | latest        |
|--------------|---------------------|-----------------|--------------------------|-----------------|-------------------|--------------------------|----------------------|---------------|---------------|---------------|
| Default User | `root`              | `root`          | `root`                   | `root`          | `root`            | `root`                   | `root`               | `root`        | `root`        | `root`        |
| Entrypoint   | `/bin/k3s`          | `/bin/k3s`      | `/bin/k3s`               | `/bin/k3s`      | `/bin/k3s`        | `/bin/k3s`               | `/bin/k3s`           | `/bin/k3s`    | `/bin/k3s`    | `/bin/k3s`    |
| CMD          | `agent`             | `agent`         | `agent`                  | `agent`         | `agent`           | `agent`                  | `agent`              | `agent`       | `agent`       | `agent`       |
| Workdir      | not specified       | not specified   | not specified            | not specified   | not specified     | not specified            | not specified        | not specified | not specified | not specified |
| Has apk?     | yes                 | no              | no                       | no              | yes               | yes                      | no                   | no            | yes           | no            |
| Has a shell? | yes                 | yes             | yes                      | yes             | yes               | yes                      | yes                  | yes           | yes           | yes           |

Check the [tags history page](/chainguard/chainguard-images/reference/k3s/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                              | allinone-latest-dev | allinone-latest | embedded-latest-embedded | embedded-latest | images-latest-dev | images-latest-images-dev | images-latest-images | images-latest | latest-dev | latest |
|------------------------------|---------------------|-----------------|--------------------------|-----------------|-------------------|--------------------------|----------------------|---------------|------------|--------|
| `apk-tools`                  | X                   |                 |                          |                 | X                 | X                        |                      |               | X          |        |
| `bash`                       | X                   |                 |                          |                 | X                 | X                        |                      |               | X          |        |
| `busybox`                    | X                   | X               | X                        | X               | X                 | X                        | X                    | X             | X          | X      |
| `ca-certificates-bundle`     | X                   | X               | X                        | X               | X                 | X                        | X                    | X             | X          | X      |
| `conntrack-tools`            | X                   | X               | X                        | X               | X                 | X                        | X                    | X             | X          | X      |
| `containerd-shim-runc-v2`    | X                   | X               |                          |                 | X                 |                          |                      | X             | X          | X      |
| `git`                        | X                   |                 |                          |                 | X                 | X                        |                      |               | X          |        |
| `glibc`                      | X                   | X               | X                        | X               | X                 | X                        | X                    | X             | X          | X      |
| `glibc-locale-posix`         | X                   | X               | X                        | X               | X                 | X                        | X                    | X             | X          | X      |
| `ip6tables`                  | X                   | X               | X                        | X               | X                 | X                        | X                    | X             | X          | X      |
| `iptables`                   | X                   | X               | X                        | X               | X                 | X                        | X                    | X             | X          | X      |
| `k3s`                        | X                   | X               |                          |                 | X                 | X                        | X                    | X             | X          | X      |
| `k3s-images`                 | X                   | X               |                          |                 | X                 | X                        | X                    | X             |            |        |
| `kmod`                       | X                   | X               | X                        | X               | X                 | X                        | X                    | X             | X          | X      |
| `ld-linux`                   | X                   | X               | X                        | X               | X                 | X                        | X                    | X             | X          | X      |
| `libblkid`                   | X                   | X               | X                        | X               | X                 | X                        | X                    | X             | X          | X      |
| `libbrotlicommon1`           | X                   |                 |                          |                 | X                 | X                        |                      |               | X          |        |
| `libbrotlidec1`              | X                   |                 |                          |                 | X                 | X                        |                      |               | X          |        |
| `libcrypt1`                  | X                   | X               |                          | X               | X                 |                          |                      | X             | X          | X      |
| `libcrypto3`                 | X                   | X               | X                        | X               | X                 | X                        | X                    | X             | X          | X      |
| `libcurl-openssl4`           | X                   |                 |                          |                 | X                 | X                        |                      |               | X          |        |
| `libexpat1`                  | X                   |                 |                          |                 | X                 | X                        |                      |               | X          |        |
| `libmnl`                     | X                   | X               | X                        | X               | X                 | X                        | X                    | X             | X          | X      |
| `libmount`                   | X                   | X               | X                        | X               | X                 | X                        | X                    | X             | X          | X      |
| `libnetfilter_conntrack`     | X                   | X               | X                        | X               | X                 | X                        | X                    | X             | X          | X      |
| `libnetfilter_cthelper`      | X                   | X               | X                        | X               | X                 | X                        | X                    | X             | X          | X      |
| `libnetfilter_cttimeout`     | X                   | X               | X                        | X               | X                 | X                        | X                    | X             | X          | X      |
| `libnetfilter_queue`         | X                   | X               | X                        | X               | X                 | X                        | X                    | X             | X          | X      |
| `libnfnetlink`               | X                   | X               | X                        | X               | X                 | X                        | X                    | X             | X          | X      |
| `libnftnl`                   | X                   | X               | X                        | X               | X                 | X                        | X                    | X             | X          | X      |
| `libnghttp2-14`              | X                   |                 |                          |                 | X                 | X                        |                      |               | X          |        |
| `libpcre2-8-0`               | X                   |                 |                          |                 | X                 | X                        |                      |               | X          |        |
| `libseccomp`                 | X                   | X               | X                        | X               | X                 | X                        | X                    | X             | X          | X      |
| `libssl3`                    | X                   |                 |                          |                 | X                 | X                        |                      |               | X          |        |
| `libzstd1`                   | X                   | X               | X                        | X               | X                 | X                        | X                    | X             | X          | X      |
| `mount`                      | X                   | X               | X                        | X               | X                 | X                        | X                    | X             | X          | X      |
| `ncurses`                    | X                   |                 |                          |                 | X                 | X                        |                      |               | X          |        |
| `ncurses-terminfo-base`      | X                   |                 |                          |                 | X                 | X                        |                      |               | X          |        |
| `openssl-config`             | X                   | X               | X                        | X               | X                 | X                        | X                    | X             | X          | X      |
| `runc`                       | X                   | X               |                          |                 | X                 | X                        | X                    | X             | X          | X      |
| `umount`                     | X                   | X               | X                        | X               | X                 | X                        | X                    | X             | X          | X      |
| `wolfi-baselayout`           | X                   | X               | X                        | X               | X                 | X                        | X                    | X             | X          | X      |
| `xz`                         | X                   | X               | X                        | X               | X                 | X                        | X                    | X             | X          | X      |
| `zlib`                       | X                   | X               | X                        | X               | X                 | X                        | X                    | X             | X          | X      |
| `k3s-embedded`               |                     |                 | X                        | X               |                   |                          |                      |               |            |        |
| `crictl`                     |                     |                 |                          |                 | X                 | X                        |                      |               |            |        |
| `ctr`                        |                     |                 |                          |                 | X                 | X                        |                      |               |            |        |
| `kubectl`                    |                     |                 |                          |                 | X                 | X                        |                      |               |            |        |
| `containerd`                 |                     |                 |                          |                 |                   | X                        | X                    |               |            |        |
| `fuse-overlayfs`             |                     |                 |                          |                 |                   |                          |                      |               | X          | X      |
| `fuse-overlayfs-snapshotter` |                     |                 |                          |                 |                   |                          |                      |               | X          | X      |
| `fuse3`                      |                     |                 |                          |                 |                   |                          |                      |               | X          | X      |
| `fuse3-libs`                 |                     |                 |                          |                 |                   |                          |                      |               | X          | X      |

