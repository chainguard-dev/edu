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
|  `latest-dev` | August 3rd   | `sha256:2cdc58c697749f97318df326834cd9c6a83f43fe3985421d6032b006457caebe` |
|  `latest`     | July 26th    | `sha256:d9d0e955b4853d505722d24b5aa2e97cde7363a1ffb4c44e9a33cc92a25b36fa` |



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

