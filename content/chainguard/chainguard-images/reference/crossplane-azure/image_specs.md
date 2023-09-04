---
title: "crossplane-azure Image Variants"
type: "article"
description: "Detailed information about the public crossplane-azure Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "crossplane-azure"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **crossplane-azure** Image.

## Variants Compared
The **crossplane-azure** Chainguard Image currently has 5 public variants: 

- `authorization-latest`
- `latest`
- `managedidentity-latest`
- `sql-latest`
- `storage-latest`

The table has detailed information about each of these variants.

|              | authorization-latest      | latest                    | managedidentity-latest    | sql-latest                | storage-latest            |
|--------------|---------------------------|---------------------------|---------------------------|---------------------------|---------------------------|
| Default User | `nonroot`                 | `nonroot`                 | `nonroot`                 | `nonroot`                 | `nonroot`                 |
| Entrypoint   | `/usr/local/bin/provider` | `/usr/local/bin/provider` | `/usr/local/bin/provider` | `/usr/local/bin/provider` | `/usr/local/bin/provider` |
| CMD          | not specified             | not specified             | not specified             | not specified             | not specified             |
| Workdir      | not specified             | not specified             | not specified             | not specified             | not specified             |
| Has apk?     | no                        | no                        | no                        | no                        | no                        |
| Has a shell? | no                        | no                        | no                        | no                        | no                        |

Check the [tags history page](/chainguard/chainguard-images/reference/crossplane-azure/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                             | authorization-latest | latest | managedidentity-latest | sql-latest | storage-latest |
|---------------------------------------------|----------------------|--------|------------------------|------------|----------------|
| `ca-certificates-bundle`                    | X                    | X      | X                      | X          | X              |
| `crossplane-provider-azure`                 | X                    | X      | X                      | X          | X              |
| `crossplane-provider-azure-authorization`   | X                    |        |                        |            |                |
| `terraform`                                 | X                    | X      | X                      | X          | X              |
| `terraform-compat`                          | X                    | X      | X                      | X          | X              |
| `terraform-local-provider-config`           | X                    | X      | X                      | X          | X              |
| `terraform-provider-azurerm`                | X                    | X      | X                      | X          | X              |
| `wolfi-baselayout`                          | X                    | X      | X                      | X          | X              |
| `crossplane-provider-azure-family`          |                      | X      |                        |            |                |
| `crossplane-provider-azure-managedidentity` |                      |        | X                      |            |                |
| `crossplane-provider-azure-sql`             |                      |        |                        | X          |                |
| `crossplane-provider-azure-storage`         |                      |        |                        |            | X              |

