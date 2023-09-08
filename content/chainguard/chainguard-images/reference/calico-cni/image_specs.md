---
title: "calico-cni Image Variants"
type: "article"
description: "Detailed information about the public calico-cni Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "calico-cni"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **calico-cni** Image.

## Variants Compared
The **calico-cni** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest                 |
|--------------|------------------------|
| Default User | `0`                    |
| Entrypoint   | `/opt/cni/bin/install` |
| CMD          | not specified          |
| Workdir      | not specified          |
| Has apk?     | no                     |
| Has a shell? | no                     |

Check the [tags history page](/chainguard/chainguard-images/reference/calico-cni/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                 | latest |
|---------------------------------|--------|
| `ca-certificates-bundle`        | X      |
| `calico-cni`                    | X      |
| `calico-cni-compat`             | X      |
| `cni-plugins-bandwidth`         | X      |
| `cni-plugins-bandwidth-compat`  | X      |
| `cni-plugins-host-local`        | X      |
| `cni-plugins-host-local-compat` | X      |
| `cni-plugins-loopback`          | X      |
| `cni-plugins-loopback-compat`   | X      |
| `cni-plugins-portmap`           | X      |
| `cni-plugins-portmap-compat`    | X      |
| `cni-plugins-tuning`            | X      |
| `cni-plugins-tuning-compat`     | X      |
| `flannel-cni-plugin`            | X      |
| `flannel-cni-plugin-compat`     | X      |
| `wolfi-baselayout`              | X      |
