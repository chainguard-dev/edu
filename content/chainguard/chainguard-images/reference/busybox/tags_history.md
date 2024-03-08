---
title: "busybox Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the busybox Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-08 00:56:03
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/busybox/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/busybox/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/busybox/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/busybox/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)         | Last Changed | Digest                                                                    |
|-----------------|--------------|---------------------------------------------------------------------------|
|  `latest-glibc` | March 7th    | `sha256:678b013f85d46a8dd43d6cdca80fd958b622a3bd272324c3cdc06c551063faa4` |
|  `latest`       | March 4th    | `sha256:34a6f3bc2bdfa828b1360041113862d9248e2654d0d623799e89c6ccdc5ec982` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                               | Last Changed  | Digest                                                                    |
|-------------------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `glibc-1.36.1` `glibc-1.36` `glibc-1` `latest-glibc` | March 7th     | `sha256:17e10e5a21a7fab0f7392a8ea2406919c41ee79eb794f957eab8fdf356ff029a` |
|  `latest`                                             | February 16th | `sha256:6799955dbd3396e9670859a42c16e6d17f963aacb264b25b6e99930590c09208` |

