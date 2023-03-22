---
title: "ruby Image Variants"
type: "article"
description: "Detailed specs for ruby Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
images: []
menu:
  docs:
    parent: "ruby"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **ruby** Image.

## Variants Compared
The **ruby** Chainguard Image currently has 6 public variants: 

- `latest`
- `latest-dev`
- `3.1`
- `3.1-dev`
- `3.0`
- `3.0-dev`

The table has detailed information about each of these variants.

|              | latest         | latest-dev     | 3.1            | 3.1-dev        | 3.0            | 3.0-dev        |
|--------------|----------------|----------------|----------------|----------------|----------------|----------------|
| Default User | `nonroot`      | `nonroot`      | `nonroot`      | `nonroot`      | `nonroot`      | `nonroot`      |
| Entrypoint   | not specified  | not specified  | not specified  | not specified  | not specified  | not specified  |
| CMD          | `/usr/bin/irb` | `/usr/bin/irb` | `/usr/bin/irb` | `/usr/bin/irb` | `/usr/bin/irb` | `/usr/bin/irb` |
| Workdir      | `/work`        | `/work`        | `/work`        | `/work`        | `/work`        | `/work`        |
| Has apk?     | no             | yes            | no             | yes            | no             | yes            |
| Has a shell? | no             | yes            | no             | yes            | no             | yes            |

## Image Dependencies
The table shows package distribution across all variants.

|                          | latest | latest-dev | 3.1 | 3.1-dev | 3.0 | 3.0-dev |
|--------------------------|--------|------------|-----|---------|-----|---------|
| `wolfi-baselayout`       | X      | X          | X   | X       | X   | X       |
| `ca-certificates-bundle` | X      | X          | X   | X       | X   | X       |
| `ruby-3.2`               | X      | X          |     |         |     |         |
| `apk-tools`              |        | X          |     | X       |     | X       |
| `bash`                   |        | X          |     | X       |     | X       |
| `busybox`                |        | X          |     | X       |     | X       |
| `build-base`             |        | X          |     | X       |     | X       |
| `ruby3.2-bundler`        |        | X          |     |         |     |         |
| `ruby-3.2-dev`           |        | X          |     |         |     |         |
| `ruby-3.1`               |        |            | X   | X       |     |         |
| `ruby3.1-bundler`        |        |            |     | X       |     |         |
| `ruby-3.1-dev`           |        |            |     | X       |     |         |
| `ruby-3.0`               |        |            |     |         | X   | X       |
| `ruby3.0-bundler`        |        |            |     |         |     | X       |
| `ruby-3.0-dev`           |        |            |     |         |     | X       |
