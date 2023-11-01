---
title: "Image Overview: redis-sentinel-bitnami"
linktitle: "redis-sentinel-bitnami"
type: "article"
layout: "single"
description: "Overview: redis-sentinel-bitnami Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/redis-sentinel-bitnami/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/redis-sentinel-bitnami/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/redis-sentinel-bitnami/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/redis-sentinel-bitnami/provenance_info/" >}}
{{</ tabs >}}



Minimalist Wolfi-based [Redis-Bitnami]() image. This is intended to be a drop in replacement for deployments that require Bitnami compatibility. The most common case is the Bitnami Helm chart, which can be deployed as follows:

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

