---
title: "Guacamole-server Image Variants"
type: "article"
description: "Detailed information about the Guacamole-serverChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Guacamole-server"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Guacamole-server** Image.

## Variants Compared
The **guacamole-server** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest                                                            | latest-dev                                                        |
|--------------|-------------------------------------------------------------------|-------------------------------------------------------------------|
| Default User | ``                                                                | ``                                                                |
| Entrypoint   | not specified                                                     | not specified                                                     |
| CMD          | `/bin/sh -c '/usr/sbin/guacd  -b 0.0.0.0 -L $GUACD_LOG_LEVEL -f'` | `/bin/sh -c '/usr/sbin/guacd  -b 0.0.0.0 -L $GUACD_LOG_LEVEL -f'` |
| Workdir      | not specified                                                     | not specified                                                     |
| Has apk?     | no                                                                | yes                                                               |
| Has a shell? | yes                                                               | yes                                                               |

Check the [tags history page](/chainguard/chainguard-images/reference/guacamole-server/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                           | latest | latest-dev |
|---------------------------|--------|------------|
| `guacamole-server`        | X      | X          |
| `busybox`                 | X      | X          |
| `ttf-dejavu`              | X      | X          |
| `netcat-openbsd`          | X      | X          |
| `libguac-client-vnc`      | X      | X          |
| `libguac-client-telnet`   | X      | X          |
| `libguac-client-ssh`      | X      | X          |
| `libguac-client-rdp`      | X      | X          |
| `openssl-provider-legacy` | X      | X          |
