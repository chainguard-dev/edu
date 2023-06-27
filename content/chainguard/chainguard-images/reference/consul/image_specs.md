---
title: "Consul Image Variants"
type: "article"
description: "Detailed information about the ConsulChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Consul"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Consul** Image.

## Variants Compared
The **consul** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest                          |
|--------------|---------------------------------|
| Default User | `root`                          |
| Entrypoint   | `/usr/bin/docker-entrypoint.sh` |
| CMD          | `agent -dev -client 0.0.0.0`    |
| Workdir      | not specified                   |
| Has apk?     | no                              |
| Has a shell? | yes                             |

Check the [tags history page](/chainguard/chainguard-images/reference/consul/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                                | latest |
|--------------------------------|--------|
| `ca-certificates-bundle`       | X      |
| `consul`                       | X      |
| `su-exec`                      | X      |
| `busybox`                      | X      |
| `consul-oci-entrypoint-compat` | X      |
| `curl`                         | X      |
