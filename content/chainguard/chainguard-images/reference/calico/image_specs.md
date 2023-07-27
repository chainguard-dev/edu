---
title: "Calico Image Variants"
type: "article"
description: "Detailed information about the CalicoChainguard Image variants"
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

The table has detailed information about each of these variants.

|              | latest.typha            | latest.typha-dev        | latest.pod2daemon     | latest.pod2daemon-dev | latest.node             | latest.node-dev         | latest.kube-controllers            | latest.kube-controllers-dev        | latest.csi                             | latest.csi-dev                         | latest.cni             | latest.cni-dev         | latest.calicoctl     | latest.calicoctl-dev |
|--------------|-------------------------|-------------------------|-----------------------|-----------------------|-------------------------|-------------------------|------------------------------------|------------------------------------|----------------------------------------|----------------------------------------|------------------------|------------------------|----------------------|----------------------|
| Default User | `nonroot`               | `nonroot`               | `root`                | `root`                | `root`                  | `root`                  | `nonroot`                          | `nonroot`                          | `root`                                 | `root`                                 | `root`                 | `root`                 | `nonroot`            | `nonroot`            |
| Entrypoint   | `/sbin/tini --`         | `/sbin/tini --`         | `/usr/bin/flexvol.sh` | `/usr/bin/flexvol.sh` | `/usr/sbin/start_runit` | `/usr/sbin/start_runit` | `/usr/bin/calico-kube-controllers` | `/usr/bin/calico-kube-controllers` | `/usr/bin/calico-pod2daemon-csidriver` | `/usr/bin/calico-pod2daemon-csidriver` | `/opt/cni/bin/install` | `/opt/cni/bin/install` | `/usr/bin/calicoctl` | `/usr/bin/calicoctl` |
| CMD          | `/usr/bin/calico-typha` | `/usr/bin/calico-typha` | not specified         | not specified         | not specified           | not specified           | not specified                      | not specified                      | not specified                          | not specified                          | not specified          | not specified          | not specified        | not specified        |
| Workdir      | not specified           | not specified           | not specified         | not specified         | not specified           | not specified           | not specified                      | not specified                      | not specified                          | not specified                          | not specified          | not specified          | not specified        | not specified        |
| Has apk?     | no                      | yes                     | no                    | yes                   | no                      | yes                     | no                                 | yes                                | no                                     | yes                                    | no                     | yes                    | no                   | yes                  |
| Has a shell? | no                      | yes                     | yes                   | yes                   | yes                     | yes                     | no                                 | yes                                | no                                     | yes                                    | no                     | yes                    | no                   | yes                  |

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
