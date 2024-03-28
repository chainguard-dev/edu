---
title: "buildkit Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the buildkit Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-28 00:50:32
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
|  `latest-root-dev` | March 21st   | `sha256:f9cb1d4232bbed67075bc6c4e1edcface3de7d68a80e81f438e8baa00c2ce64e` |
|  `latest-root`     | March 21st   | `sha256:6847e448d058d8788306c617fa59309682647eea33a9683b3898c16c6ec32f7d` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0.13.1` `0.13` `0` `latest`                 | March 27th   | `sha256:d4ee0f7058b2e894a4df8e334fc2dd3c741d9d5bbf146cc598e792075a39a083` |
|  `0.13-dev` `0-dev` `latest-dev` `0.13.1-dev` | March 27th   | `sha256:9f90fefce55c2a128837a028862676a039c5784bdf1406b54885143d59a57a96` |
|  `0.13.0-dev`                                 | March 18th   | `sha256:d60dce9606288013c6035a2f7c59b16b3fd4bf5663d420af6049f98660cce018` |
|  `0.13.0`                                     | March 18th   | `sha256:04473e9997f4b681540978caa6e8c95a5bb9cff988fb71e8000c36fae7aec439` |
|  `0.12-dev` `0.12.5-dev`                      | March 7th    | `sha256:eb2452151ab5c3adf7ee6f6d1f4dfd4a968e70234b83d642522e66703d244d2a` |
|  `0.12.5` `0.12`                              | March 7th    | `sha256:e132b011e8b5ac50ba5d5f602001286e59f82c4cb8348a83db7e5aff1f8a06f4` |

