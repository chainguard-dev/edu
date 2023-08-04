---
title: "Image Overview: zot"
type: "article"
description: "Overview: zot Chainguard Image"
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

[cgr.dev/chainguard/zot](https://github.com/chainguard-images/images/tree/main/images/zot)

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | August 3rd   | `sha256:0b3e8f813d46c33ab4ec7634bd93141281e4469570163e90c973cc0d6ed532d6` |
|  `latest-dev` | August 3rd   | `sha256:e3598ab4635a361691b6255328c02940759b6ee0035b81c0b9a9598f792d64fc` |



Minimal image with
[zot](https://github.com/project-zot/zot)
binary. **EXPERIMENTAL**

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/zot:latest
```

## Usage

Create a zot config file:

```
cat <<EOF > zot-config.yaml
distspecversion: 1.1.0-dev
http:
  address: 0.0.0.0
  port: 5000
storage:
  rootdirectory: /var/lib/zot/data
EOF
```

Create a fresh `data` directory (this will store all OCI blobs as
[OCI Image Layout](https://github.com/opencontainers/image-spec/blob/main/image-layout.md)):

```
rm -rf data && mkdir data && chmod go+wrx data
```

Run the server:

```
docker run --rm -p 5000:5000 \
  -v "${PWD}/zot-config.yaml":/zot-config.yaml \
  -v "${PWD}/data":/var/lib/zot/data \
  cgr.dev/chainguard/zot:latest \
  serve /zot-config.yaml
```

Then in another terminal, try pushing an image with crane:
```
crane cp \
  cgr.dev/chainguard/bash:latest \
  localhost:5000/demo:latest
```

Then try pulling and running the image:
```
docker run --rm \
  localhost:5000/demo:latest \
  -c 'echo hello world'
```

