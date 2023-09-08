---
title: "keda Image Variants"
type: "article"
description: "Detailed information about the public keda Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "keda"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **keda** Image.

## Variants Compared
The **keda** Chainguard Image currently has 6 public variants: 

- `adapter-latest-dev`
- `adapter-latest`
- `admission-webhooks-latest-dev`
- `admission-webhooks-latest`
- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | adapter-latest-dev                                                  | adapter-latest                                                      | admission-webhooks-latest-dev                                                 | admission-webhooks-latest                                                     | latest-dev                                                 | latest                                                     |
|--------------|---------------------------------------------------------------------|---------------------------------------------------------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------|------------------------------------------------------------|------------------------------------------------------------|
| Default User | `65532`                                                             | `65532`                                                             | `65532`                                                                       | `65532`                                                                       | `65532`                                                    | `65532`                                                    |
| Entrypoint   | `/usr/bin/keda-adapter --secure-port=6443 --logtostderr=true --v=0` | `/usr/bin/keda-adapter --secure-port=6443 --logtostderr=true --v=0` | `/usr/bin/keda-admission-webhooks --zap-log-level=info --zap-encoder=console` | `/usr/bin/keda-admission-webhooks --zap-log-level=info --zap-encoder=console` | `/usr/bin/keda --zap-log-level=info --zap-encoder=console` | `/usr/bin/keda --zap-log-level=info --zap-encoder=console` |
| CMD          | not specified                                                       | not specified                                                       | not specified                                                                 | not specified                                                                 | not specified                                              | not specified                                              |
| Workdir      | not specified                                                       | not specified                                                       | not specified                                                                 | not specified                                                                 | not specified                                              | not specified                                              |
| Has apk?     | yes                                                                 | no                                                                  | yes                                                                           | no                                                                            | yes                                                        | no                                                         |
| Has a shell? | yes                                                                 | yes                                                                 | yes                                                                           | yes                                                                           | yes                                                        | yes                                                        |

Check the [tags history page](/chainguard/chainguard-images/reference/keda/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                           | adapter-latest-dev | adapter-latest | admission-webhooks-latest-dev | admission-webhooks-latest | latest-dev | latest |
|---------------------------|--------------------|----------------|-------------------------------|---------------------------|------------|--------|
| `apk-tools`               | X                  |                | X                             |                           | X          |        |
| `bash`                    | X                  |                | X                             |                           | X          |        |
| `busybox`                 | X                  | X              | X                             | X                         | X          | X      |
| `ca-certificates-bundle`  | X                  | X              | X                             | X                         | X          | X      |
| `git`                     | X                  |                | X                             |                           | X          |        |
| `glibc`                   | X                  | X              | X                             | X                         | X          | X      |
| `glibc-locale-posix`      | X                  | X              | X                             | X                         | X          | X      |
| `keda-adapter`            | X                  | X              |                               |                           |            |        |
| `keda-compat`             | X                  | X              | X                             | X                         | X          | X      |
| `ld-linux`                | X                  | X              | X                             | X                         | X          | X      |
| `libbrotlicommon1`        | X                  |                | X                             |                           | X          |        |
| `libbrotlidec1`           | X                  |                | X                             |                           | X          |        |
| `libcrypt1`               | X                  | X              | X                             | X                         | X          | X      |
| `libcrypto3`              | X                  |                | X                             |                           | X          |        |
| `libcurl-openssl4`        | X                  |                | X                             |                           | X          |        |
| `libexpat1`               | X                  |                | X                             |                           | X          |        |
| `libnghttp2-14`           | X                  |                | X                             |                           | X          |        |
| `libpcre2-8-0`            | X                  |                | X                             |                           | X          |        |
| `libssl3`                 | X                  |                | X                             |                           | X          |        |
| `ncurses`                 | X                  |                | X                             |                           | X          |        |
| `ncurses-terminfo-base`   | X                  |                | X                             |                           | X          |        |
| `openssl-config`          | X                  |                | X                             |                           | X          |        |
| `wolfi-baselayout`        | X                  | X              | X                             | X                         | X          | X      |
| `zlib`                    | X                  |                | X                             |                           | X          |        |
| `keda-admission-webhooks` |                    |                | X                             | X                         |            |        |
| `keda`                    |                    |                |                               |                           | X          | X      |
