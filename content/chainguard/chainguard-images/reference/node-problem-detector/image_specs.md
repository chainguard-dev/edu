---
title: "Node-problem-detector Public Image Variants"
type: "article"
description: "Detailed information about the public Node-problem-detector Chainguard Image variants"
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

This page shows detailed information about all public variants of the Chainguard **Node-problem-detector** Image.

## Variants Compared
The **node-problem-detector** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev                                                | latest                                                    |
|--------------|-----------------------------------------------------------|-----------------------------------------------------------|
| Default User | `root`                                                    | `root`                                                    |
| Entrypoint   | `/usr/bin/node-problem-detector`                          | `/usr/bin/node-problem-detector`                          |
| CMD          | `--config.system-log-monitor=/config/kernel-monitor.json` | `--config.system-log-monitor=/config/kernel-monitor.json` |
| Workdir      | not specified                                             | not specified                                             |
| Has apk?     | no                                                        | no                                                        |
| Has a shell? | yes                                                       | yes                                                       |

Check the [tags history page](/chainguard/chainguard-images/reference/node-problem-detector/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                | latest-dev | latest |
|--------------------------------|------------|--------|
| `busybox`                      | X          | X      |
| `ca-certificates-bundle`       | X          | X      |
| `glibc`                        | X          | X      |
| `glibc-locale-posix`           | X          | X      |
| `health-checker`               | X          | X      |
| `ld-linux`                     | X          | X      |
| `libblkid`                     | X          | X      |
| `libcap`                       | X          | X      |
| `libcrypt1`                    | X          | X      |
| `libfdisk`                     | X          | X      |
| `libmount`                     | X          | X      |
| `libsystemd`                   | X          | X      |
| `libuuid`                      | X          | X      |
| `log-counter`                  | X          | X      |
| `node-problem-detector`        | X          | X      |
| `node-problem-detector-compat` | X          | X      |
| `systemd`                      | X          | X      |
| `systemd-dev`                  | X          | X      |
| `wolfi-baselayout`             | X          | X      |
