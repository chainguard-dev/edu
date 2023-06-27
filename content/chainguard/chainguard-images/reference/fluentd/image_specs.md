---
title: "Fluentd Image Variants"
type: "article"
description: "Detailed information about the FluentdChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Fluentd"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Fluentd** Image.

## Variants Compared
The **fluentd** Chainguard Image currently has 4 public variants: 

- `latest`
- `latest-dev`
- `edge`
- `edge-dev`

The table has detailed information about each of these variants.

|              | latest         | latest-dev     | edge           | edge-dev       |
|--------------|----------------|----------------|----------------|----------------|
| Default User | `fluent`       | `fluent`       | `fluent`       | `fluent`       |
| Entrypoint   | Service Bundle | Service Bundle | Service Bundle | Service Bundle |
| CMD          | not specified  | not specified  | not specified  | not specified  |
| Workdir      | not specified  | not specified  | not specified  | not specified  |
| Has apk?     | no             | no             | no             | no             |
| Has a shell? | no             | no             | no             | no             |

Check the [tags history page](/chainguard/chainguard-images/reference/fluentd/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                          | latest | latest-dev | edge | edge-dev |
|--------------------------|--------|------------|------|----------|
| `ca-certificates-bundle` | X      | X          | X    | X        |
| `ruby3.2-fluentd14`      | X      | X          |      |          |
| `wolfi-baselayout`       | X      | X          | X    | X        |
| `build-base`             |        | X          |      | X        |
| `ruby3.2-bundler`        |        | X          |      | X        |
| `ruby-3.2-dev`           |        | X          |      | X        |
| `glibc`                  |        |            | X    | X        |
| `ruby3.2-fluentd15`      |        |            | X    | X        |
