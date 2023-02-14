---
title: "Image Overview: deno"
type: "article"
description: "Overview: deno Chainguard Images"
date: 2022-11-01T11:07:52+02:00
lastmod: 2022-11-01T11:07:52+02:00
draft: false
images: []
menu:
  docs:
    parent: "images-reference"
weight: 600
toc: true
---

`experimental` [cgr.dev/chainguard/deno](https://github.com/chainguard-images/images/tree/main/images/deno)
| Tags     | Aliases                    |
|----------|----------------------------|
| `latest` | 1, 1.30, 1.30.3, 1.30.3-r0 |



Minimal container image for running deno apps

The image specifies a default non-root `deno` user (UID 65532), and a working directory at `/app`, owned by that `deno` user, and accessible to all users.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/deno:latest
```

## Usage Example

Navigate to the [`example/`](./example/) directory:

```
cd example/
```

The Dockerfile is based on [Deno's webserver tutorial](https://deno.land/manual@v1.28.3/examples/http_server), but packages it up into a Chainguard deno image.

Build the application on the deno base image.

```
docker build \
  --tag deno-docker \
  .
```

Then you can run the image:

```
docker run \
  --rm -it \
  -p 8080:8080 \
  deno-docker
```

...and test to see that it works:

```
$ curl localhost:8080
Your user-agent is:

curl/7.84.0%
```
