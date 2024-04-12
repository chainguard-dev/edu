---
title: "buildkit Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the buildkit Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-12 00:54:01
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
|  `latest-root-dev` | April 11th   | `sha256:36aec40a9bb41fa43fdc1674df9c9b1192154ba5caf858bf6df66a636fda6bf8` |
|  `latest-root`     | April 4th    | `sha256:327baefb50003be2bb5f767188c3a3986c6ee69b9b39901648888cf4a9a30d97` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0.13.1-dev` `latest-dev` `0.13-dev` `0-dev` | April 11th   | `sha256:b7e724177d7da5b44677aaf5bcddcd8d38af5df33e24fc347f6a0c1521dc489c` |
|  `0.13` `0` `0.13.1` `latest`                 | April 4th    | `sha256:99f3a9c5b16b925b4bcca2790a7b9610a5d1de4a2faf20d5200a95e971054127` |
|  `0.13.0-dev`                                 | March 18th   | `sha256:d60dce9606288013c6035a2f7c59b16b3fd4bf5663d420af6049f98660cce018` |
|  `0.13.0`                                     | March 18th   | `sha256:04473e9997f4b681540978caa6e8c95a5bb9cff988fb71e8000c36fae7aec439` |

