---
title: "gitness Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the gitness Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-02 00:37:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/gitness/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/gitness/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/gitness/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/gitness/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 29th   | `sha256:c2c5a09c6de8b85a91d5feee41666a250eb5f6b0a7c9c69308324570a751156b` |
|  `latest`     | April 29th   | `sha256:5c98b9279ba7cc2e091fae356e47e3b63579c2d8fd6f58a802f6a493caac9b7d` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                           | Last Changed | Digest                                                                    |
|---------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `3` `3.0` `3.0.0_beta6` `latest`                 | May 1st      | `sha256:a1c25a96e75c67ecd245b7820793ed1149b9e8aa042a0bdf1ac09a875a9bb24e` |
|  `latest-dev` `3-dev` `3.0-dev` `3.0.0_beta6-dev` | May 1st      | `sha256:a41b41cb1afa552f8c118d35d1d256678f3f8d12683a3657719142da72c0f7a9` |

