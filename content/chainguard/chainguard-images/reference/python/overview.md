---
title: "Image Overview: python"
type: "article"
description: "Overview: python Chainguard Images"
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

`stable` [cgr.dev/chainguard/python](https://github.com/chainguard-images/images/tree/main/images/python)
| Tags         | Aliases                                            |
|--------------|----------------------------------------------------|
| `3.10`       | `3.10`, `3.10.11`, `3.10.11-r0`                    |
| `3.10-dev`   | `3.10-dev`, `3.10.11-dev`, `3.10.11-r0-dev`        |
| `latest`     | `3`, `3.11`, `3.11.3`, `3.11.3-r0`                 |
| `latest-dev` | `3-dev`, `3.11-dev`, `3.11.3-dev`, `3.11.3-r0-dev` |



This is a minimal Python image based on Wolfi.

While this image is being developed, we will stick to the latest stable Python version. Supported versions in the long term are TBD.

## Get It!

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

