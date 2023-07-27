---
title: "Postgres Image Variants"
type: "article"
description: "Detailed information about the PostgresChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Postgres"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Postgres** Image.

## Variants Compared
The **postgres** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest                                                       | latest-dev                                                   |
|--------------|--------------------------------------------------------------|--------------------------------------------------------------|
| Default User | `root`                                                       | `root`                                                       |
| Entrypoint   | `/var/lib/postgres/initdb/postgresql-entrypoint.sh postgres` | `/var/lib/postgres/initdb/postgresql-entrypoint.sh postgres` |
| CMD          | not specified                                                | not specified                                                |
| Workdir      | `/home/postgres`                                             | `/home/postgres`                                             |
| Has apk?     | no                                                           | yes                                                          |
| Has a shell? | yes                                                          | yes                                                          |

Check the [tags history page](/chainguard/chainguard-images/reference/postgres/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                                | latest | latest-dev |
|--------------------------------|--------|------------|
| `glibc-locale-en`              | X      | X          |
| `busybox`                      | X      | X          |
| `postgresql-15`                | X      | X          |
| `postgresql-15-client`         | X      | X          |
| `postgresql-15-oci-entrypoint` | X      | X          |
| `postgresql-15-contrib`        | X      | X          |
| `libpq-15`                     | X      | X          |
| `su-exec`                      | X      | X          |
