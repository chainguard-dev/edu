---
title: "opentelemetry-collector-contrib Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the opentelemetry-collector-contrib Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-14 00:37:02
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/opentelemetry-collector-contrib/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/opentelemetry-collector-contrib/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/opentelemetry-collector-contrib/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/opentelemetry-collector-contrib/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | March 13th   | `sha256:ca03cbaded5be6a9fc0ec77915fea82084f4fec03e257e2d3f594d8b5e0a48c6` |
|  `latest`     | March 8th    | `sha256:172376ea490e3fe504ff64b44f7668767148f2a3a5e0f8a9e4b9d6848f2e6b8c` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed  | Digest                                                                    |
|-----------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `0-dev` `latest-dev` `0.96-dev` `0.96.0-dev` | March 13th    | `sha256:5c0409cef922117fcfb8e740ae6a61eb8e5784df2c70d6ec01db54a3435d521f` |
|  `0.96` `latest` `0` `0.96.0`                 | March 8th     | `sha256:6d817b1d079ec78a6c1ab96dc1814af29f87d1441f77da0a7ad70a5194b87ec7` |
|  `0.95-dev` `0.95.0-dev`                      | March 2nd     | `sha256:7d4d2f332b473f2e304a83c04f1d0af177e1acd67c74b24d79879a2e09f5036e` |
|  `0.95` `0.95.0`                              | February 26th | `sha256:15567c4d6e35e753141ab2d27b2048b3b31797ad499f72727a7c2fa614451b40` |
|  `0.94.0-dev` `0.94-dev`                      | February 17th | `sha256:810f71c878acc0b982df2c1aed99ee457ea2ca2bf9a7b25e80416eecd85fe488` |

