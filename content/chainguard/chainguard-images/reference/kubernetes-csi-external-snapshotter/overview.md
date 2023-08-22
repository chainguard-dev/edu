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
|  `latest` | August 15th  | `sha256:e76063ae1c84f46489a058af912d3e5506b6ffb7a0bcaed435ebc1e279b59059` |



Kubernetes CSI External Snapshotter is a sidecar container that watches Kubernetes Snapshot CRD objects and triggers CreateSnapshot/DeleteSnapshot against a CSI endpoint.

## Get It

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/kubernetes-csi-external-snapshotter
```

