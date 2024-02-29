---
title: "Image Overview: python-fips"
linktitle: "python-fips"
type: "article"
layout: "single"
description: "Overview: python-fips Chainguard Image"
date: 2024-02-29 16:25:55
lastmod: 2024-02-29 16:25:55
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/python-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/python-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/python-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/python-fips/provenance_info/" >}}
{{</ tabs >}}

Minimal FIPS-enabled images for python.

## Get It

This image provides these versions of python:

- `3.10`
- `3.11`
- `3.12`

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/python-fips:3.10
```

## Testing

* Step 1: `cd images/python-fips/fips-example/`

* Step 2: Replace the content of Dockerfile with the below:

    ```Dockerfile
    FROM cgr.dev/chainguard-private/python-fips:3.10

    WORKDIR /app

    COPY . .

    USER root

    CMD ["./fips-check.py"]
    ```
* Step 3: `docker build -t fips-python:0.0.1 .`

* Step 4: `docker run --rm fips-python:0.0.1 2>&1 >/dev/null | grep "\[digital envelope routines\] unsupported"`

Since MD5 isn't supported when we enable FIPS, the script we run inside container should throw up an error which we
redirect using `2>&1` and it should output something like '[digital envelope routines] unsupported'

