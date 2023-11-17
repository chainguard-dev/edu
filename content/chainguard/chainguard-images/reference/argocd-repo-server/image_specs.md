---
title: "argocd-repo-server Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public argocd-repo-server Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/argocd-repo-server/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/argocd-repo-server/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/argocd-repo-server/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/argocd-repo-server/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **argocd-repo-server** Image.

## Variants Compared
The **argocd-repo-server** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev                          | latest                              |
|--------------|-------------------------------------|-------------------------------------|
| Default User | `argocd`                            | `argocd`                            |
| Entrypoint   | `/usr/local/bin/argocd-repo-server` | `/usr/local/bin/argocd-repo-server` |
| CMD          | not specified                       | not specified                       |
| Workdir      | `/home/argocd`                      | `/home/argocd`                      |
| Has apk?     | yes                                 | no                                  |
| Has a shell? | yes                                 | yes                                 |

Check the [tags history page](/chainguard/chainguard-images/reference/argocd-repo-server/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                           | latest-dev | latest |
|---------------------------|------------|--------|
| `apk-tools`               | X          |        |
| `argo-cd-2.9-compat`      | X          | X      |
| `argo-cd-2.9-repo-server` | X          | X      |
| `bash`                    | X          |        |
| `busybox`                 | X          | X      |
| `ca-certificates-bundle`  | X          | X      |
| `git`                     | X          | X      |
| `git-lfs`                 | X          | X      |
| `glibc`                   | X          | X      |
| `glibc-locale-posix`      | X          | X      |
| `gnupg`                   | X          | X      |
| `gnupg-gpgconf`           | X          | X      |
| `gpg`                     | X          | X      |
| `gpg-agent`               | X          | X      |
| `helm`                    | X          | X      |
| `kustomize`               | X          | X      |
| `ld-linux`                | X          | X      |
| `libassuan`               | X          | X      |
| `libbrotlicommon1`        | X          | X      |
| `libbrotlidec1`           | X          | X      |
| `libbz2-1`                | X          | X      |
| `libcrypt1`               | X          | X      |
| `libcrypto3`              | X          | X      |
| `libcurl-openssl4`        | X          | X      |
| `libedit`                 | X          | X      |
| `libexpat1`               | X          | X      |
| `libgcrypt`               | X          | X      |
| `libgpg-error`            | X          | X      |
| `libnghttp2-14`           | X          | X      |
| `libpcre2-8-0`            | X          | X      |
| `libssl3`                 | X          | X      |
| `ncurses`                 | X          | X      |
| `ncurses-terminfo-base`   | X          | X      |
| `npth`                    | X          | X      |
| `openssh`                 | X          | X      |
| `openssh-client`          | X          | X      |
| `openssh-keygen`          | X          | X      |
| `openssh-server`          | X          | X      |
| `openssh-server-config`   | X          | X      |
| `openssh-sftp-server`     | X          | X      |
| `openssl-config`          | X          | X      |
| `sqlite-libs`             | X          | X      |
| `tzdata`                  | X          | X      |
| `wolfi-baselayout`        | X          | X      |
| `zlib`                    | X          | X      |

