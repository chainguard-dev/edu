---
title: "calico-node-driver-registrar Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public calico-node-driver-registrar Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/calico-node-driver-registrar/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/calico-node-driver-registrar/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/calico-node-driver-registrar/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/calico-node-driver-registrar/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **calico-node-driver-registrar** Image.

## Variants Compared
The **calico-node-driver-registrar** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest                               |
|--------------|--------------------------------------|
| Default User | `nonroot`                            |
| Entrypoint   | `/usr/bin/csi-node-driver-registrar` |
| CMD          | not specified                        |
| Workdir      | not specified                        |
| Has apk?     | no                                   |
| Has a shell? | no                                   |

Check the [tags history page](/chainguard/chainguard-images/reference/calico-node-driver-registrar/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                               | latest |
|-----------------------------------------------|--------|
| `ca-certificates-bundle`                      | X      |
| `glibc`                                       | X      |
| `glibc-locale-posix`                          | X      |
| `kubernetes-csi-node-driver-registrar`        | X      |
| `kubernetes-csi-node-driver-registrar-compat` | X      |
| `ld-linux`                                    | X      |
| `wolfi-baselayout`                            | X      |

