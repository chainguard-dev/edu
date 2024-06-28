---
title: "Image Overview: calico-key-cert-provisioner"
linktitle: "calico-key-cert-provisioner"
type: "article"
layout: "single"
description: "Overview: calico-key-cert-provisioner Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-06-28 00:31:38
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/calico-key-cert-provisioner/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/calico-key-cert-provisioner/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/calico-key-cert-provisioner/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/calico-key-cert-provisioner/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
[Calico](https://projectcalico.docs.tigera.io/) is a networking and security solution that enables Kubernetes workloads and non-Kubernetes/legacy workloads to communicate seamlessly and securely.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/calico-key-cert-provisioner:latest
```


<!--body:start-->
## Installation

There are several ways you can install Calico onto a Kubernetes cluster. This document follows method recommended in the [official Calico documentation](https://docs.tigera.io/calico/latest/getting-started/kubernetes/quickstart#install-calico) which involves using the Tigera Calico operator. 

After setting up and connecting to the Kubernetes cluster where you want to install Calico, install the Tigera Calico operator and custom resource definitions (CRDs).

```shell
kubectl create -f https://raw.githubusercontent.com/projectcalico/calico/v3.26.4/manifests/tigera-operator.yaml
```

Then apply the following YAML manifest to create two CRDs.

```yaml
---
# ImageSet
apiVersion: operator.tigera.io/v1
kind: ImageSet
metadata:
  name: calico-v3.26.1
spec:
  images:
    - image: calico/node
      digest: ... # Replace with $(crane digest cgr.dev/chainguard/calico-node:latest)
    - image: calico/cni
      digest: ... # Replace with $(crane digest cgr.dev/chainguard/calico-cni:latest)
    - image: calico/kube-controllers
      digest: ... # Replace with $(crane digest cgr.dev/chainguard/calico-kube-controllers:latest)
    - image: calico/pod2daemon-flexvol
      digest: ... # Replace with $(crane digest cgr.dev/chainguard/calico-pod2daemon-flexvol:latest)
    - image: calico/csi
      digest: ... # Replace with $(crane digest cgr.dev/chainguard/calico-csi:latest)
    - image: calico/typha
      digest: ... # Replace with $(crane digest cgr.dev/chainguard/calico-typha:latest)
    - image: calico/node-driver-registrar
      digest: ... # Replace with $(crane digest cgr.dev/chainguard/calico-node-driver-registrar:latest)
    # This isn't used on Linux, but it needs to have a value containing a valid digest.
    - image: calico/windows-upgrade
      digest: sha256:0000000000000000000000000000000000000000000000000000000000000000

---
# Installation
apiVersion: operator.tigera.io/v1
kind: Installation
metadata:
  name: default
spec:
  variant: Calico
  registry: cgr.dev
  imagePath: chainguard
  imagePrefix: calico-
```

The combination of these `ImageSet` and `Installation` CRDs serve as a drop in replacement for [Step 2 of the upstream documentation](https://docs.tigera.io/calico/latest/getting-started/kubernetes/quickstart#install-calico). Together, these correctly rename the Calico images to their `cgr.dev` variants.

After creating the CRDs, you can ensure that the pods are running with a command like the following.

```shell
kubectl get pods -n calico-system
```
<!--body:end-->

