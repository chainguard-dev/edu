---
title: "Image Overview: External-dns"
type: "article"
description: "Overview: External-dns Chainguard Image"
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

[cgr.dev/chainguard/external-dns](https://github.com/chainguard-images/images/tree/main/images/external-dns)

| Tag          | Last Updated | Digest                                                                    |
|--------------|--------------|---------------------------------------------------------------------------|
| `latest`     | 20 hours ago | `sha256:ff48aee16093966edf8f4ab561a28389d9629a41b1a67b7940f91228dfd29625` |
| `latest-dev` | 20 hours ago | `sha256:5bb8418ec99c62401ebc2793b525627b4caa53ccc0480c13aa9214dd9fb558b2` |



Minimal image with Kubernetes External DNS. **EXPERIMENTAL**

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/external-dns:latest
```

## Using External DNS

The Chainguard External DNS image is a drop-in replacement for the upstream image.
See the [upstream documentation](https://github.com/kubernetes-sigs/external-dns) for usage information specific to your environment.

```shell
$ docker run cgr.dev/chainguard/external-dns
usage: external-dns --source=source --provider=provider [<flags>]

ExternalDNS synchronizes exposed Kubernetes Services and Ingresses with DNS
providers.

Note that all flags may be replaced with env vars - `--flag` ->
`EXTERNAL_DNS_FLAG=1` or `--flag value` -> `EXTERNAL_DNS_FLAG=value`

Flags:
  --help                         Show context-sensitive help (also try
                                 --help-long and --help-man).
  --version                      Show application version.
  --server=""                    The Kubernetes API server to connect to
                                 (default: auto-detect)
  --kubeconfig=""                Retrieve target cluster configuration from
                                 a Kubernetes configuration file (default:
                                 auto-detect)
```
