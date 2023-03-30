---
title: "fluentd Image Variants"
type: "article"
description: "Detailed specs for fluentd Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "fluentd"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **fluentd** Image.

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
| Has apk?     | no             | yes            | no             | yes            |
| Has a shell? | no             | yes            | no             | yes            |

## Image Dependencies
The table shows package distribution across all variants.

|                          | latest | latest-dev | edge | edge-dev |
|--------------------------|--------|------------|------|----------|
| `wolfi-baselayout`       | X      | X          | X    | X        |
| `ca-certificates-bundle` | X      | X          | X    | X        |
| `ruby3.2-fluentd14`      | X      | X          |      |          |
| `apk-tools`              |        | X          |      | X        |
| `bash`                   |        | X          |      | X        |
| `busybox`                |        | X          |      | X        |
| `git`                    |        | X          |      | X        |
| `build-base`             |        | X          |      | X        |
| `ruby3.2-bundler`        |        | X          |      | X        |
| `ruby-3.2-dev`           |        | X          |      | X        |
| `glibc`                  |        |            | X    | X        |
| `ruby3.2-fluentd15`      |        |            | X    | X        |

