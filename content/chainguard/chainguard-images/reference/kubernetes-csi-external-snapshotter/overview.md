---
title: "Image Overview: kubernetes-csi-external-snapshotter"
type: "article"
description: "Overview: kubernetes-csi-external-snapshotter Chainguard Image"
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

[cgr.dev/chainguard/kubernetes-csi-external-snapshotter](https://github.com/chainguard-images/images/tree/main/images/kubernetes-csi-external-snapshotter)

| Tag (s)   | Last Changed | Digest                                                                    |
|-----------|--------------|---------------------------------------------------------------------------|
|  `latest` | July 23rd    | `sha256:6eca29e69f0a6cf72f99f18f502c6ebfd311487927501df4d98a3a40ccecac6d` |



Kubernetes CSI External Snapshotter is a sidecar container that watches Kubernetes Snapshot CRD objects and triggers CreateSnapshot/DeleteSnapshot against a CSI endpoint.

## Get It

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/kubernetes-csi-external-snapshotter
```

