---
title: "gradle Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the gradle Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-03 00:46:08
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/gradle/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/gradle/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/gradle/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/gradle/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)   | Last Changed | Digest                                                                    |
|-----------|--------------|---------------------------------------------------------------------------|
|  `latest` | May 31st     | `sha256:a29b29f5d8a91bf8ca9073b9e4729b1528f081fd75744a95c1487e2a0ba49dd5` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-17-8.7.0-dev` `openjdk-17-8-dev` `openjdk-17-dev` `openjdk-17-8.7-dev`              | June 1st     | `sha256:2f06ce1f06965505d389cea2da2059f15f8dc5003a6b3a3a812f9b7cf64a9e51` |
|  `latest-dev` `openjdk-21-dev` `openjdk-21-8-dev` `openjdk-21-8.7-dev` `openjdk-21-8.7.0-dev` | June 1st     | `sha256:8b4e75699fbaa26b82391389f04fa6d833d1715773ba5e97242ec0b86fd54960` |
|  `openjdk-17-8` `openjdk-17` `openjdk-17-8.7.0` `openjdk-17-8.7`                              | May 30th     | `sha256:f2f696cf729967c513cfdcb1e39b876f96505d892a7cae5aa424872e84bc4237` |
|  `latest` `openjdk-21-8.7` `openjdk-21-8.7.0` `openjdk-21` `openjdk-21-8`                     | May 30th     | `sha256:efabacf0bddd8b6e5b07b55b8c7ca71abf660437e88d40009c7dcf3a66f5fc55` |

