---
title: "nfs-subdir-external-provisioner Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public nfs-subdir-external-provisioner Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/nfs-subdir-external-provisioner/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/nfs-subdir-external-provisioner/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/nfs-subdir-external-provisioner/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/nfs-subdir-external-provisioner/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **nfs-subdir-external-provisioner** Image.

## Variants Compared
The **nfs-subdir-external-provisioner** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev                                 | latest                                     |
|--------------|--------------------------------------------|--------------------------------------------|
| Default User | `nonroot`                                  | `nonroot`                                  |
| Entrypoint   | `/usr/bin/nfs-subdir-external-provisioner` | `/usr/bin/nfs-subdir-external-provisioner` |
| CMD          | not specified                              | not specified                              |
| Workdir      | not specified                              | not specified                              |
| Has apk?     | yes                                        | no                                         |
| Has a shell? | yes                                        | yes                                        |

Check the [tags history page](/chainguard/chainguard-images/reference/nfs-subdir-external-provisioner/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                   | latest-dev | latest |
|-----------------------------------|------------|--------|
| `apk-tools`                       | X          |        |
| `bash`                            | X          |        |
| `busybox`                         | X          | X      |
| `ca-certificates-bundle`          | X          | X      |
| `cyrus-sasl`                      | X          | X      |
| `device-mapper-libs`              | X          | X      |
| `gdbm`                            | X          | X      |
| `git`                             | X          |        |
| `glibc`                           | X          | X      |
| `glibc-locale-posix`              | X          | X      |
| `heimdal`                         | X          | X      |
| `keyutils-libs`                   | X          | X      |
| `krb5-conf`                       | X          | X      |
| `krb5-libs`                       | X          | X      |
| `ld-linux`                        | X          | X      |
| `libblkid`                        | X          | X      |
| `libbrotlicommon1`                | X          |        |
| `libbrotlidec1`                   | X          |        |
| `libbz2-1`                        | X          | X      |
| `libcap`                          | X          | X      |
| `libcom_err`                      | X          | X      |
| `libcrypt1`                       | X          | X      |
| `libcrypto3`                      | X          | X      |
| `libcurl-openssl4`                | X          |        |
| `libevent`                        | X          | X      |
| `libexpat1`                       | X          | X      |
| `libffi`                          | X          | X      |
| `libgcc`                          | X          | X      |
| `libldap`                         | X          | X      |
| `libmount`                        | X          | X      |
| `libnghttp2-14`                   | X          |        |
| `libpcre2-8-0`                    | X          |        |
| `libssl3`                         | X          | X      |
| `libstdc++`                       | X          | X      |
| `libtirpc`                        | X          | X      |
| `libuuid`                         | X          | X      |
| `libverto`                        | X          | X      |
| `mount`                           | X          | X      |
| `mpdecimal`                       | X          | X      |
| `ncurses`                         | X          | X      |
| `ncurses-terminfo-base`           | X          | X      |
| `nfs-subdir-external-provisioner` | X          | X      |
| `nfs-utils`                       | X          | X      |
| `openssl-config`                  | X          | X      |
| `python-3.12`                     | X          | X      |
| `readline`                        | X          | X      |
| `sqlite-libs`                     | X          | X      |
| `umount`                          | X          | X      |
| `wolfi-baselayout`                | X          | X      |
| `xz`                              | X          | X      |
| `zlib`                            | X          | X      |

