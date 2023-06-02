---
title: "newrelic-k8s-events-forwarder Image Variants"
type: "article"
description: "Detailed specs for newrelic-k8s-events-forwarder Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "newrelic-k8s-events-forwarder"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **newrelic-k8s-events-forwarder** Image.

## Variants Compared
The **newrelic-k8s-events-forwarder** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest                            | latest-dev                        |
|--------------|-----------------------------------|-----------------------------------|
| Default User | `nonroot`                         | `nonroot`                         |
| Entrypoint   | `/sbin/tini --`                   | `/sbin/tini --`                   |
| CMD          | `/usr/bin/newrelic-infra-service` | `/usr/bin/newrelic-infra-service` |
| Workdir      | not specified                     | not specified                     |
| Has apk?     | no                                | yes                               |
| Has a shell? | no                                | yes                               |

## Image Dependencies
The table shows package distribution across all variants.

|                                 | latest | latest-dev |
|---------------------------------|--------|------------|
| `ca-certificates-bundle`        | X      | X          |
| `wolfi-baselayout`              | X      | X          |
| `bind-tools`                    | X      | X          |
| `tini`                          | X      | X          |
| `curl`                          | X      | X          |
| `newrelic-infrastructure-agent` | X      | X          |
| `apk-tools`                     |        | X          |
| `bash`                          |        | X          |
| `busybox`                       |        | X          |
| `git`                           |        | X          |

