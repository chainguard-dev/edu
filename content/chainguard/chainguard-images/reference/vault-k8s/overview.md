---
title: "Image Overview: Vault-k8s"
type: "article"
description: "Overview: Vault-k8s Chainguard Image"
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

[cgr.dev/chainguard/vault-k8s](https://github.com/chainguard-images/images/tree/main/images/vault-k8s)


Image with Kubernetes Intergrations for Vault.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/vault-k8s:latest
```

## Using Vault K8s

The Chainguard Vault k8s image contains the [vault-k8s](https://github.com/hashicorp/vault-k8s) binary. The binary contains various
intergrations for Kubernetes and Vault, including the Vault Agent Sidecar Injector.
This is a drop-in replacement for the Hashicorp [vault-k8s image](https://hub.docker.com/r/hashicorp/vault-k8s). 

This image is intended to be used alongside the [Chainguard
Vault](https://github.com/chainguard-images/images/tree/main/images/vault) image. See the [Vault
image docs](https://github.com/chainguard-images/images/tree/main/images/vault#helm-chart-usage) for
information on how to run these images with the [Hashicorp Helm Chart](https://github.com/hashicorp/vault-helm).

You can also run this image standalone e.g:

```shell
$ docker run cgr.dev/chainguard/vault-k8s
Usage: vault-k8s [--version] [--help] <command> [<args>]

Available commands are:
    agent-inject    Vault Agent injector service
    version         Prints the version
```
