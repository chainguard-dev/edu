---
title: "Helm Public Image Variants"
type: "article"
description: "Detailed information about the public Helm Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Helm"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **Helm** Image.

## Variants Compared
The **helm** Chainguard Image currently has 6 public variants: 

- `chartmuseum-latest-dev`
- `chartmuseum-latest`
- `controller-latest-dev`
- `controller-latest`
- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | chartmuseum-latest-dev | chartmuseum-latest     | controller-latest-dev      | controller-latest          | latest-dev      | latest          |
|--------------|------------------------|------------------------|----------------------------|----------------------------|-----------------|-----------------|
| Default User | `nonroot`              | `nonroot`              | `nonroot`                  | `nonroot`                  | `nonroot`       | `nonroot`       |
| Entrypoint   | `/usr/bin/chartmuseum` | `/usr/bin/chartmuseum` | `/usr/bin/helm-controller` | `/usr/bin/helm-controller` | `/usr/bin/helm` | `/usr/bin/helm` |
| CMD          | not specified          | not specified          | not specified              | not specified              | `help`          | `help`          |
| Workdir      | not specified          | not specified          | not specified              | not specified              | not specified   | not specified   |
| Has apk?     | yes                    | no                     | yes                        | no                         | yes             | no              |
| Has a shell? | yes                    | no                     | yes                        | no                         | yes             | no              |

Check the [tags history page](/chainguard/chainguard-images/reference/helm/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | chartmuseum-latest-dev | chartmuseum-latest | controller-latest-dev | controller-latest | latest-dev | latest |
|--------------------------|------------------------|--------------------|-----------------------|-------------------|------------|--------|
| `apk-tools`              | X                      |                    | X                     |                   | X          |        |
| `bash`                   | X                      |                    | X                     |                   | X          |        |
| `busybox`                | X                      |                    | X                     |                   | X          |        |
| `ca-certificates-bundle` | X                      | X                  | X                     | X                 | X          | X      |
| `chartmuseum`            | X                      | X                  |                       |                   |            |        |
| `git`                    | X                      |                    | X                     |                   | X          |        |
| `glibc`                  | X                      |                    | X                     |                   | X          |        |
| `glibc-locale-posix`     | X                      |                    | X                     | X                 | X          |        |
| `ld-linux`               | X                      |                    | X                     |                   | X          |        |
| `libbrotlicommon1`       | X                      |                    | X                     |                   | X          |        |
| `libbrotlidec1`          | X                      |                    | X                     |                   | X          |        |
| `libcrypt1`              | X                      |                    |                       |                   | X          |        |
| `libcrypto3`             | X                      |                    | X                     |                   | X          |        |
| `libcurl-openssl4`       | X                      |                    | X                     |                   | X          |        |
| `libexpat1`              | X                      |                    |                       |                   | X          |        |
| `libnghttp2-14`          | X                      |                    | X                     |                   | X          |        |
| `libpcre2-8-0`           | X                      |                    | X                     |                   | X          |        |
| `libssl3`                | X                      |                    | X                     |                   | X          |        |
| `ncurses`                | X                      |                    | X                     |                   | X          |        |
| `ncurses-terminfo-base`  | X                      |                    | X                     |                   | X          |        |
| `openssl-config`         | X                      |                    | X                     |                   | X          |        |
| `wolfi-baselayout`       | X                      | X                  | X                     | X                 | X          | X      |
| `zlib`                   | X                      |                    | X                     |                   | X          |        |
| `expat`                  |                        |                    | X                     |                   |            |        |
| `flux-helm-controller`   |                        |                    | X                     | X                 |            |        |
| `helm`                   |                        |                    |                       |                   | X          | X      |
| `kubectl`                |                        |                    |                       |                   | X          | X      |
