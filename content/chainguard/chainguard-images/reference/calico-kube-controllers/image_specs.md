---
title: "Calico-kube-controllers Public Image Variants"
type: "article"
description: "Detailed information about the public Calico-kube-controllers Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Calico-kube-controllers"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **Calico-kube-controllers** Image.

## Variants Compared
The **calico-kube-controllers** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest                             |
|--------------|------------------------------------|
| Default User | `nonroot`                          |
| Entrypoint   | `/usr/bin/calico-kube-controllers` |
| CMD          | not specified                      |
| Workdir      | not specified                      |
| Has apk?     | no                                 |
| Has a shell? | no                                 |

Check the [tags history page](/chainguard/chainguard-images/reference/calico-kube-controllers/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                           | latest |
|---------------------------|--------|
| `ca-certificates-bundle`  | X      |
| `calico-kube-controllers` | X      |
| `glibc`                   | X      |
| `glibc-dev`               | X      |
| `glibc-locale-posix`      | X      |
| `ld-linux`                | X      |
| `libcrypt1`               | X      |
| `linux-headers`           | X      |
| `nss-db`                  | X      |
| `nss-hesiod`              | X      |
| `wolfi-baselayout`        | X      |
