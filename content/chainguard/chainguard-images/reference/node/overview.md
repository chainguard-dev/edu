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
|               | July 18th    | `sha256:c41d69ec8d938d693ffbc812dd34cfabc874f5dbc3d312c0ee8da847f60db9eb` |
|               | July 18th    | `sha256:b1d87ebfd90198dfed10a38f20bfc78241adb77e8ab1ae0aa8ef33d2f3558117` |
|               | July 18th    | `sha256:f4c712953222187dc861c53ea6c53c1cc8b4d44fec988916778523c53248e9af` |
|  `latest-dev` | July 18th    | `sha256:3bf0d16b4a77a6381a2b3ca844a4aad421e9dd41bbb432d9d7e4a4296c44b30e` |
|               | July 18th    | `sha256:7b1cf5bbd194b0d808fa4b93bcc59246477e67dd0a4afbd4680e65d4900c7ac7` |
|  `latest`     | July 18th    | `sha256:9b4310b99d50cc4c30a3ded94fc8a962f987ed1a1c9ba4f058c95cc7e766908e` |
|               | July 4th     | `sha256:5d3aa26fffd3cf21fdc200144675ab909e3a5ffd2b7cad98da6a29694e1568c7` |
|               | July 4th     | `sha256:e41414b4bd7b773159e3fa0781e37d22c580fb31bf91c945916db3bf2a6b35a1` |



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

