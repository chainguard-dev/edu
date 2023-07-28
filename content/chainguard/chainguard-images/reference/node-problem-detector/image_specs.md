---
title: "Node-problem-detector Image Variants"
type: "article"
description: "Detailed information about the Node-problem-detector Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Node-problem-detector"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Node-problem-detector** Image.

## Variants Compared
The **node-problem-detector** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

## Default Image Settings
`USER`:		`root`

`WORKDIR`:	not specified

`ENTRYPOINT`:	`/usr/bin/node-problem-detector`

`CMD`:		`--config.system-log-monitor=/config/kernel-monitor.json`

The following table has additional information about each of these variants.

|              | latest | latest-dev |
|--------------|--------|------------|
| Has apk?     | no     | yes        |
| Has a shell? | no     | yes        |

Check the [tags history page](/chainguard/chainguard-images/reference/node-problem-detector/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                                | latest | latest-dev |
|--------------------------------|--------|------------|
| `node-problem-detector`        | X      | X          |
| `node-problem-detector-compat` | X      | X          |
| `health-checker`               | X      | X          |
| `log-counter`                  | X      | X          |
