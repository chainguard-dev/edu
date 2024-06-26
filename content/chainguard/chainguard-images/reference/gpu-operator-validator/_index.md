---
title: "Image Overview: gpu-operator-validator"
linktitle: "gpu-operator-validator"
type: "article"
layout: "single"
description: "Overview: gpu-operator-validator Chainguard Image"
date: 2024-06-26 00:35:03
lastmod: 2024-06-26 00:35:03
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/gpu-operator-validator/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/gpu-operator-validator/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/gpu-operator-validator/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/gpu-operator-validator/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal [gpu-operator-validator](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/cloud-native/containers/gpu-operator-validator) container image for gpu-operator-validator.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/gpu-operator-validator:latest
```


<!--body:start-->
## Usage
NVIDIA GPU Operator creates/configures/manages GPUs atop Kubernetes and automates tasks related to bootstrapping GPU nodes.

The `gpu-operator-validator` image provides the validator for NVIDIA GPU Operator, which runs as a Daemonset and ensures that all components are working as expected on all GPU nodes. This needs to be run on a VM which has GPU support, or a kind cluster which supports GPUs.

## Helm Installation for GPU-Operator
You can configure the GPU Operator Validator using the Helm chart
```shell
$ helm repo add nvidia https://helm.ngc.nvidia.com/nvidia \
    && helm repo update
$ helm upgrade --install gpu-operator nvidia/gpu-operator \
    --set validator.repository=<cgr-registry> \
    --set validator.image=gpu-operator-validator \
    --set validator.version=latest \
    --set operator.repository=<cgr-registry> \
    --set operator.image=gpu-operator \
    --set operator.version=latest-dev
 ```

It might take a couple of minutes for all the pods and deamonsets to be created. Once created you may verify them by looking for the following:

### Verify Deployments and Daemonsets

```
$ kubectl get pods
NAME                                                          READY   STATUS      RESTARTS   AGE
gpu-feature-discovery-pdhdn                                   1/1     Running     0          10m
gpu-operator-6cf77ccd94-jv2dm                                 1/1     Running     0          11m
gpu-operator-node-feature-discovery-gc-7b4fd865f4-578fw       1/1     Running     0          11m
gpu-operator-node-feature-discovery-master-5dff7dbb89-xzsc8   1/1     Running     0          11m
gpu-operator-node-feature-discovery-worker-65gvq              1/1     Running     0          11m
nvidia-container-toolkit-daemonset-zkpsh                      1/1     Running     0          10m
nvidia-cuda-validator-jhz7l                                   0/1     Completed   0          10m
nvidia-dcgm-exporter-vg5wz                                    1/1     Running     0          10m
nvidia-device-plugin-daemonset-gbmd4                          1/1     Running     0          10m
nvidia-operator-validator-qb22l                               1/1     Running     0          10m


# Verify GPU Feature Discovery Deployments
$ kubectl get deploy -l app.kubernetes.io/name=node-feature-discovery

# Verify GPU Feature Discovery Daemonset
$ kubectl get daemonset -l app.kubernetes.io/name=node-feature-discovery

# Verify GPU Operator Deployment
$ kubectl get rs -l app.kubernetes.io/name=gpu-operator
```

For more information, refer to the documentation:
- https://github.com/NVIDIA/gpu-operator/tree/main/deployments/gpu-operator
- https://catalog.ngc.nvidia.com/orgs/nvidia/teams/cloud-native/containers/gpu-operator-validator

