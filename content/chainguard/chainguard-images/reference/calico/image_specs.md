---
title: "calico Image Variants"
type: "article"
description: "Detailed information about the public calico Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "calico"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **calico** Image.

## Variants Compared
The **calico** Chainguard Image currently has 10 public variants: 

- `cni-latest`
- `csi-latest`
- `kube-controllers-latest`
- `latest`
- `node-driver-registrar-latest`
- `node-latest`
- `pod2daemon-flexvol-latest`
- `pod2daemon-latest`
- `typha-latest`
- `calicoctl-latest`

The table has detailed information about each of these variants.

|              | cni-latest             | csi-latest                             | kube-controllers-latest            | latest               | node-driver-registrar-latest         | node-latest             | pod2daemon-flexvol-latest | pod2daemon-latest     | typha-latest            | calicoctl-latest     |
|--------------|------------------------|----------------------------------------|------------------------------------|----------------------|--------------------------------------|-------------------------|---------------------------|-----------------------|-------------------------|----------------------|
| Default User | `0`                    | `0`                                    | `65532`                            | `65532`              | `65532`                              | `0`                     | `0`                       | `0`                   | `65532`                 | `65532`              |
| Entrypoint   | `/opt/cni/bin/install` | `/usr/bin/calico-pod2daemon-csidriver` | `/usr/bin/calico-kube-controllers` | `/usr/bin/calicoctl` | `/usr/bin/csi-node-driver-registrar` | `/usr/sbin/start_runit` | `/usr/bin/flexvol.sh`     | `/usr/bin/flexvol.sh` | `/sbin/tini --`         | `/usr/bin/calicoctl` |
| CMD          | not specified          | not specified                          | not specified                      | not specified        | not specified                        | not specified           | not specified             | not specified         | `/usr/bin/calico-typha` | not specified        |
| Workdir      | not specified          | not specified                          | not specified                      | not specified        | not specified                        | not specified           | not specified             | not specified         | not specified           | not specified        |
| Has apk?     | no                     | no                                     | no                                 | no                   | no                                   | no                      | no                        | no                    | no                      | no                   |
| Has a shell? | no                     | no                                     | no                                 | no                   | no                                   | yes                     | yes                       | yes                   | no                      | no                   |

Check the [tags history page](/chainguard/chainguard-images/reference/calico/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                               | cni-latest | csi-latest | kube-controllers-latest | latest | node-driver-registrar-latest | node-latest | pod2daemon-flexvol-latest | pod2daemon-latest | typha-latest | calicoctl-latest |
|-----------------------------------------------|------------|------------|-------------------------|--------|------------------------------|-------------|---------------------------|-------------------|--------------|------------------|
| `ca-certificates-bundle`                      | X          | X          | X                       | X      | X                            | X           | X                         | X                 | X            | X                |
| `calico-cni`                                  | X          |            |                         |        |                              |             |                           |                   |              |                  |
| `calico-cni-compat`                           | X          |            |                         |        |                              |             |                           |                   |              |                  |
| `cni-plugins-bandwidth`                       | X          |            |                         |        |                              |             |                           |                   |              |                  |
| `cni-plugins-bandwidth-compat`                | X          |            |                         |        |                              |             |                           |                   |              |                  |
| `cni-plugins-host-local`                      | X          |            |                         |        |                              |             |                           |                   |              |                  |
| `cni-plugins-host-local-compat`               | X          |            |                         |        |                              |             |                           |                   |              |                  |
| `cni-plugins-loopback`                        | X          |            |                         |        |                              |             |                           |                   |              |                  |
| `cni-plugins-loopback-compat`                 | X          |            |                         |        |                              |             |                           |                   |              |                  |
| `cni-plugins-portmap`                         | X          |            |                         |        |                              |             |                           |                   |              |                  |
| `cni-plugins-portmap-compat`                  | X          |            |                         |        |                              |             |                           |                   |              |                  |
| `cni-plugins-tuning`                          | X          |            |                         |        |                              |             |                           |                   |              |                  |
| `cni-plugins-tuning-compat`                   | X          |            |                         |        |                              |             |                           |                   |              |                  |
| `flannel-cni-plugin`                          | X          |            |                         |        |                              |             |                           |                   |              |                  |
| `flannel-cni-plugin-compat`                   | X          |            |                         |        |                              |             |                           |                   |              |                  |
| `wolfi-baselayout`                            | X          | X          | X                       | X      | X                            | X           | X                         | X                 | X            | X                |
| `calico-pod2daemon`                           |            | X          |                         |        |                              |             | X                         | X                 |              |                  |
| `glibc`                                       |            | X          | X                       | X      | X                            | X           | X                         | X                 | X            | X                |
| `glibc-locale-posix`                          |            | X          | X                       | X      | X                            | X           | X                         | X                 | X            | X                |
| `ld-linux`                                    |            | X          | X                       | X      | X                            | X           | X                         | X                 | X            | X                |
| `calico-kube-controllers`                     |            |            | X                       |        |                              |             |                           |                   |              |                  |
| `glibc-dev`                                   |            |            | X                       |        |                              |             |                           |                   |              |                  |
| `libcrypt1`                                   |            |            | X                       |        |                              | X           | X                         | X                 |              |                  |
| `linux-headers`                               |            |            | X                       |        |                              |             |                           |                   |              |                  |
| `nss-db`                                      |            |            | X                       |        |                              |             |                           |                   |              |                  |
| `nss-hesiod`                                  |            |            | X                       |        |                              |             |                           |                   |              |                  |
| `calicoctl`                                   |            |            |                         | X      |                              |             |                           |                   |              | X                |
| `kubernetes-csi-node-driver-registrar`        |            |            |                         |        | X                            |             |                           |                   |              |                  |
| `kubernetes-csi-node-driver-registrar-compat` |            |            |                         |        | X                            |             |                           |                   |              |                  |
| `busybox`                                     |            |            |                         |        |                              | X           | X                         | X                 |              |                  |
| `calico-node`                                 |            |            |                         |        |                              | X           |                           |                   |              |                  |
| `conntrack-tools`                             |            |            |                         |        |                              | X           |                           |                   |              |                  |
| `ip6tables`                                   |            |            |                         |        |                              | X           |                           |                   |              |                  |
| `iproute2`                                    |            |            |                         |        |                              | X           |                           |                   |              |                  |
| `ipset`                                       |            |            |                         |        |                              | X           |                           |                   |              |                  |
| `iptables`                                    |            |            |                         |        |                              | X           |                           |                   |              |                  |
| `libbpf`                                      |            |            |                         |        |                              | X           |                           |                   |              |                  |
| `libbz2-1`                                    |            |            |                         |        |                              | X           |                           |                   |              |                  |
| `libelf`                                      |            |            |                         |        |                              | X           |                           |                   |              |                  |
| `libmnl`                                      |            |            |                         |        |                              | X           |                           |                   |              |                  |
| `libnetfilter_conntrack`                      |            |            |                         |        |                              | X           |                           |                   |              |                  |
| `libnetfilter_cthelper`                       |            |            |                         |        |                              | X           |                           |                   |              |                  |
| `libnetfilter_cttimeout`                      |            |            |                         |        |                              | X           |                           |                   |              |                  |
| `libnetfilter_queue`                          |            |            |                         |        |                              | X           |                           |                   |              |                  |
| `libnfnetlink`                                |            |            |                         |        |                              | X           |                           |                   |              |                  |
| `libnftnl`                                    |            |            |                         |        |                              | X           |                           |                   |              |                  |
| `libpcap`                                     |            |            |                         |        |                              | X           |                           |                   |              |                  |
| `libproc-2-0`                                 |            |            |                         |        |                              | X           |                           |                   |              |                  |
| `ncurses`                                     |            |            |                         |        |                              | X           |                           |                   |              |                  |
| `ncurses-terminfo-base`                       |            |            |                         |        |                              | X           |                           |                   |              |                  |
| `procps`                                      |            |            |                         |        |                              | X           |                           |                   |              |                  |
| `runit`                                       |            |            |                         |        |                              | X           |                           |                   |              |                  |
| `xz`                                          |            |            |                         |        |                              | X           |                           |                   |              |                  |
| `zlib`                                        |            |            |                         |        |                              | X           |                           |                   |              |                  |
| `calico-pod2daemon-flexvol-compat`            |            |            |                         |        |                              |             | X                         |                   |              |                  |
| `calico-typhad`                               |            |            |                         |        |                              |             |                           |                   | X            |                  |
| `tini`                                        |            |            |                         |        |                              |             |                           |                   | X            |                  |
