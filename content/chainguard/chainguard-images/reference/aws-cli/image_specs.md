---
title: "aws-cli Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public aws-cli Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/aws-cli/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/aws-cli/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/aws-cli/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/aws-cli/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **aws-cli** Image.

## Variants Compared
The **aws-cli** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev    | latest        |
|--------------|---------------|---------------|
| Default User | `65532`       | `65532`       |
| Entrypoint   | `aws`         | `aws`         |
| CMD          | not specified | not specified |
| Workdir      | not specified | not specified |
| Has apk?     | yes           | no            |
| Has a shell? | yes           | no            |

Check the [tags history page](/chainguard/chainguard-images/reference/aws-cli/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-dev | latest |
|--------------------------|------------|--------|
| `apk-tools`              | X          |        |
| `aws-cli`                | X          | X      |
| `bash`                   | X          |        |
| `busybox`                | X          |        |
| `ca-certificates-bundle` | X          | X      |
| `gdbm`                   | X          | X      |
| `git`                    | X          |        |
| `glibc`                  | X          | X      |
| `glibc-locale-posix`     | X          | X      |
| `groff`                  | X          | X      |
| `ld-linux`               | X          | X      |
| `libbrotlicommon1`       | X          |        |
| `libbrotlidec1`          | X          |        |
| `libbz2-1`               | X          | X      |
| `libcrypt1`              | X          | X      |
| `libcrypto3`             | X          | X      |
| `libcurl-openssl4`       | X          |        |
| `libexpat1`              | X          | X      |
| `libffi`                 | X          | X      |
| `libgcc`                 | X          | X      |
| `libnghttp2-14`          | X          |        |
| `libpcre2-8-0`           | X          |        |
| `libssl3`                | X          | X      |
| `libstdc++`              | X          | X      |
| `mpdecimal`              | X          | X      |
| `ncurses`                | X          | X      |
| `ncurses-terminfo-base`  | X          | X      |
| `openssl-config`         | X          | X      |
| `py3-asn1`               | X          | X      |
| `py3-botocore`           | X          | X      |
| `py3-colorama`           | X          | X      |
| `py3-dateutil`           | X          | X      |
| `py3-docutils`           | X          | X      |
| `py3-jmespath`           | X          | X      |
| `py3-rsa`                | X          | X      |
| `py3-s3transfer`         | X          | X      |
| `py3-six`                | X          | X      |
| `py3-urllib3`            | X          | X      |
| `py3-yaml`               | X          | X      |
| `py3.11-setuptools`      | X          | X      |
| `python-3.11`            | X          | X      |
| `readline`               | X          | X      |
| `sqlite-libs`            | X          | X      |
| `wolfi-baselayout`       | X          | X      |
| `xz`                     | X          | X      |
| `yaml`                   | X          | X      |
| `zlib`                   | X          | X      |

