---
title: "Argocd Image Variants"
type: "article"
description: "Detailed information about the Argocd Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Argocd"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Argocd** Image.

## Variants Compared
The **argocd** Chainguard Image currently has 4 public variants: 

- `latest.repo-server`
- `latest.repo-server-dev`
- `latest.argocd`
- `latest.argocd-dev`

The table has detailed information about each of these variants.

|              | latest.repo-server                  | latest.repo-server-dev              | latest.argocd  | latest.argocd-dev |
|--------------|-------------------------------------|-------------------------------------|----------------|-------------------|
| Default User | `argocd`                            | `argocd`                            | `argocd`       | `argocd`          |
| Entrypoint   | `/usr/local/bin/argocd-repo-server` | `/usr/local/bin/argocd-repo-server` | not specified  | not specified     |
| CMD          | not specified                       | not specified                       | not specified  | not specified     |
| Workdir      | `/home/argocd`                      | `/home/argocd`                      | `/home/argocd` | `/home/argocd`    |
| Has apk?     | no                                  | yes                                 | no             | yes               |
| Has a shell? | yes                                 | yes                                 | yes            | yes               |

Check the [tags history page](/chainguard/chainguard-images/reference/argocd/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                       | latest.repo-server | latest.repo-server-dev | latest.argocd | latest.argocd-dev |
|-----------------------|--------------------|------------------------|---------------|-------------------|
| `busybox`             | X                  | X                      | X             | X                 |
| `argo-cd-repo-server` | X                  | X                      |               |                   |
| `argo-cd-compat`      | X                  | X                      | X             | X                 |
| `argo-cd`             |                    |                        | X             | X                 |
