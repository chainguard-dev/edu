---
title: "Image Overview: node"
type: "article"
description: "Overview: node Chainguard Image"
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

[cgr.dev/chainguard/node](https://github.com/chainguard-images/images/tree/main/images/node)

| Tag (s)       | Last Changed   | Digest                                                                    |
|---------------|----------------|---------------------------------------------------------------------------|
|  `latest-dev` | September 11th | `sha256:9972eae79df1a1b16075e7e7b2b0fabed1e8aebf89dd57485a0ea6c021655af2` |
|  `latest`     | September 11th | `sha256:f940303eff83d6f956374ff7e108aa8d4f182c20a07467a07f3e247427b77adb` |



Minimal container image for running NodeJS apps

The image specifies a default non-root `node` user (UID 65532), and a working directory at `/app`, owned by that `node` user, and accessible to all users.

It specifies `NODE_PORT=3000` by default.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/node:latest
```

## Usage Example

Navigate to the [`example/`](https://github.com/chainguard-images/images/tree/main/images/node/example) directory:

```
cd example/
```

The Dockerfile is based on Docker's [Build your Node image](https://docs.docker.com/language/nodejs/build-images/) tutorial, but uses the Chainguard node base image instead.

Build the application on the node base image.

```
docker build \
  --tag node-docker \
  --platform=linux/amd64 \
  .
```

Then you can run the image:

```
docker run \
  --rm -it \
  -p 8000:8000 \
  --platform=linux/amd64 \
  node-docker
```

...and test to see that it works:

```
curl --request POST \
  --url http://localhost:8000/test \
  --header 'content-type: application/json' \
  --data '{"msg": "testing" }'
```

