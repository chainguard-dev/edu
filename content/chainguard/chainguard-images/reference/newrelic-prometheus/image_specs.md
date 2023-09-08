---
title: "newrelic-prometheus Image Variants"
type: "article"
description: "Detailed information about the public newrelic-prometheus Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "newrelic-prometheus"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **newrelic-prometheus** Image.

## Variants Compared
The **newrelic-prometheus** Chainguard Image currently has 2 public variants: 

- `configurator-latest`
- `latest`

The table has detailed information about each of these variants.

|              | configurator-latest                | latest                                  |
|--------------|------------------------------------|-----------------------------------------|
| Default User | `65532`                            | `65532`                                 |
| Entrypoint   | `/usr/bin/prometheus-configurator` | `/sbin/tini -- /usr/bin/nri-prometheus` |
| CMD          | not specified                      | not specified                           |
| Workdir      | not specified                      | not specified                           |
| Has apk?     | no                                 | no                                      |
| Has a shell? | no                                 | yes                                     |

Check the [tags history page](/chainguard/chainguard-images/reference/newrelic-prometheus/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                    | configurator-latest | latest |
|------------------------------------|---------------------|--------|
| `ca-certificates-bundle`           | X                   | X      |
| `newrelic-prometheus-configurator` | X                   |        |
| `wolfi-baselayout`                 | X                   | X      |
| `busybox`                          |                     | X      |
| `glibc`                            |                     | X      |
| `glibc-locale-posix`               |                     | X      |
| `ld-linux`                         |                     | X      |
| `libcrypt1`                        |                     | X      |
| `nri-prometheus`                   |                     | X      |
| `tini`                             |                     | X      |
