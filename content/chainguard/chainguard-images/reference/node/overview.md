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

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | August 17th  | `sha256:1611317f57819302818b8283f4cccceff3d1180ca6c2a64944a0916fb4f57daa` |
|  `latest`     | August 17th  | `sha256:1503cb6568807812370f77f0f2dbe416291c1f6e24eff555c1fb92165899bb86` |



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

