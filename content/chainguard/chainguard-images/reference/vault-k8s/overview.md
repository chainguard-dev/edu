---
title: "Image Overview: vault-k8s"
type: "article"
description: "Overview: vault-k8s Chainguard Images"
date: 2022-11-01T11:07:52+02:00
lastmod: 2022-11-01T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "images-reference"
weight: 500
toc: true
---

`experimental` [cgr.dev/chainguard/vault-k8s](https://github.com/chainguard-images/images/tree/main/images/vault-k8s)
| Tags         | Aliases                                         |
|--------------|-------------------------------------------------|
| `latest`     | `1`, `1.2`, `1.2.1`, `1.2.1-r0`                 |
| `latest-dev` | `1-dev`, `1.2-dev`, `1.2.1-dev`, `1.2.1-r0-dev` |



Minimal image with the Vault Kubernetes integration. **EXPERIMENTAL**

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/vault-k8s:latest
```

## Using Vault K8s

The Chainguard Vault k8s image contains the `vault-k8s` binary.
This is a drop-in replacement for the upstream image.
See the [documentation there](https://github.com/hashicorp/vault-k8s) for more detailed usage.

```shell
$ docker run cgr.dev/chainguard/vault-k8s
Usage: vault-k8s [--version] [--help] <command> [<args>]

Available commands are:
    agent-inject    Vault Agent injector service
    version         Prints the version
```

