---
title: "grype Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the grype Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-13 00:52:18
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/grype/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/grype/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/grype/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/grype/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | March 12th   | `sha256:c603ad330f2174212f2a3568e8874eaa306dea1a6b714a53c2632b32bfb756f8` |
|  `latest`     | March 8th    | `sha256:4db7ee603d3bb780e27a1c27bc15827c3bdeaf975417c42c18c98a7c9abd24f0` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed  | Digest                                                                    |
|-----------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `0.74.7-dev` `0.74-dev` `latest-dev` `0-dev` | March 12th    | `sha256:c83f868c6b267477f665dce632477a42a3214508ba71932838e6c07f256613b2` |
|  `0.74.7` `0.74` `0` `latest`                 | March 8th     | `sha256:4bec5014defcc7fef8b82407b37f1c52e3faef86e4c57f715846648e82d9dbb5` |
|  `0.74.6-dev`                                 | February 24th | `sha256:d5387724ca01f846d1ac86307b01a3d8ea87380305977ac662ea89e48e65f176` |
|  `0.74.6`                                     | February 15th | `sha256:dbfda491a10443aecc872cfc99de41775b740b6d3c58f11bc69735df348e26f5` |
|  `0.74.5-dev`                                 | February 13th | `sha256:1637bc03700fb4e4bcb769d55fe9179bbca98f32aa3c585796a1eb0cf598341f` |

