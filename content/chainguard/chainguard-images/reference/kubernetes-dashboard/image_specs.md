---
title: "Kubernetes-dashboard Image Variants"
type: "article"
description: "Detailed information about the Kubernetes-dashboard Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Kubernetes-dashboard"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Kubernetes-dashboard** Image.

## Variants Compared
The **kubernetes-dashboard** Chainguard Image currently has 4 public variants: 

- `latest.metrics-scraper`
- `latest.metrics-scraper-dev`
- `latest.dashboard`
- `latest.dashboard-dev`

The table has detailed information about each of these variants.

|              | latest.metrics-scraper     | latest.metrics-scraper-dev | latest.dashboard                                                                                   | latest.dashboard-dev                                                                               |
|--------------|----------------------------|----------------------------|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| Default User | `nonroot`                  | `nonroot`                  | `nonroot`                                                                                          | `nonroot`                                                                                          |
| Entrypoint   | `/usr/bin/metrics-sidecar` | `/usr/bin/metrics-sidecar` | `/usr/share/kubernetes-dashboard/dashboard --insecure-bind-address=0.0.0.0 --bind-address=0.0.0.0` | `/usr/share/kubernetes-dashboard/dashboard --insecure-bind-address=0.0.0.0 --bind-address=0.0.0.0` |
| CMD          | not specified              | not specified              | not specified                                                                                      | not specified                                                                                      |
| Workdir      | not specified              | not specified              | not specified                                                                                      | not specified                                                                                      |
| Has apk?     | no                         | yes                        | no                                                                                                 | yes                                                                                                |
| Has a shell? | no                         | yes                        | no                                                                                                 | yes                                                                                                |

Check the [tags history page](/chainguard/chainguard-images/reference/kubernetes-dashboard/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                                        | latest.metrics-scraper | latest.metrics-scraper-dev | latest.dashboard | latest.dashboard-dev |
|----------------------------------------|------------------------|----------------------------|------------------|----------------------|
| `kubernetes-dashboard-metrics-scraper` | X                      | X                          |                  |                      |
| `kubernetes-dashboard`                 |                        |                            | X                | X                    |
