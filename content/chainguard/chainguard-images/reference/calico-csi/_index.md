---
title: "Image Overview: calico-csi"
linktitle: "calico-csi"
type: "article"
layout: "single"
description: "Overview: calico-csi Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2023-11-29 00:31:44
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/calico-csi/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/calico-csi/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/calico-csi/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/calico-csi/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
[Calico](https://projectcalico.docs.tigera.io/) is a networking and security solution that enables Kubernetes workloads and non-Kubernetes/legacy workloads to communicate seamlessly and securely.
<!--overview:end-->

<!--getting:start-->
## Get It!
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/calico:latest
```
<!--getting:end-->

<!--body:start-->
## Installation

There are several ways to install Calico. This document follows the upstream recommended way with the `tigera-operator` ([ref](https://docs.tigera.io/calico/latest/getting-started/kubernetes/quickstart#install-calico)).

There are two CRDs involved that work together to use the correct Chainguard Images:

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

The above combination of `ImageSet` and `Installation` can be used as a drop in replacement for the [upstream documentation](https://docs.tigera.io/calico/latest/getting-started/kubernetes/quickstart#install-calico) step 2 (`custom-resources.yaml`) to correctly rename the Calico images to their `cgr.dev` variants.
<!--body:end-->

