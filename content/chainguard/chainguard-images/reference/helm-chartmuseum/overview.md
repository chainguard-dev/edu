---
title: "Image Overview: helm-chartmuseum"
type: "article"
description: "Overview: helm-chartmuseum Chainguard Image"
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

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | July 18th    | `sha256:1a0353cfdeb6ceb3c2df78186cb400c6dc0bdcb025cd528c469d8e2e7cb1d784` |
|  `latest`     | July 14th    | `sha256:0ed92c5ae2229336a500189e77f0e32ffd294f4470033dc146c76b67c47d44d9` |
|               | July 12th    | `sha256:d55c6814124ec11caf301be490b97640d8d831b48e1fdfb3512db74134ffac18` |



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

