---
title: "Image Overview: external-dns-fips"
linktitle: "external-dns-fips"
type: "article"
layout: "single"
description: "Overview: external-dns-fips Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-04-11 12:38:02
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu: 
  docs: 
    parent: "images-reference"
weight: 500
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/external-dns-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/external-dns-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/external-dns-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/external-dns-fips/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal image to configure external DNS servers (AWS Route53, Google CloudDNS and others) for Kubernetes Ingresses and Services
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/external-dns-fips:latest
```


<!--body:start-->
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
<!--body:end-->

