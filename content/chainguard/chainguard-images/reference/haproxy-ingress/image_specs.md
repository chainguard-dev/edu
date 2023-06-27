---
title: "Haproxy-ingress Image Variants"
type: "article"
description: "Detailed information about the Haproxy-ingressChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Haproxy-ingress"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Haproxy-ingress** Image.

## Variants Compared
The **haproxy-ingress** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest                                    | latest-dev                                |
|--------------|-------------------------------------------|-------------------------------------------|
| Default User | `haproxy`                                 | `haproxy`                                 |
| Entrypoint   | `/usr/bin/dumb-init -- /usr/bin/start.sh` | `/usr/bin/dumb-init -- /usr/bin/start.sh` |
| CMD          | not specified                             | not specified                             |
| Workdir      | not specified                             | not specified                             |
| Has apk?     | no                                        | no                                        |
| Has a shell? | yes                                       | yes                                       |

Check the [tags history page](/chainguard/chainguard-images/reference/haproxy-ingress/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                          | latest | latest-dev |
|--------------------------|--------|------------|
| `ca-certificates-bundle` | X      | X          |
| `busybox`                | X      | X          |
| `haproxy-ingress`        | X      | X          |
| `haproxy-ingress-compat` | X      | X          |
| `wolfi-baselayout`       | X      | X          |
| `dumb-init`              | X      | X          |
| `haproxy`                | X      | X          |
| `lua-json4`              | X      | X          |
