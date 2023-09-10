---
title: "newrelic-fluent-bit-output Image Variants"
type: "article"
description: "Detailed information about the public newrelic-fluent-bit-output Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "newrelic-fluent-bit-output"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **newrelic-fluent-bit-output** Image.

## Variants Compared
The **newrelic-fluent-bit-output** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest                                                                  |
|--------------|-------------------------------------------------------------------------|
| Default User | `root`                                                                  |
| Entrypoint   | `/usr/bin/fluent-bit`                                                   |
| CMD          | `-c /fluent-bit/etc/fluent-bit.conf -e /fluent-bit/bin/out_newrelic.so` |
| Workdir      | not specified                                                           |
| Has apk?     | no                                                                      |
| Has a shell? | no                                                                      |

Check the [tags history page](/chainguard/chainguard-images/reference/newrelic-fluent-bit-output/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                     | latest |
|-------------------------------------|--------|
| `ca-certificates-bundle`            | X      |
| `fluent-bit`                        | X      |
| `glibc`                             | X      |
| `glibc-locale-posix`                | X      |
| `ld-linux`                          | X      |
| `libcap`                            | X      |
| `libcrypto3`                        | X      |
| `libgcc`                            | X      |
| `libpq-11`                          | X      |
| `libssl3`                           | X      |
| `libsystemd`                        | X      |
| `newrelic-fluent-bit-output`        | X      |
| `newrelic-fluent-bit-output-compat` | X      |
| `openssl-config`                    | X      |
| `wolfi-baselayout`                  | X      |
| `yaml`                              | X      |
| `zlib`                              | X      |

