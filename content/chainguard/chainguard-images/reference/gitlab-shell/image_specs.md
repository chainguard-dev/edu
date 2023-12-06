---
title: "gitlab-shell Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public gitlab-shell Chainguard Image variants"
date: 2023-12-06 17:47:48
lastmod: 2023-12-06 17:47:48
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/gitlab-shell/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/gitlab-shell/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/gitlab-shell/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/gitlab-shell/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **gitlab-shell** Image.

## Variants Compared
The **gitlab-shell** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev                                        | latest                                            |
|--------------|---------------------------------------------------|---------------------------------------------------|
| Default User | `nonroot`                                         | `nonroot`                                         |
| Entrypoint   | `/scripts/entrypoint.sh /scripts/process-wrapper` | `/scripts/entrypoint.sh /scripts/process-wrapper` |
| CMD          | not specified                                     | not specified                                     |
| Workdir      | not specified                                     | not specified                                     |
| Has apk?     | yes                                               | no                                                |
| Has a shell? | yes                                               | yes                                               |

Check the [tags history page](/chainguard/chainguard-images/reference/gitlab-shell/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                            | latest-dev | latest |
|----------------------------|------------|--------|
| `apk-tools`                | X          |        |
| `bash`                     | X          | X      |
| `busybox`                  | X          | X      |
| `ca-certificates-bundle`   | X          | X      |
| `curl`                     | X          | X      |
| `git`                      | X          |        |
| `gitlab-cng-base`          | X          | X      |
| `gitlab-cng-shell-scripts` | X          | X      |
| `gitlab-logger`            | X          | X      |
| `gitlab-logger-compat`     | X          | X      |
| `gitlab-shell`             | X          | X      |
| `glibc`                    | X          | X      |
| `glibc-locale-posix`       | X          | X      |
| `gomplate`                 | X          | X      |
| `ld-linux`                 | X          | X      |
| `libbrotlicommon1`         | X          | X      |
| `libbrotlidec1`            | X          | X      |
| `libcrypt1`                | X          | X      |
| `libcrypto3`               | X          | X      |
| `libcurl-openssl4`         | X          | X      |
| `libedit`                  | X          | X      |
| `libexpat1`                | X          |        |
| `libnghttp2-14`            | X          | X      |
| `libpcre2-8-0`             | X          |        |
| `libproc-2-0`              | X          | X      |
| `libssl3`                  | X          | X      |
| `ncurses`                  | X          | X      |
| `ncurses-terminfo-base`    | X          | X      |
| `openssh`                  | X          | X      |
| `openssh-client`           | X          | X      |
| `openssh-keygen`           | X          | X      |
| `openssh-server`           | X          | X      |
| `openssh-server-config`    | X          | X      |
| `openssh-sftp-server`      | X          | X      |
| `openssl-config`           | X          | X      |
| `procps`                   | X          | X      |
| `wolfi-baselayout`         | X          | X      |
| `xtail`                    | X          | X      |
| `zlib`                     | X          | X      |

