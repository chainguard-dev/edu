---
title: "kubernetes-dashboard Image Variants"
type: "article"
description: "Detailed information about the public kubernetes-dashboard Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "kubernetes-dashboard"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **kubernetes-dashboard** Image.

## Variants Compared
The **kubernetes-dashboard** Chainguard Image currently has 4 public variants: 

- `latest-dev`
- `latest`
- `metrics-scraper-latest-dev`
- `metrics-scraper-latest`

The table has detailed information about each of these variants.

|              | latest-dev                                                                                         | latest                                                                                             | metrics-scraper-latest-dev | metrics-scraper-latest     |
|--------------|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|----------------------------|----------------------------|
| Default User | `nonroot`                                                                                          | `nonroot`                                                                                          | `nonroot`                  | `nonroot`                  |
| Entrypoint   | `/usr/share/kubernetes-dashboard/dashboard --insecure-bind-address=0.0.0.0 --bind-address=0.0.0.0` | `/usr/share/kubernetes-dashboard/dashboard --insecure-bind-address=0.0.0.0 --bind-address=0.0.0.0` | `/usr/bin/metrics-sidecar` | `/usr/bin/metrics-sidecar` |
| CMD          | not specified                                                                                      | not specified                                                                                      | not specified              | not specified              |
| Workdir      | not specified                                                                                      | not specified                                                                                      | not specified              | not specified              |
| Has apk?     | yes                                                                                                | no                                                                                                 | yes                        | no                         |
| Has a shell? | yes                                                                                                | no                                                                                                 | yes                        | no                         |

Check the [tags history page](/chainguard/chainguard-images/reference/kubernetes-dashboard/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                        | latest-dev | latest | metrics-scraper-latest-dev | metrics-scraper-latest |
|----------------------------------------|------------|--------|----------------------------|------------------------|
| `apk-tools`                            | X          |        | X                          |                        |
| `bash`                                 | X          |        | X                          |                        |
| `busybox`                              | X          |        | X                          |                        |
| `ca-certificates-bundle`               | X          | X      | X                          | X                      |
| `git`                                  | X          |        | X                          |                        |
| `glibc`                                | X          |        | X                          |                        |
| `glibc-locale-posix`                   | X          |        | X                          |                        |
| `kubernetes-dashboard`                 | X          | X      |                            |                        |
| `ld-linux`                             | X          |        | X                          |                        |
| `libbrotlicommon1`                     | X          |        | X                          |                        |
| `libbrotlidec1`                        | X          |        | X                          |                        |
| `libcrypt1`                            | X          |        | X                          |                        |
| `libcrypto3`                           | X          |        | X                          |                        |
| `libcurl-openssl4`                     | X          |        | X                          |                        |
| `libexpat1`                            | X          |        | X                          |                        |
| `libnghttp2-14`                        | X          |        | X                          |                        |
| `libpcre2-8-0`                         | X          |        | X                          |                        |
| `libssl3`                              | X          |        | X                          |                        |
| `ncurses`                              | X          |        | X                          |                        |
| `ncurses-terminfo-base`                | X          |        | X                          |                        |
| `openssl-config`                       | X          |        | X                          |                        |
| `wolfi-baselayout`                     | X          | X      | X                          | X                      |
| `zlib`                                 | X          |        | X                          |                        |
| `kubernetes-dashboard-metrics-scraper` |            |        | X                          | X                      |

