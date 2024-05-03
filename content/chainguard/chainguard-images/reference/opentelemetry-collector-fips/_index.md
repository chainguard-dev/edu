---
title: "Image Overview: opentelemetry-collector-fips"
linktitle: "opentelemetry-collector-fips"
type: "article"
layout: "single"
description: "Overview: opentelemetry-collector-fips Chainguard Image"
date: 2024-05-03 00:45:55
lastmod: 2024-05-03 00:45:55
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/opentelemetry-collector-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/opentelemetry-collector-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/opentelemetry-collector-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/opentelemetry-collector-fips/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->

Minimal image with [opentelemetry-collector (FIPS-enabled)](https://github.com/open-telemetry/opentelemetry-collector).

<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/opentelemetry-collector-fips:latest
```


<!--body:start-->
## Using this image

Chainguard cgr.dev/chainguard/opentelemetry-collector-fips is a FIPS-enabled drop in replacement for the upstream image, tested using the the community [helm chart](https://opentelemetry.io/docs/kubernetes/helm/collector/).

```bash
helm repo add open-telemetry https://open-telemetry.github.io/opentelemetry-helm-charts
helm install my-opentelemetry-collector open-telemetry/opentelemetry-collector \
   --set mode=<daemonset|deployment|statefulset> \
   --set image.repository=cgr.dev/chainguard/opentelemetry-collector-fips \
   --set image.tag=latest
```

To use custom configuration it is easier to use a values.yaml file:

```yaml
mode: daemonset
configMap:
  create: false
image:
  tag: latest
  repository: cgr.dev/chainguard/opentelemetry-collector-fips
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
<!--body:end-->

