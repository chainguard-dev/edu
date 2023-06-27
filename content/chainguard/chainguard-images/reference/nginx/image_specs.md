---
title: "Nginx Image Variants"
type: "article"
description: "Detailed information about the NginxChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Nginx"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Nginx** Image.

## Variants Compared
The **nginx** Chainguard Image currently has 3 public variants: 

- `latest`
- `latest-dev`
- `next`

The table has detailed information about each of these variants.

|              | latest                                                     | latest-dev                                                 | next                                                       |
|--------------|------------------------------------------------------------|------------------------------------------------------------|------------------------------------------------------------|
| Default User | `nginx`                                                    | `nginx`                                                    | `nginx`                                                    |
| Entrypoint   | `/usr/sbin/nginx`                                          | `/usr/sbin/nginx`                                          | `/usr/sbin/nginx`                                          |
| CMD          | `-c /etc/nginx/nginx.conf -e /dev/stderr -g "daemon off;"` | `-c /etc/nginx/nginx.conf -e /dev/stderr -g "daemon off;"` | `-c /etc/nginx/nginx.conf -e /dev/stderr -g "daemon off;"` |
| Workdir      | not specified                                              | not specified                                              | not specified                                              |
| Has apk?     | no                                                         | no                                                         | no                                                         |
| Has a shell? | no                                                         | no                                                         | no                                                         |

Check the [tags history page](/chainguard/chainguard-images/reference/nginx/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                          | latest | latest-dev | next |
|--------------------------|--------|------------|------|
| `ca-certificates-bundle` | X      | X          | X    |
| `wolfi-baselayout`       | X      | X          | X    |
| `nginx`                  | X      | X          | X    |
| `nginx-package-config`   | X      | X          | X    |
