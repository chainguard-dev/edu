---
title: "falcoctl Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the falcoctl Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-12 00:55:01
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/falcoctl/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/falcoctl/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/falcoctl/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/falcoctl/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | March 11th   | `sha256:99b601e5f9dfd107465966e29a550b80a12e770b2a55b1fc0fc01fabcc5c6f80` |
|  `latest`     | March 9th    | `sha256:3709bf7dae9e7a8c8a3b9596e4589ae2f0e4f6e000a9734442f517c81821e3fd` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0.7-dev` `0-dev` `0.7.3-dev` `latest-dev` | March 10th   | `sha256:5f0cd12ce0c9b74766ead6b6f89ed99978e6da0d32371e38e6d26cb406eda603` |
|  `0` `0.7.3` `0.7` `latest`                 | March 8th    | `sha256:346970d43eb22783cfc7d256f3dd8f5036272c53f2296da6d9eb6b012dbf0fbe` |

