---
title: "Spire-agent Image Variants"
type: "article"
description: "Detailed information about the Spire-agentChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Spire-agent"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Spire-agent** Image.

## Variants Compared
The **spire-agent** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest                     | latest-dev                 |
|--------------|----------------------------|----------------------------|
| Default User | `root`                     | `root`                     |
| Entrypoint   | `/usr/bin/spire-agent run` | `/usr/bin/spire-agent run` |
| CMD          | not specified              | not specified              |
| Workdir      | not specified              | not specified              |
| Has apk?     | no                         | no                         |
| Has a shell? | yes                        | yes                        |

Check the [tags history page](/chainguard/chainguard-images/reference/spire-agent/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                          | latest | latest-dev |
|--------------------------|--------|------------|
| `wolfi-baselayout`       | X      | X          |
| `ca-certificates-bundle` | X      | X          |
| `spire-agent`            | X      | X          |
| `busybox`                | X      | X          |
| `libcap-utils`           | X      | X          |
