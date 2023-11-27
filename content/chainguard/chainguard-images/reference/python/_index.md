---
title: "Image Overview: python"
linktitle: "python"
type: "article"
layout: "single"
description: "Overview: python Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/python/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/python/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/python/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/python/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal Python image based on Wolfi.
<!--overview:end-->

<!--getting:start-->
## Get It!
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/python:latest
```
<!--getting:end-->

<!--body:start-->
## Variants

We have two images available: a `python:latest-dev` variant that contains `pip` and a shell, and a minimal runtime image that just contains
python itself.

These images are available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/python:latest
docker pull cgr.dev/chainguard/python:latest-dev
```

## Usage

The python image can be used directly for simple cases, or with a multi-stage build using python-dev as the build container.

```Dockerfile
FROM cgr.dev/chainguard/python:latest-dev as builder

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt --user

FROM cgr.dev/chainguard/python:latest

WORKDIR /app

# Make sure you update Python version in path
COPY --from=builder /home/nonroot/.local/lib/python3.11/site-packages /home/nonroot/.local/lib/python3.11/site-packages

COPY main.py .

ENTRYPOINT [ "python", "/app/main.py" ]
```
<!--body:end-->

