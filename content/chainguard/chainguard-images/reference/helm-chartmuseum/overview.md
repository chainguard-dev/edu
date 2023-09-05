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

| Tag (s)       | Last Changed  | Digest                                                                    |
|---------------|---------------|---------------------------------------------------------------------------|
|  `latest-dev` | September 4th | `sha256:5708ae6ddf0160c900be408cf41ab9d8866dfd55def75ccfc10414c929464626` |
|  `latest`     | September 4th | `sha256:86a2d08471c56dc0b99be403adfcaf7226b318553d58ea25c58a040207217a14` |



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

