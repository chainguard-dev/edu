---
title: "Kafka Image Variants"
type: "article"
description: "Detailed information about the Kafka Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Kafka"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Kafka** Image.

## Variants Compared
The **kafka** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

## Default Image Settings
`USER`:		`kafka`

`WORKDIR`:	not specified

`ENTRYPOINT`:	`/usr/lib/kafka/bin/kafka-server-start.sh`

`CMD`:		`/usr/lib/kafka/config/server.properties`

The following table has additional information about each of these variants.

|              | latest | latest-dev |
|--------------|--------|------------|
| Has apk?     | no     | yes        |
| Has a shell? | yes    | yes        |

Check the [tags history page](/chainguard/chainguard-images/reference/kafka/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                          | latest | latest-dev |
|--------------------------|--------|------------|
| `bash`                   | X      | X          |
| `busybox`                | X      | X          |
| `kafka`                  | X      | X          |
| `openjdk-11-default-jvm` | X      | X          |
