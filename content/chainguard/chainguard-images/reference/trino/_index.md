---
title: "Image Overview: trino"
linktitle: "trino"
type: "article"
layout: "single"
description: "Overview: trino Chainguard Image"
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

{{< tabs >}}
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/trino/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/trino/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/trino/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/trino/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Fast distributed SQL query engine for big data analytics that helps you explore your data universe.
<!--overview:end-->

<!--getting:start-->
## Get It!
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/trino:latest
```
<!--getting:end-->

<!--body:start-->
## Usage

There is a TrinoDB Helm Chart exists, [here](https://github.com/trinodb/charts), which makes it easy to deploy TrinoDB on Kubernetes.

Here is the command that can be used to deploy TrinoDB on Kubernetes:

```
helm repo add trino https://trinodb.github.io/charts
helm repo update
helm install trino trino/trino \
      --set image.repository=cgr.dev/chainguard/trino
```

That's it, now, you have TrinoDB running on Kubernetes.
<!--body:end-->

