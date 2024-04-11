---
title: "Image Overview: grafana-agent-operator"
linktitle: "grafana-agent-operator"
type: "article"
layout: "single"
description: "Overview: grafana-agent-operator Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-04-11 12:38:02
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/grafana-agent-operator/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/grafana-agent-operator/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/grafana-agent-operator/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/grafana-agent-operator/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
[Grafana Agent Operator](https://grafana.com/docs/agent/latest/operator/) is a Kubernetes operator for the static mode of Grafana Agent.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/grafana-agent-operator:latest
```


<!--body:start-->

## Usage
For full instructions on grafana-agent-operator, refer to the
[official documentation](https://grafana.com/docs/agent/latest/operator/).
The GitHub repository can also be [found here](https://github.com/grafana/agent).

### Helm
To deploy via helm, please refer to the
[official helm charts documentation](https://grafana.com/docs/agent/latest/operator/helm-getting-started/) and the [helm charts repository](https://github.com/grafana/helm-charts/tree/main/charts/agent-operator)
for comprehensive instructions, which includes
[supported parameters](https://github.com/grafana/helm-charts/blob/main/charts/agent-operator/values.yaml)

Below is an example of how to use the helm chart, overriding the image with the
chainguard image:

```bash
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update

helm install my-release grafana/grafana-agent-operator \
 --set image.registry=cgr.dev \
 --set image.repository=chainguard/grafana-agent-operator \
 --set image.tag=latest
```
<!--body:end-->

