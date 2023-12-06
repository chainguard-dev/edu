---
title: "kube-bench Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public kube-bench Chainguard Image variants"
date: 2023-12-06 17:47:48
lastmod: 2023-12-06 17:47:48
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/kube-bench/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/kube-bench/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/kube-bench/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kube-bench/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **kube-bench** Image.

## Variants Compared
The **kube-bench** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest                |
|--------------|-----------------------|
| Default User | `root`                |
| Entrypoint   | `/usr/bin/kube-bench` |
| CMD          | `help`                |
| Workdir      | `/etc/kube-bench`     |
| Has apk?     | no                    |
| Has a shell? | no                    |

Check the [tags history page](/chainguard/chainguard-images/reference/kube-bench/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest |
|--------------------------|--------|
| `ca-certificates-bundle` | X      |
| `glibc`                  | X      |
| `glibc-locale-posix`     | X      |
| `kube-bench`             | X      |
| `kube-bench-configs`     | X      |
| `kubectl-1.28`           | X      |
| `ld-linux`               | X      |
| `libproc-2-0`            | X      |
| `ncurses`                | X      |
| `ncurses-terminfo-base`  | X      |
| `procps`                 | X      |
| `wolfi-baselayout`       | X      |

