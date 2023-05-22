---
title: "newrelic-fluent-bit-output Image Variants"
type: "article"
description: "Detailed specs for newrelic-fluent-bit-output Chainguard Image Variants"
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

This page shows detailed information about all available variants of the Chainguard **newrelic-fluent-bit-output** Image.

## Variants Compared
The **newrelic-fluent-bit-output** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest                                                                  | latest-dev                                                              |
|--------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|
| Default User | `nonroot`                                                               | `nonroot`                                                               |
| Entrypoint   | `/usr/bin/fluent-bit`                                                   | `/usr/bin/fluent-bit`                                                   |
| CMD          | `-c /fluent-bit/etc/fluent-bit.conf -e /fluent-bit/bin/out_newrelic.so` | `-c /fluent-bit/etc/fluent-bit.conf -e /fluent-bit/bin/out_newrelic.so` |
| Workdir      | not specified                                                           | not specified                                                           |
| Has apk?     | no                                                                      | yes                                                                     |
| Has a shell? | no                                                                      | yes                                                                     |

## Image Dependencies
The table shows package distribution across all variants.

|                              | latest | latest-dev |
|------------------------------|--------|------------|
| `ca-certificates-bundle`     | X      | X          |
| `wolfi-baselayout`           | X      | X          |
| `newrelic-fluent-bit-output` | X      | X          |
| `fluent-bit`                 | X      | X          |
| `apk-tools`                  |        | X          |
| `bash`                       |        | X          |
| `busybox`                    |        | X          |
| `git`                        |        | X          |

