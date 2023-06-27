---
title: "Argocd-repo-server Image Variants"
type: "article"
description: "Detailed information about the Argocd-repo-serverChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Argocd-repo-server"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Argocd-repo-server** Image.

## Variants Compared
The **argocd-repo-server** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest                              | latest-dev                          |
|--------------|-------------------------------------|-------------------------------------|
| Default User | `argocd`                            | `argocd`                            |
| Entrypoint   | `/usr/local/bin/argocd-repo-server` | `/usr/local/bin/argocd-repo-server` |
| CMD          | not specified                       | not specified                       |
| Workdir      | `/home/argocd`                      | `/home/argocd`                      |
| Has apk?     | no                                  | no                                  |
| Has a shell? | yes                                 | yes                                 |

Check the [tags history page](/chainguard/chainguard-images/reference/argocd-repo-server/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                          | latest | latest-dev |
|--------------------------|--------|------------|
| `ca-certificates-bundle` | X      | X          |
| `busybox`                | X      | X          |
| `wolfi-baselayout`       | X      | X          |
| `argo-cd-repo-server`    | X      | X          |
| `argo-cd-compat`         | X      | X          |
