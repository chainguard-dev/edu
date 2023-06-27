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
The **git** Chainguard Image currently has 6 public variants: 

- `latest`
- `latest-dev`
- `latest-glibc`
- `latest-glibc-dev`
- `latest-root`
- `latest-glibc-root`

The table has detailed information about each of these variants.

|              | latest         | latest-dev     | latest-glibc   | latest-glibc-dev | latest-root    | latest-glibc-root |
|--------------|----------------|----------------|----------------|------------------|----------------|-------------------|
| Default User | `git`          | `git`          | `git`          | `git`            | `root`         | `root`            |
| Entrypoint   | `/usr/bin/git` | `/usr/bin/git` | `/usr/bin/git` | `/usr/bin/git`   | `/usr/bin/git` | `/usr/bin/git`    |
| CMD          | not specified  | not specified  | not specified  | not specified    | not specified  | not specified     |
| Workdir      | `/home/git`    | `/home/git`    | `/home/git`    | `/home/git`      | `/home/git`    | `/home/git`       |
| Has apk?     | no             | no             | no             | no               | no             | no                |
| Has a shell? | no             | no             | no             | no               | no             | no                |

Check the [tags history page](/chainguard/chainguard-images/reference/git/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                          | latest | latest-dev | latest-glibc | latest-glibc-dev | latest-root | latest-glibc-root |
|--------------------------|--------|------------|--------------|------------------|-------------|-------------------|
| `alpine-baselayout-data` | X      | X          |              |                  | X           |                   |
| `alpine-release`         | X      | X          |              |                  | X           |                   |
| `ca-certificates-bundle` | X      | X          | X            | X                | X           | X                 |
| `git`                    | X      | X          | X            | X                | X           | X                 |
| `git-lfs`                | X      | X          | X            | X                | X           | X                 |
| `openssh-client`         | X      | X          | X            | X                | X           | X                 |
| `wolfi-baselayout`       |        |            | X            | X                |             | X                 |
