---
title: "Newrelic-fluent-bit-output Image Variants"
type: "article"
description: "Detailed information about the Newrelic-fluent-bit-outputChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Newrelic-fluent-bit-output"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Newrelic-fluent-bit-output** Image.

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
| Has apk?     | no                                                                      | no                                                                      |
| Has a shell? | no                                                                      | no                                                                      |

Check the [tags history page](/chainguard/chainguard-images/reference/newrelic-fluent-bit-output/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                              | latest | latest-dev |
|------------------------------|--------|------------|
| `ca-certificates-bundle`     | X      | X          |
| `wolfi-baselayout`           | X      | X          |
| `newrelic-fluent-bit-output` | X      | X          |
| `fluent-bit`                 | X      | X          |
