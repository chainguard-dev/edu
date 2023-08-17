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
|  `latest-dev` | August 16th  | `sha256:325c5e98b1056f3ad8b6783bff979f6fcdccbd41306a5f8fe749a247ab27251c` |
|  `latest`     | August 16th  | `sha256:5f9ba82341dde18196f1c6baa8b6719ce4d189998087138dfd488aae829be4cb` |



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

