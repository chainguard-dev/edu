---
title: "Image Overview: opentelemetry-collector-contrib"
type: "article"
description: "Overview: opentelemetry-collector-contrib Chainguard Image"
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

[cgr.dev/chainguard/opentelemetry-collector-contrib](https://github.com/chainguard-images/images/tree/main/images/opentelemetry-collector-contrib)

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | August 11th  | `sha256:84b59908e5875e48a227706f694c448295c2a62e5b2dd26696f644b942490236` |
|  `latest-dev` | August 9th   | `sha256:becc1491b9abfed532a3fcf9778d2261da931823990db7ea4ba4c7f5c6337c82` |



Minimal image with [opentelemetry-collector-contrib](https://github.com/open-telemetry/opentelemetry-collector-contrib).

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/opentelemetry-collector-contrib:latest
```

## Using this image

Chainguard cgr.dev/chainguard/opentelemetry-collector-contrib is a drop in replacement for the upstream image, tested using the the community [helm chart](https://opentelemetry.io/docs/kubernetes/helm/collector/).

```bash
helm repo add open-telemetry https://open-telemetry.github.io/opentelemetry-helm-charts
helm install my-opentelemetry-collector open-telemetry/opentelemetry-collector \
   --set mode=<daemonset|deployment|statefulset> \
   --set image.repository=cgr.dev/chainguard/opentelemetry-collector-contrib \
   --set image.tag=latest
```

To use custom configuration it is easier to use a values.yaml file:

```yaml
mode: daemonset
configMap:
  create: false
image:
  tag: latest
  repository: cgr.dev/chainguard/opentelemetry-collector-contrib
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

