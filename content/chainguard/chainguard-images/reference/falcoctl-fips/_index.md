---
title: "Image Overview: falcoctl-fips"
linktitle: "falcoctl-fips"
type: "article"
layout: "single"
description: "Overview: falcoctl-fips Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/falcoctl-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/falcoctl-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/falcoctl-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/falcoctl-fips/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimalist Wolfi-based image for `falcoctl`.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/falcoctl-fips:latest
```


<!--body:start-->
`falcoctl` is a command-line tool for managing the runtime security tool Falco,
assisting with configuration, rule management, and integration in Kubernetes
environments. falcoctl runs as part of falco by default, but can also be ran
as an external service.

## Usage

`falcoctl` is the entrypoint for the container image. Run with `help` to view
list of supported commands and options:

```bash
docker run cgr.dev/chainguard/falcoctl:latest help
```

For more information, refer to the falco documentation:
- [Install and operate falco](https://falco.org/docs/install-operate/running/)
- [Falco GitHub](https://github.com/falcosecurity/falco)
<!--body:end-->

