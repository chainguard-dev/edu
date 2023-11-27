---
title: "Image Overview: smarter-device-manager"
linktitle: "smarter-device-manager"
type: "article"
layout: "single"
description: "Overview: smarter-device-manager Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2023-11-27 16:34:14
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/smarter-device-manager/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/smarter-device-manager/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/smarter-device-manager/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/smarter-device-manager/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimalist Wolfi-based image for smarter device manager.
<!--overview:end-->

<!--getting:start-->
## Get It!
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/smarter-device-manager:latest
```
<!--getting:end-->

<!--body:start-->

Smarter-device-manager is a Kubernetes tool designed for IoT applications,
enabling containers to securely access host devices like sensors, actuators,
and various hardware interfaces.


## Usage

### Manifests
Deploy using one of the example manifests provided in the upstream projects
Gitlab repository: [Smart Device Manager](https://gitlab.com/arm-research/smarter/smarter-device-manager).

> If using one of the manifests from the upstream repository, you'll need to
change the `config` mountPath to `/etc/smarter-device-manager`(in place of /root/config).

### Helm chart

The following helm chart can be used:
[helm chart](https://github.com/gabe565/charts/tree/main/charts/smarter-device-manager).

You'll need to override the image and tag:

```bash
helm repo add gabe565 https://charts.gabe565.com
helm repo update
helm install smart-device-manager gabe565/smarter-device-manager \
 --set image.repository=cgr.dev/chainguard/smarter-device-manager --set image.tag=latest
```
<!--body:end-->

