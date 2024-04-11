---
title: "Image Overview: cortex-fips"
linktitle: "cortex-fips"
type: "article"
layout: "single"
description: "Overview: cortex-fips Chainguard Image"
date: 2024-04-11 00:54:43
lastmod: 2024-04-11 00:54:43
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/cortex-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/cortex-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/cortex-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/cortex-fips/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Cortex provides horizontally scalable, highly available, multi-tenant, long term storage for Prometheus.
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/cortex:latest
```
<!--getting:end-->

<!--body:start-->

## Usage
For full instructions on using cortex, refer to the
[official documentation](https://cortexmetrics.io/docs/).
The GitHub repository can also be [found here](https://github.com/cortexproject/cortex).

### Helm
To deploy cortex via helm, please refer to the
[official helm charts documentation](https://cortexproject.github.io/cortex-helm-chart/) and the [helm charts repository](https://github.com/cortexproject/cortex-helm-chart)
for comprehensive instructions, which includes
[supported parameters](https://github.com/cortexproject/cortex-helm-chart/blob/master/values.yaml)

Below is an example of how to use the helm chart, overriding the image with the
chainguard image:

```bash
helm repo add cortex-helm https://cortexproject.github.io/cortex-helm-chart
helm repo update

helm install cortex --namespace cortex cortex-helm/cortex \
 --set image.repository=cgr.dev/chainguard/cortex \
 --set image.tag=latest
```
<!--body:end-->

