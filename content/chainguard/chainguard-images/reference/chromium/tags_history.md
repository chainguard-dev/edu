---
title: "chromium Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the chromium Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-28 00:50:32
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/chromium/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/chromium/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/chromium/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/chromium/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | March 25th   | `sha256:0b5053c3fce6dfc48246ed7100b5a502eeed53c74f279c290fc94cf7d53d9799` |
|  `latest`     | March 25th   | `sha256:66a317d5f0234b0a02fdf0d6769f97d3fd8597d6f3b0fa988e59987c215fb909` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                  | Last Changed | Digest                                                                    |
|--------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `123.0.6312-dev` `latest-dev` `123.0-dev` `123-dev` `123.0.6312.86-dev` | March 27th   | `sha256:4203c4557202269913076cf7013d86a7732d3a1768dc56e0637a699ba68046c5` |
|  `123.0.6312` `123` `123.0.6312.86` `latest` `123.0`                     | March 27th   | `sha256:e327796e1be9eb2986f676e95dd48a5bce5fb365147acdede69a4b281d336655` |
|  `123.0.6312.58-dev`                                                     | March 27th   | `sha256:bfb3e3cb70016bb4792b00d7021925de744ea1387959298964b79f06d3eccb61` |
|  `123.0.6312.58`                                                         | March 27th   | `sha256:28acf6ada311ea8bfd2385f82e00f52937575516ead9ab72100a8b57e1ce9551` |
|  `122.0.6261` `122.0` `122` `122.0.6261.128`                             | March 18th   | `sha256:205efdb878b9493fbc8320f7d1a882cb93c7513159488189b747d6175f238e9b` |
|  `122.0.6261.128-dev` `122.0.6261-dev` `122-dev` `122.0-dev`             | March 18th   | `sha256:411875021780446e9fafd0c15f4f900ab1f4255d05faad659336df47f3617bbf` |

