---
title: "Prometheus Image Variants"
type: "article"
description: "Detailed information about the Prometheus Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Prometheus"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Prometheus** Image.

## Variants Compared
The **prometheus** Chainguard Image currently has 20 public variants: 

- `latest.redis-exporter`
- `latest.redis-exporter-dev`
- `latest.postgres-exporter`
- `latest.postgres-exporter-dev`
- `latest.operator`
- `latest.operator-dev`
- `latest.node-exporter`
- `latest.node-exporter-dev`
- `latest.mysqld-exporter`
- `latest.mysqld-exporter-dev`
- `latest.elasticsearch-exporter`
- `latest.elasticsearch-exporter-dev`
- `latest.core`
- `latest.core-dev`
- `latest.config-reloader`
- `latest.config-reloader-dev`
- `latest.cloudwatch-exporter`
- `latest.cloudwatch-exporter-dev`
- `latest.alertmanager`
- `latest.alertmanager-dev`

## Default Image Settings
`USER`:		`alertmanager`

`WORKDIR`:	not specified

`ENTRYPOINT`:	`/usr/bin/alertmanager`

`CMD`:		`--config.file=/etc/alertmanager/alertmanager.yml --storage.path=/alertmanager`

The following table has additional information about each of these variants.

|              | latest.redis-exporter | latest.redis-exporter-dev | latest.postgres-exporter | latest.postgres-exporter-dev | latest.operator | latest.operator-dev | latest.node-exporter | latest.node-exporter-dev | latest.mysqld-exporter | latest.mysqld-exporter-dev | latest.elasticsearch-exporter | latest.elasticsearch-exporter-dev | latest.core | latest.core-dev | latest.config-reloader | latest.config-reloader-dev | latest.cloudwatch-exporter | latest.cloudwatch-exporter-dev | latest.alertmanager | latest.alertmanager-dev |
|--------------|-----------------------|---------------------------|--------------------------|------------------------------|-----------------|---------------------|----------------------|--------------------------|------------------------|----------------------------|-------------------------------|-----------------------------------|-------------|-----------------|------------------------|----------------------------|----------------------------|--------------------------------|---------------------|-------------------------|
| Has apk?     | no                    | yes                       | no                       | yes                          | no              | yes                 | no                   | yes                      | yes                    | yes                        | yes                           | yes                               | no          | yes             | no                     | yes                        | no                         | yes                            | yes                 | yes                     |
| Has a shell? | no                    | yes                       | yes                      | yes                          | no              | yes                 | yes                  | yes                      | yes                    | yes                        | yes                           | yes                               | no          | yes             | no                     | yes                        | yes                        | yes                            | yes                 | yes                     |

Check the [tags history page](/chainguard/chainguard-images/reference/prometheus/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                                                    | latest.redis-exporter | latest.redis-exporter-dev | latest.postgres-exporter | latest.postgres-exporter-dev | latest.operator | latest.operator-dev | latest.node-exporter | latest.node-exporter-dev | latest.mysqld-exporter | latest.mysqld-exporter-dev | latest.elasticsearch-exporter | latest.elasticsearch-exporter-dev | latest.core | latest.core-dev | latest.config-reloader | latest.config-reloader-dev | latest.cloudwatch-exporter | latest.cloudwatch-exporter-dev | latest.alertmanager | latest.alertmanager-dev |
|----------------------------------------------------|-----------------------|---------------------------|--------------------------|------------------------------|-----------------|---------------------|----------------------|--------------------------|------------------------|----------------------------|-------------------------------|-----------------------------------|-------------|-----------------|------------------------|----------------------------|----------------------------|--------------------------------|---------------------|-------------------------|
| `prometheus-redis-exporter`                        | X                     | X                         |                          |                              |                 |                     |                      |                          |                        |                            |                               |                                   |             |                 |                        |                            |                            |                                |                     |                         |
| `prometheus-postgres-exporter`                     |                       |                           | X                        | X                            |                 |                     |                      |                          |                        |                            |                               |                                   |             |                 |                        |                            |                            |                                |                     |                         |
| `busybox`                                          |                       |                           | X                        | X                            |                 |                     | X                    | X                        | X                      | X                          | X                             | X                                 |             |                 |                        |                            | X                          | X                              | X                   | X                       |
| `prometheus-operator`                              |                       |                           |                          |                              | X               | X                   |                      |                          |                        |                            |                               |                                   |             |                 |                        |                            |                            |                                |                     |                         |
| `prometheus-node-exporter`                         |                       |                           |                          |                              |                 |                     | X                    | X                        |                        |                            |                               |                                   |             |                 |                        |                            |                            |                                |                     |                         |
| `prometheus-mysqld-exporter`                       |                       |                           |                          |                              |                 |                     |                      |                          | X                      | X                          |                               |                                   |             |                 |                        |                            |                            |                                |                     |                         |
| `wolfi-base`                                       |                       |                           |                          |                              |                 |                     |                      |                          | X                      | X                          | X                             | X                                 |             |                 |                        |                            |                            |                                | X                   | X                       |
| `prometheus-elasticsearch-exporter`                |                       |                           |                          |                              |                 |                     |                      |                          |                        |                            | X                             | X                                 |             |                 |                        |                            |                            |                                |                     |                         |
| `prometheus`                                       |                       |                           |                          |                              |                 |                     |                      |                          |                        |                            |                               |                                   | X           | X               |                        |                            |                            |                                |                     |                         |
| `prometheus-config-reloader`                       |                       |                           |                          |                              |                 |                     |                      |                          |                        |                            |                               |                                   |             |                 | X                      | X                          |                            |                                |                     |                         |
| `prometheus-config-reloader-oci-entrypoint-compat` |                       |                           |                          |                              |                 |                     |                      |                          |                        |                            |                               |                                   |             |                 | X                      | X                          |                            |                                |                     |                         |
| `openjdk-17-jre`                                   |                       |                           |                          |                              |                 |                     |                      |                          |                        |                            |                               |                                   |             |                 |                        |                            | X                          | X                              |                     |                         |
| `openjdk-17-default-jvm`                           |                       |                           |                          |                              |                 |                     |                      |                          |                        |                            |                               |                                   |             |                 |                        |                            | X                          | X                              |                     |                         |
| `cloudwatch-exporter`                              |                       |                           |                          |                              |                 |                     |                      |                          |                        |                            |                               |                                   |             |                 |                        |                            | X                          | X                              |                     |                         |
| `prometheus-alertmanager`                          |                       |                           |                          |                              |                 |                     |                      |                          |                        |                            |                               |                                   |             |                 |                        |                            |                            |                                | X                   | X                       |
