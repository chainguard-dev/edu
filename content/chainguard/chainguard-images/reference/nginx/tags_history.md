---
title: "nginx Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the nginx Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-19 00:54:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/nginx/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/nginx/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/nginx/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/nginx/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | March 18th   | `sha256:b2f1979f26c75879f9f85622e93f686a849b2221ca7b82b7d362e44ad2c04f98` |
|  `latest-dev` | March 18th   | `sha256:84c925edb61499461aa2a7e9e36266ea6cb019996a1edcb6da2564df35da15b9` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.25.4-dev` `1-dev` `latest-dev` `1.25-dev` | March 18th   | `sha256:28fe2bb8e225105d1f0791e52048aa0c9b2572d0bc0d264f752915d8f1236c27` |
|  `1.24-dev` `1.24.0-dev`                      | March 18th   | `sha256:e63efdad35d2ad01fd0b7bb3e5cdd8b56bf56dc834565b4007bce56d65a261c2` |
|  `1.25.4` `mainline` `1.25` `1` `latest`      | March 18th   | `sha256:f7cbbe9b43c1d7e4ccc6c0d9c5abe7b1c40aa4f2da50d5ee6cca3c0c4bb54244` |
|  `1.24` `stable` `1.24.0`                     | March 18th   | `sha256:93cca6e273caebecfa3d3bb4853572e9b0c3fd079395056eb103dd023d110ef8` |

