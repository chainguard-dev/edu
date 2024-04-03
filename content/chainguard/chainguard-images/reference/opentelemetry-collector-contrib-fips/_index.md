---
title: "Image Overview: opentelemetry-collector-contrib-fips"
linktitle: "opentelemetry-collector-contrib-fips"
type: "article"
layout: "single"
description: "Overview: opentelemetry-collector-contrib-fips Chainguard Image"
date: 2024-04-03 00:49:16
lastmod: 2024-04-03 00:49:16
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/opentelemetry-collector-contrib-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/opentelemetry-collector-contrib-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/opentelemetry-collector-contrib-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/opentelemetry-collector-contrib-fips/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->

Minimal image with [opentelemetry-collector-contrib (FIPS-enabled)](https://github.com/open-telemetry/opentelemetry-collector-contrib).

<!--overview:end-->

<!--getting:start-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/opentelemetry-collector-contrib-fips:latest
```

<!--getting:end-->

<!--body:start-->

## Using this image

Chainguard cgr.dev/chainguard/opentelemetry-collector-contrib-fips is a FIPS-enabled drop in replacement for the upstream image, tested using the the community [helm chart](https://opentelemetry.io/docs/kubernetes/helm/collector/).

```bash
helm repo add open-telemetry https://open-telemetry.github.io/opentelemetry-helm-charts
helm install my-opentelemetry-collector open-telemetry/opentelemetry-collector \
   --set mode=<daemonset|deployment|statefulset> \
   --set image.repository=cgr.dev/chainguard/opentelemetry-collector-contrib-fips \
   --set image.tag=latest
```

To use custom configuration it is easier to use a values.yaml file:

```yaml
mode: daemonset
configMap:
  create: false
image:
  tag: latest
  repository: cgr.dev/chainguard/opentelemetry-collector-contrib-fips
command:
  extraArgs:
    - "--config=/conf/custom-config.yaml"
extraVolumeMounts:
  - name: "custom-vm"
    mountPath: "/conf"
extraVolumes:
  - name: "custom-vm"
    configMap:
      name: "custom"
```

```bash
helm repo add open-telemetry https://open-telemetry.github.io/opentelemetry-helm-charts
helm install open-telemetry opentelemetry/opentelemetry-collector --namespace open-telemetry-custom-config -f values.yaml
```

<!--body:end-->

