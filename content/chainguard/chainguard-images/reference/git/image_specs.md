---
title: "git Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public git Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-01-25 00:19:46
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/git/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/git/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/git/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/git/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **git** Image.

## Variants Compared
The **git** Chainguard Image currently has 8 public variants: 

- `latest-dev`
- `latest-glibc-dev`
- `latest-glibc-root-dev`
- `latest-glibc-root`
- `latest-glibc`
- `latest-root-dev`
- `latest-root`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev     | latest-glibc-dev | latest-glibc-root-dev | latest-glibc-root | latest-glibc   | latest-root-dev | latest-root    | latest         |
|--------------|----------------|------------------|-----------------------|-------------------|----------------|-----------------|----------------|----------------|
| Default User | `git`          | `git`            | `root`                | `root`            | `git`          | `root`          | `root`         | `git`          |
| Entrypoint   | `/usr/bin/git` | `/usr/bin/git`   | `/usr/bin/git`        | `/usr/bin/git`    | `/usr/bin/git` | `/usr/bin/git`  | `/usr/bin/git` | `/usr/bin/git` |
| CMD          | not specified  | not specified    | not specified         | not specified     | not specified  | not specified   | not specified  | not specified  |
| Workdir      | `/home/git`    | `/home/git`      | `/home/git`           | `/home/git`       | `/home/git`    | `/home/git`     | `/home/git`    | `/home/git`    |
| Has apk?     | yes            | yes              | yes                   | no                | no             | yes             | no             | no             |
| Has a shell? | yes            | yes              | yes                   | no                | no             | yes             | yes            | yes            |

Check the [tags history page](/chainguard/chainguard-images/reference/git/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-dev | latest-glibc-dev | latest-glibc-root-dev | latest-glibc-root | latest-glibc | latest-root-dev | latest-root | latest |
|--------------------------|------------|------------------|-----------------------|-------------------|--------------|-----------------|-------------|--------|
| `alpine-baselayout-data` | X          |                  |                       |                   |              | X               | X           | X      |
| `alpine-keys`            | X          |                  |                       |                   |              | X               | X           | X      |
| `alpine-release`         | X          |                  |                       |                   |              | X               | X           | X      |
| `apk-tools`              | X          | X                | X                     |                   |              | X               |             |        |
| `bash`                   | X          | X                | X                     |                   |              | X               |             |        |
| `brotli-libs`            | X          |                  |                       |                   |              | X               | X           | X      |
| `busybox`                | X          | X                | X                     |                   |              | X               | X           | X      |
| `busybox-binsh`          | X          |                  |                       |                   |              | X               | X           | X      |
| `c-ares`                 | X          |                  |                       |                   |              | X               | X           | X      |
| `ca-certificates`        | X          |                  |                       |                   |              | X               | X           | X      |
| `ca-certificates-bundle` | X          | X                | X                     | X                 | X            | X               | X           | X      |
| `git`                    | X          | X                | X                     | X                 | X            | X               | X           | X      |
| `git-lfs`                | X          | X                | X                     | X                 | X            | X               | X           | X      |
| `libcrypto3`             | X          | X                | X                     | X                 | X            | X               | X           | X      |
| `libcurl`                | X          |                  |                       |                   |              | X               | X           | X      |
| `libedit`                | X          | X                | X                     | X                 | X            | X               | X           | X      |
| `libexpat`               | X          |                  |                       |                   |              | X               | X           | X      |
| `libidn2`                | X          | X                | X                     | X                 | X            | X               | X           | X      |
| `libncursesw`            | X          |                  |                       |                   |              | X               | X           | X      |
| `libpsl`                 | X          | X                | X                     | X                 | X            | X               | X           | X      |
| `libssl3`                | X          | X                | X                     | X                 | X            | X               | X           | X      |
| `libunistring`           | X          | X                | X                     | X                 | X            | X               | X           | X      |
| `musl`                   | X          |                  |                       |                   |              | X               | X           | X      |
| `ncurses-terminfo-base`  | X          | X                | X                     | X                 | X            | X               | X           | X      |
| `nghttp2-libs`           | X          |                  |                       |                   |              | X               | X           | X      |
| `openssh-client-common`  | X          |                  |                       |                   |              | X               | X           | X      |
| `openssh-client-default` | X          |                  |                       |                   |              | X               | X           | X      |
| `openssh-keygen`         | X          |                  |                       |                   |              | X               | X           | X      |
| `pcre2`                  | X          |                  |                       |                   |              | X               | X           | X      |
| `readline`               | X          |                  |                       |                   |              | X               |             |        |
| `ssl_client`             | X          |                  |                       |                   |              | X               | X           | X      |
| `zlib`                   | X          | X                | X                     | X                 | X            | X               | X           | X      |
| `glibc`                  |            | X                | X                     | X                 | X            |                 |             |        |
| `glibc-locale-posix`     |            | X                | X                     | X                 | X            |                 |             |        |
| `ld-linux`               |            | X                | X                     | X                 | X            |                 |             |        |
| `libbrotlicommon1`       |            | X                | X                     | X                 | X            |                 |             |        |
| `libbrotlidec1`          |            | X                | X                     | X                 | X            |                 |             |        |
| `libcrypt1`              |            | X                | X                     |                   |              |                 |             |        |
| `libcurl-openssl4`       |            | X                | X                     | X                 | X            |                 |             |        |
| `libexpat1`              |            | X                | X                     | X                 | X            |                 |             |        |
| `libnghttp2-14`          |            | X                | X                     | X                 | X            |                 |             |        |
| `libpcre2-8-0`           |            | X                | X                     | X                 | X            |                 |             |        |
| `ncurses`                |            | X                | X                     | X                 | X            |                 |             |        |
| `openssh-client`         |            | X                | X                     | X                 | X            |                 |             |        |
| `openssl-config`         |            | X                | X                     | X                 | X            |                 |             |        |
| `wolfi-baselayout`       |            | X                | X                     | X                 | X            |                 |             |        |

