---
title: "Consul Image Variants"
type: "article"
description: "Detailed information about the Consul Chainguard Image variants"
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
The **consul** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest                          | latest-dev                      |
|--------------|---------------------------------|---------------------------------|
| Default User | `root`                          | `root`                          |
| Entrypoint   | `/usr/bin/docker-entrypoint.sh` | `/usr/bin/docker-entrypoint.sh` |
| CMD          | `agent -dev -client 0.0.0.0`    | `agent -dev -client 0.0.0.0`    |
| Workdir      | not specified                   | not specified                   |
| Has apk?     | no                              | yes                             |
| Has a shell? | yes                             | yes                             |

Check the [tags history page](/chainguard/chainguard-images/reference/consul/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                                | latest | latest-dev |
|--------------------------------|--------|------------|
| `consul`                       | X      | X          |
| `su-exec`                      | X      | X          |
| `busybox`                      | X      | X          |
| `consul-oci-entrypoint-compat` | X      | X          |
| `curl`                         | X      | X          |
