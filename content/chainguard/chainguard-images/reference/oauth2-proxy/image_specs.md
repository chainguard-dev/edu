---
title: "Oauth2-proxy Image Variants"
type: "article"
description: "Detailed information about the Oauth2-proxy Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Oauth2-proxy"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Oauth2-proxy** Image.

## Variants Compared
The **oauth2-proxy** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest                  | latest-dev              |
|--------------|-------------------------|-------------------------|
| Default User | `oauth2-proxy`          | `oauth2-proxy`          |
| Entrypoint   | `/usr/bin/oauth2-proxy` | `/usr/bin/oauth2-proxy` |
| CMD          | not specified           | not specified           |
| Workdir      | not specified           | not specified           |
| Has apk?     | no                      | yes                     |
| Has a shell? | no                      | yes                     |

Check the [tags history page](/chainguard/chainguard-images/reference/oauth2-proxy/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                | latest | latest-dev |
|----------------|--------|------------|
| `oauth2-proxy` | X      | X          |
