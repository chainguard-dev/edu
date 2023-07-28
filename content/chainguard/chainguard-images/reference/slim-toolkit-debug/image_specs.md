---
title: "Slim-toolkit-debug Image Variants"
type: "article"
description: "Detailed information about the Slim-toolkit-debug Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Slim-toolkit-debug"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Slim-toolkit-debug** Image.

## Variants Compared
The **slim-toolkit-debug** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

## Default Image Settings
`USER`:		`root`

`WORKDIR`:	not specified

`ENTRYPOINT`:	`/bin/bash -c`

`CMD`:		not specified

The following table has additional information about each of these variants.

|              | latest | latest-dev |
|--------------|--------|------------|
| Has apk?     | no     | yes        |
| Has a shell? | yes    | yes        |

Check the [tags history page](/chainguard/chainguard-images/reference/slim-toolkit-debug/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                 | latest | latest-dev |
|-----------------|--------|------------|
| `curl`          | X      | X          |
| `bash`          | X      | X          |
| `busybox`       | X      | X          |
| `git`           | X      | X          |
| `grpcurl`       | X      | X          |
| `drill`         | X      | X          |
| `nmap`          | X      | X          |
| `dhcping`       | X      | X          |
| `tcptraceroute` | X      | X          |
| `bind-tools`    | X      | X          |
| `net-tools`     | X      | X          |
| `iproute2`      | X      | X          |
| `socat`         | X      | X          |
| `openssl`       | X      | X          |
| `gperf`         | X      | X          |
| `jq`            | X      | X          |
| `yq`            | X      | X          |
| `strace`        | X      | X          |
| `redis`         | X      | X          |
| `oras`          | X      | X          |
| `crane`         | X      | X          |
| `fatrace`       | X      | X          |
| `ngrep`         | X      | X          |
| `sysstat`       | X      | X          |
| `ltrace`        | X      | X          |
| `dstat`         | X      | X          |
| `mycli`         | X      | X          |
| `py3-pgcli`     | X      | X          |
