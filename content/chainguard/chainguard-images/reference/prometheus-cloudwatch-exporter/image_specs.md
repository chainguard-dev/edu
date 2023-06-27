---
title: "Prometheus-cloudwatch-exporter Image Variants"
type: "article"
description: "Detailed information about the Prometheus-cloudwatch-exporterChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Prometheus-cloudwatch-exporter"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Prometheus-cloudwatch-exporter** Image.

## Variants Compared
The **prometheus-cloudwatch-exporter** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest                                                                                | latest-dev                                                                            |
|--------------|---------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| Default User | `nonroot`                                                                             | `nonroot`                                                                             |
| Entrypoint   | `/usr/bin/java -jar /usr/share/java/cloudwatch_exporter/cloudwatch_exporter.jar 9106` | `/usr/bin/java -jar /usr/share/java/cloudwatch_exporter/cloudwatch_exporter.jar 9106` |
| CMD          | `/config/config.yml`                                                                  | `/config/config.yml`                                                                  |
| Workdir      | not specified                                                                         | not specified                                                                         |
| Has apk?     | no                                                                                    | no                                                                                    |
| Has a shell? | yes                                                                                   | yes                                                                                   |

Check the [tags history page](/chainguard/chainguard-images/reference/prometheus-cloudwatch-exporter/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                          | latest | latest-dev |
|--------------------------|--------|------------|
| `ca-certificates-bundle` | X      | X          |
| `busybox`                | X      | X          |
| `openjdk-17-jre`         | X      | X          |
| `openjdk-17-default-jvm` | X      | X          |
| `cloudwatch-exporter`    | X      | X          |
| `wolfi-baselayout`       | X      | X          |
