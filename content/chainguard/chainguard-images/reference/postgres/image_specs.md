---
title: "postgres Image Variants"
type: "article"
description: "Detailed specs for postgres Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
images: []
menu:
  docs:
    parent: "postgres"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **postgres** Image.

## Variants Compared
The **postgres** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest                                                       |
|--------------|--------------------------------------------------------------|
| Default User | `root`                                                       |
| Entrypoint   | `/var/lib/postgres/initdb/postgresql-entrypoint.sh postgres` |
| CMD          | not specified                                                |
| Workdir      | `/home/postgres`                                             |
| Has apk?     | no                                                           |
| Has a shell? | yes                                                          |

## Image Dependencies
The table shows package distribution across all variants.

|                                | latest |
|--------------------------------|--------|
| `ca-certificates-bundle`       | X      |
| `wolfi-baselayout`             | X      |
| `busybox`                      | X      |
| `postgresql-15`                | X      |
| `postgresql-15-client`         | X      |
| `postgresql-15-oci-entrypoint` | X      |
| `postgresql-15-contrib`        | X      |
| `libpq-15`                     | X      |
| `su-exec`                      | X      |
