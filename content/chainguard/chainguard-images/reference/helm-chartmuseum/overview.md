---
title: "Image Overview: Helm-chartmuseum"
type: "article"
description: "Overview: Helm-chartmuseum Chainguard Image"
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

[cgr.dev/chainguard/helm-chartmuseum](https://github.com/chainguard-images/images/tree/main/images/helm-chartmuseum)

| Tag          | Last Updated | Digest                                                                    |
|--------------|--------------|---------------------------------------------------------------------------|
| `latest`     | 20 hours ago | `sha256:af6b780ae104e11ac317e4a2204cf2581bca507b8b4ce78f3ec17c81fe70cff7` |
| `latest-dev` | 20 hours ago | `sha256:089fdd9341de0d8e33273490ad8bce083ff96ca6c6bd147e96de88e9981401f9` |



Minimal image with
[chartmuseum](https://github.com/helm/chartmuseum)
binary. **EXPERIMENTAL**

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/chartmuseum:latest
```

## Usage

Create a helm chart, and package it into a `charts/` directory:

```
helm create hello
mkdir charts/
helm package hello -d ./charts
```

Start the chartmuseum server:

```
docker run --rm -p 8080:8080 -v $(pwd)/charts:/charts \
  cgr.dev/chainguard/chartmuseum:latest
```

From another terminal, use it as a helm repository:
```
helm repo add chartmuseum http://localhost:8080
helm search repo chartmuseum/
helm upgrade --install chartmuseum-demo chartmuseum/hello
```
