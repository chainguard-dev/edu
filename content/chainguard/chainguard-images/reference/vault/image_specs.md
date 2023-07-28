---
title: "Vault Image Variants"
type: "article"
description: "Detailed information about the Vault Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Vault"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Vault** Image.

## Variants Compared
The **vault** Chainguard Image currently has 4 public variants: 

- `latest.vault`
- `latest.vault-dev`
- `latest.vault-k8s`
- `latest.vault-k8s-dev`

## Default Image Settings
`USER`:		`vault`

`WORKDIR`:	not specified

`ENTRYPOINT`:	`/usr/bin/vault-k8s`

`CMD`:		not specified

The following table has additional information about each of these variants.

|              | latest.vault | latest.vault-dev | latest.vault-k8s | latest.vault-k8s-dev |
|--------------|--------------|------------------|------------------|----------------------|
| Has apk?     | no           | yes              | no               | yes                  |
| Has a shell? | no           | yes              | no               | yes                  |

Check the [tags history page](/chainguard/chainguard-images/reference/vault/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                    | latest.vault | latest.vault-dev | latest.vault-k8s | latest.vault-k8s-dev |
|--------------------|--------------|------------------|------------------|----------------------|
| `vault`            | X            | X                |                  |                      |
| `vault-entrypoint` | X            | X                |                  |                      |
| `vault-k8s`        |              |                  | X                | X                    |
| `libcap`           |              |                  | X                | X                    |
