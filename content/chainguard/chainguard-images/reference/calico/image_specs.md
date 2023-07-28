---
title: "Calico Image Variants"
type: "article"
description: "Detailed information about the Calico Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Calico"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Calico** Image.

## Variants Compared
The **calico** Chainguard Image currently has 14 public variants: 

- `latest.typha`
- `latest.typha-dev`
- `latest.pod2daemon`
- `latest.pod2daemon-dev`
- `latest.node`
- `latest.node-dev`
- `latest.kube-controllers`
- `latest.kube-controllers-dev`
- `latest.csi`
- `latest.csi-dev`
- `latest.cni`
- `latest.cni-dev`
- `latest.calicoctl`
- `latest.calicoctl-dev`

## Default Image Settings
`USER`:		`nonroot`

`WORKDIR`:	not specified

`ENTRYPOINT`:	`/usr/bin/calicoctl`

`CMD`:		not specified

The following table has additional information about each of these variants.

|              | latest.typha | latest.typha-dev | latest.pod2daemon | latest.pod2daemon-dev | latest.node | latest.node-dev | latest.kube-controllers | latest.kube-controllers-dev | latest.csi | latest.csi-dev | latest.cni | latest.cni-dev | latest.calicoctl | latest.calicoctl-dev |
|--------------|--------------|------------------|-------------------|-----------------------|-------------|-----------------|-------------------------|-----------------------------|------------|----------------|------------|----------------|------------------|----------------------|
| Has apk?     | no           | yes              | no                | yes                   | no          | yes             | no                      | yes                         | no         | yes            | no         | yes            | no               | yes                  |
| Has a shell? | no           | yes              | yes               | yes                   | yes         | yes             | no                      | yes                         | no         | yes            | no         | yes            | no               | yes                  |

Check the [tags history page](/chainguard/chainguard-images/reference/calico/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                           | latest.typha | latest.typha-dev | latest.pod2daemon | latest.pod2daemon-dev | latest.node | latest.node-dev | latest.kube-controllers | latest.kube-controllers-dev | latest.csi | latest.csi-dev | latest.cni | latest.cni-dev | latest.calicoctl | latest.calicoctl-dev |
|---------------------------|--------------|------------------|-------------------|-----------------------|-------------|-----------------|-------------------------|-----------------------------|------------|----------------|------------|----------------|------------------|----------------------|
| `calico-typhad`           | X            | X                |                   |                       |             |                 |                         |                             |            |                |            |                |                  |                      |
| `tini`                    | X            | X                |                   |                       |             |                 |                         |                             |            |                |            |                |                  |                      |
| `calico-pod2daemon`       |              |                  | X                 | X                     |             |                 |                         |                             | X          | X              |            |                |                  |                      |
| `busybox`                 |              |                  | X                 | X                     | X           | X               |                         |                             |            |                |            |                |                  |                      |
| `calico-node`             |              |                  |                   |                       | X           | X               |                         |                             |            |                |            |                |                  |                      |
| `calico-kube-controllers` |              |                  |                   |                       |             |                 | X                       | X                           |            |                |            |                |                  |                      |
| `calico-cni`              |              |                  |                   |                       |             |                 |                         |                             |            |                | X          | X              |                  |                      |
| `calico-cni-compat`       |              |                  |                   |                       |             |                 |                         |                             |            |                | X          | X              |                  |                      |
| `calicoctl`               |              |                  |                   |                       |             |                 |                         |                             |            |                |            |                | X                | X                    |
