---
title: "newrelic-kube-events Image Variants"
type: "article"
description: "Detailed information about the public newrelic-kube-events Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "newrelic-kube-events"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **newrelic-kube-events** Image.

## Variants Compared
The **newrelic-kube-events** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest                                   |
|--------------|------------------------------------------|
| Default User | `65532`                                  |
| Entrypoint   | `/sbin/tini -- /usr/bin/nri-kube-events` |
| CMD          | not specified                            |
| Workdir      | not specified                            |
| Has apk?     | no                                       |
| Has a shell? | yes                                      |

Check the [tags history page](/chainguard/chainguard-images/reference/newrelic-kube-events/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                            | latest |
|----------------------------|--------|
| `busybox`                  | X      |
| `ca-certificates-bundle`   | X      |
| `glibc`                    | X      |
| `glibc-locale-posix`       | X      |
| `ld-linux`                 | X      |
| `libcrypt1`                | X      |
| `newrelic-nri-kube-events` | X      |
| `tini`                     | X      |
| `wolfi-baselayout`         | X      |
