---
title: "Image Overview: redis-bitnami-cluster-bitnami"
linktitle: "redis-bitnami-cluster-bitnami"
type: "article"
layout: "single"
description: "Overview: redis-bitnami-cluster-bitnami Chainguard Image"
date: 2024-04-18 00:43:55
lastmod: 2024-04-18 00:43:55
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/redis-bitnami-cluster-bitnami/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/redis-bitnami-cluster-bitnami/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/redis-bitnami-cluster-bitnami/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/redis-bitnami-cluster-bitnami/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimalist Wolfi-based [Redis-Bitnami](https://github.com/redis/redis) image.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/redis-bitnami-cluster-bitnami:latest
```


<!--body:start-->
This image is intended to be a drop in replacement for deployments that require Bitnami compatibility. The most common case is the Bitnami Helm chart, which can be deployed as follows:

```bash
cat <<EOF > values.yaml
image:
  registry: cgr.dev
  repository: chainguard/redis-server-bitnami
  tag: latest
# Optinoally enable HA sentinel:
sentinel:
  enabled: true
  image:
    registry: cgr.dev
    repository: chainguard/redis-sentinel-bitnami
    tag: latest
EOF
```
<!--body:end-->

