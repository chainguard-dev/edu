---
title: "Ruby Image Variants"
type: "article"
description: "Detailed information about the RubyChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Ruby"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Ruby** Image.

## Variants Compared
The **ruby** Chainguard Image currently has 8 public variants: 

- `latest`
- `latest-dev`
- `3.2`
- `3.2-dev`
- `3.1`
- `3.1-dev`
- `3.0`
- `3.0-dev`

The table has detailed information about each of these variants.

|              | latest          | latest-dev      | 3.2             | 3.2-dev         | 3.1             | 3.1-dev         | 3.0             | 3.0-dev         |
|--------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|
| Default User | `nonroot`       | `nonroot`       | `nonroot`       | `nonroot`       | `nonroot`       | `nonroot`       | `nonroot`       | `nonroot`       |
| Entrypoint   | `/usr/bin/ruby` | `/usr/bin/ruby` | `/usr/bin/ruby` | `/usr/bin/ruby` | `/usr/bin/ruby` | `/usr/bin/ruby` | `/usr/bin/ruby` | `/usr/bin/ruby` |
| CMD          | `--version`     | `--version`     | `--version`     | `--version`     | `--version`     | `--version`     | `--version`     | `--version`     |
| Workdir      | `/work`         | `/work`         | `/work`         | `/work`         | `/work`         | `/work`         | `/work`         | `/work`         |
| Has apk?     | no              | yes             | no              | yes             | no              | yes             | no              | yes             |
| Has a shell? | no              | yes             | no              | yes             | no              | yes             | no              | yes             |

Check the [tags history page](/chainguard/chainguard-images/reference/ruby/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|            | latest | latest-dev | 3.2 | 3.2-dev | 3.1 | 3.1-dev | 3.0 | 3.0-dev |
|------------|--------|------------|-----|---------|-----|---------|-----|---------|
| `ruby-3.2` | X      | X          | X   | X       |     |         |     |         |
| `ruby-3.1` |        |            |     |         | X   | X       |     |         |
| `ruby-3.0` |        |            |     |         |     |         | X   | X       |
