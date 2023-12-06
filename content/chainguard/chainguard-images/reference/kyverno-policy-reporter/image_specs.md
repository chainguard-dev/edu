---
title: "kyverno-policy-reporter Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public kyverno-policy-reporter Chainguard Image variants"
date: 2023-12-06 17:47:48
lastmod: 2023-12-06 17:47:48
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/kyverno-policy-reporter/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/kyverno-policy-reporter/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/kyverno-policy-reporter/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kyverno-policy-reporter/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **kyverno-policy-reporter** Image.

## Variants Compared
The **kyverno-policy-reporter** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev                    | latest                        |
|--------------|-------------------------------|-------------------------------|
| Default User | `nonroot`                     | `nonroot`                     |
| Entrypoint   | `/usr/bin/policyreporter run` | `/usr/bin/policyreporter run` |
| CMD          | not specified                 | not specified                 |
| Workdir      | `/app`                        | `/app`                        |
| Has apk?     | yes                           | no                            |
| Has a shell? | yes                           | no                            |

Check the [tags history page](/chainguard/chainguard-images/reference/kyverno-policy-reporter/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                  | latest-dev | latest |
|----------------------------------|------------|--------|
| `apk-tools`                      | X          |        |
| `bash`                           | X          |        |
| `busybox`                        | X          |        |
| `ca-certificates-bundle`         | X          | X      |
| `git`                            | X          |        |
| `glibc`                          | X          |        |
| `glibc-locale-posix`             | X          |        |
| `kyverno-policy-reporter`        | X          | X      |
| `kyverno-policy-reporter-compat` | X          | X      |
| `ld-linux`                       | X          |        |
| `libbrotlicommon1`               | X          |        |
| `libbrotlidec1`                  | X          |        |
| `libcrypt1`                      | X          |        |
| `libcrypto3`                     | X          |        |
| `libcurl-openssl4`               | X          |        |
| `libexpat1`                      | X          |        |
| `libnghttp2-14`                  | X          |        |
| `libpcre2-8-0`                   | X          |        |
| `libssl3`                        | X          |        |
| `ncurses`                        | X          |        |
| `ncurses-terminfo-base`          | X          |        |
| `openssl-config`                 | X          |        |
| `wolfi-baselayout`               | X          | X      |
| `zlib`                           | X          |        |

