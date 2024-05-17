---
title: "opentelemetry-collector Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the opentelemetry-collector Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-17 00:44:46
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/opentelemetry-collector/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/opentelemetry-collector/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/opentelemetry-collector/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/opentelemetry-collector/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 16th     | `sha256:8a5ba2cd1140b60d5fd1d090c228d839baa7699445944eeda2dd990bc6d72cbb` |
|  `latest`     | May 15th     | `sha256:af7b985a14854a6355672011c110c700d490d5d216058baa1498b94385301d0f` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                         | Last Changed | Digest                                                                    |
|-------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0.100.0-dev` `0-dev` `0.100-dev` `latest-dev` | May 16th     | `sha256:5f6c267e5a27c1f374e22a37d8cf4dc3fa42b1ce0a7b2ad795028e3e91d7f21c` |
|  `0` `0.100.0` `0.100` `latest`                 | May 15th     | `sha256:d698d074a8fab9bdc1552c6588e723392e6c922122aa0f5cf6d8a2dcb4efb728` |
|  `0.99.0-dev` `0.99-dev`                        | May 2nd      | `sha256:426134a7a289f9afe3b728103cacdb83437bb707653aada28f57fe1248380c7a` |
|  `0.99` `0.99.0`                                | May 2nd      | `sha256:fd4edcdf64de8cfda943de5887d3a77d78c9fb9eeabceb281e38b693064dffbc` |

