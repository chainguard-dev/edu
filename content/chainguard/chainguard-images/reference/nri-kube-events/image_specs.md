---
title: "Nri-kube-events Image Variants"
type: "article"
description: "Detailed information about the Nri-kube-eventsChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Nri-kube-events"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Nri-kube-events** Image.

## Variants Compared
The **nri-kube-events** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest                                   | latest-dev                               |
|--------------|------------------------------------------|------------------------------------------|
| Default User | `nri-kube-events`                        | `nri-kube-events`                        |
| Entrypoint   | `/sbin/tini -- /usr/bin/nri-kube-events` | `/sbin/tini -- /usr/bin/nri-kube-events` |
| CMD          | not specified                            | not specified                            |
| Workdir      | not specified                            | not specified                            |
| Has apk?     | no                                       | no                                       |
| Has a shell? | yes                                      | yes                                      |

Check the [tags history page](/chainguard/chainguard-images/reference/nri-kube-events/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                            | latest | latest-dev |
|----------------------------|--------|------------|
| `ca-certificates-bundle`   | X      | X          |
| `busybox`                  | X      | X          |
| `newrelic-nri-kube-events` | X      | X          |
| `wolfi-baselayout`         | X      | X          |
| `bind-tools`               | X      | X          |
| `tini`                     | X      | X          |
