---
title: "buildkit Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the buildkit Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-19 00:54:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/buildkit/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/buildkit/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/buildkit/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/buildkit/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)            | Last Changed | Digest                                                                    |
|--------------------|--------------|---------------------------------------------------------------------------|
|  `latest-root-dev` | March 18th   | `sha256:bf47a374c3f22cfa602270f3bda0f2a9ecf879d2901db023d5d094965a23010c` |
|  `latest-root`     | March 18th   | `sha256:6a44ac7aa5513ed7f27f1e8ec956c2cb291723a71ee853567476f3895367a698` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0.13-dev` `0.13.1-dev` `0-dev` `latest-dev` | March 18th   | `sha256:206e340f9d45ae2531de57826c9a14e0a30d42d8f532a9087600a1e43837e934` |
|  `0.13` `latest` `0` `0.13.1`                 | March 18th   | `sha256:fa5119b239890a0095031498c9a7531f4a7caa9820e380f8104c27a4789600c2` |
|  `0.13.0-dev`                                 | March 18th   | `sha256:d60dce9606288013c6035a2f7c59b16b3fd4bf5663d420af6049f98660cce018` |
|  `0.13.0`                                     | March 18th   | `sha256:04473e9997f4b681540978caa6e8c95a5bb9cff988fb71e8000c36fae7aec439` |
|  `0.12-dev` `0.12.5-dev`                      | March 7th    | `sha256:eb2452151ab5c3adf7ee6f6d1f4dfd4a968e70234b83d642522e66703d244d2a` |
|  `0.12.5` `0.12`                              | March 7th    | `sha256:e132b011e8b5ac50ba5d5f602001286e59f82c4cb8348a83db7e5aff1f8a06f4` |

