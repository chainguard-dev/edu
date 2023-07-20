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
|  `latest-dev` | July 19th    | `sha256:01e36672bafd0326dcecd77bda21f19e04da33d92bd4521efe5ff42a19af7692` |
|  `latest`     | July 14th    | `sha256:d12a953a042f5a484eca29fca3df32d002f193f156f4ace82b2e9e37585d2853` |



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

