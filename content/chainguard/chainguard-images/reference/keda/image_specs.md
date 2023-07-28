---
title: "Keda Image Variants"
type: "article"
description: "Detailed information about the Keda Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Keda"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Keda** Image.

## Variants Compared
The **keda** Chainguard Image currently has 6 public variants: 

- `latest.webhooks`
- `latest.webhooks-dev`
- `latest.controller`
- `latest.controller-dev`
- `latest.adapter`
- `latest.adapter-dev`

## Default Image Settings
`USER`:		`nonroot`

`WORKDIR`:	not specified

`ENTRYPOINT`:	`/usr/bin/keda-adapter --secure-port=6443 --logtostderr=true --v=0`

`CMD`:		not specified

The following table has additional information about each of these variants.

|              | latest.webhooks | latest.webhooks-dev | latest.controller | latest.controller-dev | latest.adapter | latest.adapter-dev |
|--------------|-----------------|---------------------|-------------------|-----------------------|----------------|--------------------|
| Has apk?     | no              | yes                 | no                | yes                   | no             | yes                |
| Has a shell? | yes             | yes                 | yes               | yes                   | yes            | yes                |

Check the [tags history page](/chainguard/chainguard-images/reference/keda/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                           | latest.webhooks | latest.webhooks-dev | latest.controller | latest.controller-dev | latest.adapter | latest.adapter-dev |
|---------------------------|-----------------|---------------------|-------------------|-----------------------|----------------|--------------------|
| `busybox`                 | X               | X                   | X                 | X                     | X              | X                  |
| `keda-admission-webhooks` | X               | X                   |                   |                       |                |                    |
| `keda-compat`             | X               | X                   | X                 | X                     | X              | X                  |
| `keda`                    |                 |                     | X                 | X                     |                |                    |
| `keda-adapter`            |                 |                     |                   |                       | X              | X                  |
