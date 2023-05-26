---
title: "prometheus-cloudwatch-exporter Image Variants"
type: "article"
description: "Detailed specs for prometheus-cloudwatch-exporter Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "prometheus-cloudwatch-exporter"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **prometheus-cloudwatch-exporter** Image.

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
| Has apk?     | no                                                                                    | yes                                                                                   |
| Has a shell? | yes                                                                                   | yes                                                                                   |

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
| `apk-tools`              |        | X          |
| `bash`                   |        | X          |
| `git`                    |        | X          |

