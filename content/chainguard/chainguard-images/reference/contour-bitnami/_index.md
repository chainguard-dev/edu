---
title: "Image Overview: contour-bitnami"
linktitle: "contour-bitnami"
type: "article"
layout: "single"
description: "Overview: contour-bitnami Chainguard Image"
date: 2024-06-25 00:42:19
lastmod: 2024-06-25 00:42:19
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/contour-bitnami/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/contour-bitnami/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/contour-bitnami/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/contour-bitnami/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Contour is an ingress controller for Kubernetes that works by deploying the Envoy proxy as a reverse proxy and load balancer. Contour supports dynamic configuration updates out of the box while maintaining a lightweight profile.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/contour-bitnami:latest
```


<!--body:start-->


### Usage

To deploy Contour with the Bitnami variant using the Helm chart, follow these steps:

#### Add the Bitnami Helm repository

```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
```

#### Install the Contour Helm chart

```bash
helm install contour bitnami/contour \
    --set contour.image.registry="cgr.dev" \
    --set contour.image.repository="chainguard/contour-bitnami" \
    --set contour.image.tag=latest
```

#### Test it out!

You should see the following:

* 2 Contour pods each with status Running and 1/1 Ready
* 1+ Envoy pod(s), each with the status Running and 2/2 Ready

Now that you have installed Contour and Envoy, let’s install a web application workload and get some traffic flowing to the backend.

To install httpbin, run the following:

```bash
kubectl apply -f https://projectcontour.io/examples/httpbin.yaml
```

Verify the pods and services are running:

```bash
kubectl get po,svc,ing -l app=httpbin
```

You should see the following:

* 3 instances of pods/httpbin, each with status Running and 1/1 Ready
* 1 service/httpbin CLUSTER-IP listed on port 80
* 1 Ingress on port 80


NOTE: The Helm install configures Contour to filter Ingress and HTTPProxy objects based on the contour IngressClass name. If using Helm, ensure the Ingress has an ingress class of contour with the following:

```bash
kubectl patch ingress httpbin -p '{"spec":{"ingressClassName": "contour"}}'
```

Next, we can `kubectl port-forward` to get traffic to Envoy:

```bash
kubectl -n projectcontour port-forward service/contour-envoy 8888:80
```

In a browser or via curl, make a request to http://local.projectcontour.io:8888

```bash
curl -s http://local.projectcontour.io:8888/
```

Congratulations, you have installed Contour, deployed a backend application, created an Ingress to route traffic to the application, and successfully accessed the app with Contour!

For further next steps, you can also continue with [official docs](https://projectcontour.io/getting-started/#next-steps) to play around

<!--body:end-->

