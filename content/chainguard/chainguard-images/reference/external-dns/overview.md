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

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | August 23rd  | `sha256:c7881e51169726587e173b7180c68f5875cfe005eab88b8b2e211d0e7b760462` |
|  `latest`     | August 15th  | `sha256:742835e0219fd9176505a9b4386ce2df5c09b8f685781c3d41077f35b968a1ea` |



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

