---
title: "Image Overview: meilisearch"
type: "article"
description: "Overview: meilisearch Chainguard Image"
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

[cgr.dev/chainguard/meilisearch](https://github.com/chainguard-images/images/tree/main/images/meilisearch)

| Tag (s)   | Last Changed | Digest                                                                    |
|-----------|--------------|---------------------------------------------------------------------------|
|  `latest` | August 3rd   | `sha256:7aa211b4ec1c6308c7781283f17599b5bdfb41c7e8b4a19dae1b724dbb667200` |



Minimal meilisearch image.

The image specifies a default non-root `meilisearch` user (UID 999), and a data and dump directory at `/var/data.ms`, owned by that `meilisearch` user, accessible to all users.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/meilisearch:latest
```

## Usage Example

Run a meilisearch container with the following command:

```
docker run \
  --rm \
  -d \
  -p 7700:7700 \
  cgr.dev/chainguard/meilisearch:latest \
  --db-path /var/data.ms
  --dump-dir /var/data.ms/dumps \
  --http-addr 0.0.0.0:7700
```

Then you can follow the [meilisearch quick start guide](https://www.meilisearch.com/docs/learn/getting_started/quick_start#add-documents) and start adding documents.

