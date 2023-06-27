---
title: "Terraform Image Variants"
type: "article"
description: "Detailed information about the TerraformChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Terraform"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Terraform** Image.

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

Check the [tags history page](/chainguard/chainguard-images/reference/terraform/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                          | latest |
|--------------------------|--------|
| `terraform`              | X      |
| `ca-certificates-bundle` | X      |
