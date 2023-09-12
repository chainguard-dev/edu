---
title: "argocd Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public argocd Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/argocd/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/argocd/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/argocd/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/argocd/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **argocd** Image.

## Variants Compared
The **argocd** Chainguard Image currently has 4 public variants: 

- `latest-dev`
- `latest`
- `repo-server-latest-dev`
- `repo-server-latest`

The table has detailed information about each of these variants.

|              | latest-dev     | latest         | repo-server-latest-dev              | repo-server-latest                  |
|--------------|----------------|----------------|-------------------------------------|-------------------------------------|
| Default User | `999`          | `999`          | `999`                               | `999`                               |
| Entrypoint   | not specified  | not specified  | `/usr/local/bin/argocd-repo-server` | `/usr/local/bin/argocd-repo-server` |
| CMD          | not specified  | not specified  | not specified                       | not specified                       |
| Workdir      | `/home/argocd` | `/home/argocd` | `/home/argocd`                      | `/home/argocd`                      |
| Has apk?     | yes            | no             | yes                                 | no                                  |
| Has a shell? | yes            | yes            | yes                                 | yes                                 |

Check the [tags history page](/chainguard/chainguard-images/reference/argocd/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                           | latest-dev | latest | repo-server-latest-dev | repo-server-latest |
|---------------------------|------------|--------|------------------------|--------------------|
| `apk-tools`               | X          |        | X                      |                    |
| `argo-cd-2.8`             | X          | X      |                        |                    |
| `argo-cd-2.8-compat`      | X          | X      | X                      | X                  |
| `bash`                    | X          |        | X                      |                    |
| `busybox`                 | X          | X      | X                      | X                  |
| `ca-certificates-bundle`  | X          | X      | X                      | X                  |
| `git`                     | X          |        | X                      | X                  |
| `glibc`                   | X          | X      | X                      | X                  |
| `glibc-locale-posix`      | X          | X      | X                      | X                  |
| `ld-linux`                | X          | X      | X                      | X                  |
| `libbrotlicommon1`        | X          |        | X                      | X                  |
| `libbrotlidec1`           | X          |        | X                      | X                  |
| `libcrypt1`               | X          | X      | X                      | X                  |
| `libcrypto3`              | X          |        | X                      | X                  |
| `libcurl-openssl4`        | X          |        | X                      | X                  |
| `libexpat1`               | X          |        | X                      | X                  |
| `libnghttp2-14`           | X          |        | X                      | X                  |
| `libpcre2-8-0`            | X          |        | X                      | X                  |
| `libssl3`                 | X          |        | X                      | X                  |
| `ncurses`                 | X          |        | X                      |                    |
| `ncurses-terminfo-base`   | X          |        | X                      |                    |
| `openssl-config`          | X          |        | X                      | X                  |
| `wolfi-baselayout`        | X          | X      | X                      | X                  |
| `zlib`                    | X          |        | X                      | X                  |
| `argo-cd-2.8-repo-server` |            |        | X                      | X                  |
| `git-lfs`                 |            |        | X                      | X                  |
| `gnupg`                   |            |        | X                      | X                  |
| `gnupg-gpgconf`           |            |        | X                      | X                  |
| `gpg`                     |            |        | X                      | X                  |
| `gpg-agent`               |            |        | X                      | X                  |
| `helm`                    |            |        | X                      | X                  |
| `kustomize`               |            |        | X                      | X                  |
| `libassuan`               |            |        | X                      | X                  |
| `libbz2-1`                |            |        | X                      | X                  |
| `libgcrypt`               |            |        | X                      | X                  |
| `libgpg-error`            |            |        | X                      | X                  |
| `npth`                    |            |        | X                      | X                  |
| `openssh-keygen`          |            |        | X                      | X                  |
| `openssh-server`          |            |        | X                      | X                  |
| `sqlite-libs`             |            |        | X                      | X                  |
| `tzdata`                  |            |        | X                      | X                  |

