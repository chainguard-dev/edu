---
title: "Image Overview: crane"
type: "article"
description: "Overview: crane Chainguard Image"
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

[cgr.dev/chainguard/crane](https://github.com/chainguard-images/images/tree/main/images/crane)

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | August 31st  | `sha256:7840c794f1028c0b031efe6d5a7f2cd30447de56892c80738d24207b57ce1422` |
|  `latest`     | August 31st  | `sha256:3bb826321523b7a021f221d7d0a6514fa35e321a445dec42dbde8a14777d30b2` |



Minimalist Wolfi-based crane image for interacting with registries.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/crane:latest
```

## Usage

Inspect the crane image manifest using the crane image:

```
docker run --rm cgr.dev/chainguard/crane:latest manifest cgr.dev/chainguard/crane:latest
```

