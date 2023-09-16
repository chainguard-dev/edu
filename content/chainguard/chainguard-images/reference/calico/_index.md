---
title: "Image Overview: calico"
linktitle: "calico"
type: "article"
layout: "single"
description: "Overview: calico Chainguard Image"
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

{{< tabs >}}
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/calico/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/calico/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/calico/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/calico/provenance_info/" >}}
{{</ tabs >}}



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
      # crane digest cgr.dev/chainguard/calico-node:latest
      digest: $node_digest
    - image: calico/cni
      # crane digest cgr.dev/chainguard/calico-cni:latest
      digest: $cni_digest
    - image: calico/kube-controllers
      # crane digest cgr.dev/chainguard/calico-kube-controllers:latest
      digest: $calico-kube-controllers
    - image: calico/pod2daemon-flexvol
      # crane digest cgr.dev/chainguard/calico-pod2daemon-flexvol:latest
      digest: $calico-pod2daemon-flexvol
    - image: calico/csi
      # crane digest cgr.dev/chainguard/calico-csi:latest
      digest: $calico-csi
    - image: calico/typha
      # crane digest cgr.dev/chainguard/calico-typha:latest
      digest: $calico-typha
    - image: calico/node-driver-registrar
      # crane digest cgr.dev/chainguard/calico-node-driver-registrar:latest
      digest: $calico-node-driver-registrar
    # This isn't used on Linux, it just needs to have a value.
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

