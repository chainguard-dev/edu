---
title: "Image Overview: external-dns"
type: "article"
description: "Overview: external-dns Chainguard Image"
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

| Tag (s)       | Last Changed  | Digest                                                                    |
|---------------|---------------|---------------------------------------------------------------------------|
|  `latest`     | September 7th | `sha256:fefcf4601dfe8ef95552315081abbb3b4026f1b0d4d63c849723d7d970591201` |
|  `latest-dev` | September 7th | `sha256:879b9d22600b9c3e41109d01125861c9841b33ad840c147db3ada76b956ad0d1` |



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

