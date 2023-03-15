---
title: "terraform Image Variants"
type: "article"
description: "Detailed specs for terraform Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
images: []
menu:
  docs:
    parent: "terraform"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **terraform** Image.

## Variants Compared
The **terraform** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest               |
|--------------|----------------------|
| Default User | `nonroot`            |
| Entrypoint   | `/usr/bin/terraform` |
| CMD          | `--help`             |
| Workdir      | not specified        |
| Has apk?     | no                   |
| Has a shell? | no                   |

## Image Dependencies
The table shows package distribution across all variants.

|                    | latest |
|--------------------|--------|
| `terraform`        | X      |
| `wolfi-baselayout` | X      |
