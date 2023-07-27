---
title: "Git Image Variants"
type: "article"
description: "Detailed information about the GitChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Git"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Git** Image.

## Variants Compared
The **git** Chainguard Image currently has 8 public variants: 

- `latest.wolfi.root`
- `latest.wolfi.root-dev`
- `latest.wolfi.nonroot`
- `latest.wolfi.nonroot-dev`
- `latest.alpine.root`
- `latest.alpine.root-dev`
- `latest.alpine.nonroot`
- `latest.alpine.nonroot-dev`

The table has detailed information about each of these variants.

|              | latest.wolfi.root | latest.wolfi.root-dev | latest.wolfi.nonroot | latest.wolfi.nonroot-dev | latest.alpine.root | latest.alpine.root-dev | latest.alpine.nonroot | latest.alpine.nonroot-dev |
|--------------|-------------------|-----------------------|----------------------|--------------------------|--------------------|------------------------|-----------------------|---------------------------|
| Default User | `root`            | `root`                | `git`                | `git`                    | `root`             | `root`                 | `git`                 | `git`                     |
| Entrypoint   | `/usr/bin/git`    | `/usr/bin/git`        | `/usr/bin/git`       | `/usr/bin/git`           | `/usr/bin/git`     | `/usr/bin/git`         | `/usr/bin/git`        | `/usr/bin/git`            |
| CMD          | not specified     | not specified         | not specified        | not specified            | not specified      | not specified          | not specified         | not specified             |
| Workdir      | `/home/git`       | `/home/git`           | `/home/git`          | `/home/git`              | `/home/git`        | `/home/git`            | `/home/git`           | `/home/git`               |
| Has apk?     | no                | yes                   | no                   | yes                      | no                 | yes                    | no                    | yes                       |
| Has a shell? | no                | yes                   | no                   | yes                      | no                 | yes                    | no                    | yes                       |

Check the [tags history page](/chainguard/chainguard-images/reference/git/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                  | latest.wolfi.root | latest.wolfi.root-dev | latest.wolfi.nonroot | latest.wolfi.nonroot-dev | latest.alpine.root | latest.alpine.root-dev | latest.alpine.nonroot | latest.alpine.nonroot-dev |
|------------------|-------------------|-----------------------|----------------------|--------------------------|--------------------|------------------------|-----------------------|---------------------------|
| `git`            | X                 | X                     | X                    | X                        | X                  | X                      | X                     | X                         |
| `git-lfs`        | X                 | X                     | X                    | X                        | X                  | X                      | X                     | X                         |
| `openssh-client` | X                 | X                     | X                    | X                        | X                  | X                      | X                     | X                         |
