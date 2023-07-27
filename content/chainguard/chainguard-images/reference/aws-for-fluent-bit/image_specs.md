---
title: "Aws-for-fluent-bit Image Variants"
type: "article"
description: "Detailed information about the Aws-for-fluent-bit Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Aws-for-fluent-bit"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Aws-for-fluent-bit** Image.

## Variants Compared
The **aws-for-fluent-bit** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest                                                                                                                 | latest-dev                                                                                                             |
|--------------|------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| Default User | `nonroot`                                                                                                              | `nonroot`                                                                                                              |
| Entrypoint   | `/fluent-bit/bin/fluent-bit`                                                                                           | `/fluent-bit/bin/fluent-bit`                                                                                           |
| CMD          | `-e /fluent-bit/firehose.so -e /fluent-bit/cloudwatch.so -e /fluent-bit/kinesis.so -c /fluent-bit/etc/fluent-bit.conf` | `-e /fluent-bit/firehose.so -e /fluent-bit/cloudwatch.so -e /fluent-bit/kinesis.so -c /fluent-bit/etc/fluent-bit.conf` |
| Workdir      | not specified                                                                                                          | not specified                                                                                                          |
| Has apk?     | no                                                                                                                     | yes                                                                                                                    |
| Has a shell? | no                                                                                                                     | yes                                                                                                                    |

Check the [tags history page](/chainguard/chainguard-images/reference/aws-for-fluent-bit/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                             | latest | latest-dev |
|-----------------------------|--------|------------|
| `aws-for-fluent-bit`        | X      | X          |
| `aws-for-fluent-bit-compat` | X      | X          |
