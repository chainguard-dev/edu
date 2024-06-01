---
title: "Image Overview: redis-sentinel-bitnami-fips"
linktitle: "redis-sentinel-bitnami-fips"
type: "article"
layout: "single"
description: "Overview: redis-sentinel-bitnami-fips Chainguard Image"
date: 2024-06-01 00:50:07
lastmod: 2024-06-01 00:50:07
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/redis-sentinel-bitnami-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/redis-sentinel-bitnami-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/redis-sentinel-bitnami-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/redis-sentinel-bitnami-fips/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimalist Wolfi-based [Redis-Bitnami](https://github.com/redis/redis) image.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/redis-sentinel-bitnami-fips:latest
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

