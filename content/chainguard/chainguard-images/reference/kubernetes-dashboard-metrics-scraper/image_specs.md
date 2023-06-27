---
title: "Kubernetes-dashboard-metrics-scraper Image Variants"
type: "article"
description: "Detailed information about the Kubernetes-dashboard-metrics-scraperChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Kubernetes-dashboard-metrics-scraper"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Kubernetes-dashboard-metrics-scraper** Image.

## Variants Compared
The **kubernetes-dashboard-metrics-scraper** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest                     | latest-dev                 |
|--------------|----------------------------|----------------------------|
| Default User | `nonroot`                  | `nonroot`                  |
| Entrypoint   | `/usr/bin/metrics-sidecar` | `/usr/bin/metrics-sidecar` |
| CMD          | not specified              | not specified              |
| Workdir      | not specified              | not specified              |
| Has apk?     | no                         | no                         |
| Has a shell? | no                         | no                         |

Check the [tags history page](/chainguard/chainguard-images/reference/kubernetes-dashboard-metrics-scraper/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                                        | latest | latest-dev |
|----------------------------------------|--------|------------|
| `ca-certificates-bundle`               | X      | X          |
| `kubernetes-dashboard-metrics-scraper` | X      | X          |
| `wolfi-baselayout`                     | X      | X          |
