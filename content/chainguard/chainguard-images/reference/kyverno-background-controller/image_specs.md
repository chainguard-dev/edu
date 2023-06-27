---
title: "Kyverno-background-controller Image Variants"
type: "article"
description: "Detailed information about the Kyverno-background-controllerChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Kyverno-background-controller"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Kyverno-background-controller** Image.

## Variants Compared
The **kyverno-background-controller** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest                           |
|--------------|----------------------------------|
| Default User | `nonroot`                        |
| Entrypoint   | `/usr/bin/background-controller` |
| CMD          | `help`                           |
| Workdir      | not specified                    |
| Has apk?     | no                               |
| Has a shell? | no                               |

Check the [tags history page](/chainguard/chainguard-images/reference/kyverno-background-controller/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                                 | latest |
|---------------------------------|--------|
| `ca-certificates-bundle`        | X      |
| `kyverno-background-controller` | X      |
| `wolfi-baselayout`              | X      |
| `kubectl`                       | X      |
