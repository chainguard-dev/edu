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
The **ruby** Chainguard Image currently has 3 public variants: 

- `latest`
- `3.1`
- `3.0`

The table has detailed information about each of these variants.

|              | latest         | 3.1            | 3.0            |
|--------------|----------------|----------------|----------------|
| Default User | `nonroot`      | `nonroot`      | `nonroot`      |
| Entrypoint   | not specified  | not specified  | not specified  |
| CMD          | `/usr/bin/irb` | `/usr/bin/irb` | `/usr/bin/irb` |
| Workdir      | `/work`        | `/work`        | `/work`        |
| Has apk?     | no             | no             | no             |
| Has a shell? | no             | no             | no             |

## Image Dependencies
The table shows package distribution across all variants.

|                          | latest | 3.1 | 3.0 |
|--------------------------|--------|-----|-----|
| `wolfi-baselayout`       | X      | X   | X   |
| `ca-certificates-bundle` | X      | X   | X   |
| `ruby-3.2`               | X      |     |     |
| `ruby-3.1`               |        | X   |     |
| `ruby-3.0`               |        |     | X   |
