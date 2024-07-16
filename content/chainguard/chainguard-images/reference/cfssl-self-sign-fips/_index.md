---
title: "Image Overview: cfssl-self-sign-fips"
linktitle: "cfssl-self-sign-fips"
type: "article"
layout: "single"
description: "Overview: cfssl-self-sign-fips Chainguard Image"
date: 2024-07-10 00:36:03
lastmod: 2024-07-10 00:36:03
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/cfssl-self-sign-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/cfssl-self-sign-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/cfssl-self-sign-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/cfssl-self-sign-fips/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->

## Overview

This image is a wrapper around self-signed certificate generator using Cloudflare's PKI toolkit, `cfssl` which is a tool which is useful for generating self-signed certificates for testing and development purposes.

The image generates a self-signed certificate for a wildcard domain, `*.example.com` by default. The generated certificates are output to the `/output` directory.

<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/cfssl-self-sign-fips:latest
```


<!--body:start-->

## Usage

This image outputs the generated certificates to the `/output` directory. You can mount a volume to this directory to access the generated certificates.

```bash
$ docker container run -v $(pwd):/output cgr.dev/chainguard-private/cfssl-self-sign

$ ls
...
ca-config.json
ca-csr.json
ca-key.pem
ca.csr
ca.pem
wildcard-csr.json
wildcard-key.pem
wildcard.csr
wildcard.pem
...
```

<!--body:end-->

