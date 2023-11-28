---
title: "Image Overview: bank-vaults"
linktitle: "bank-vaults"
type: "article"
layout: "single"
description: "Overview: bank-vaults Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2023-11-28 00:31:13
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/bank-vaults/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/bank-vaults/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/bank-vaults/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/bank-vaults/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal Image for [Bank Vaults](https://bank-vaults.dev/), a CLI tool to init, unseal and configure Vault 
<!--overview:end-->

<!--getting:start-->
## Get It!
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/bank-vaults:latest
```
<!--getting:end-->

<!--body:start-->
## Usage

This image is a drop-in replacement for the upstream image.
You can run it using the helm chart with:

```shell
$ helm repo add bank-vaults oci://ghcr.io/bank-vaults/helm-charts/vault-operator
$ helm install bank-vaults bank-vaults/bank-vaults \
    --set bankVaults.image.repository=cgr.dev/chainguard/bank-vaults \
    --set bankVaults.image.tag=latest
    <other configuration parameters here>
```
<!--body:end-->

