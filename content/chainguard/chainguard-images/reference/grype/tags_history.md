---
title: "grype Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the grype Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-14 00:37:02
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
|  `latest-dev` | March 13th   | `sha256:e3e6e36fd7aa5e0ea31ebc6de9cea4200d6b6fb572a904cf80a49df75d8530f9` |
|  `latest`     | March 8th    | `sha256:4db7ee603d3bb780e27a1c27bc15827c3bdeaf975417c42c18c98a7c9abd24f0` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed  | Digest                                                                    |
|-----------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `latest-dev` `0.74-dev` `0.74.7-dev` `0-dev` | March 13th    | `sha256:1b007e512fd94cedba68d7d7a1ec9edb41052645676bcfc80537be46a9519e71` |
|  `0.74.7` `0.74` `0` `latest`                 | March 8th     | `sha256:4bec5014defcc7fef8b82407b37f1c52e3faef86e4c57f715846648e82d9dbb5` |
|  `0.74.6-dev`                                 | February 24th | `sha256:d5387724ca01f846d1ac86307b01a3d8ea87380305977ac662ea89e48e65f176` |
|  `0.74.6`                                     | February 15th | `sha256:dbfda491a10443aecc872cfc99de41775b740b6d3c58f11bc69735df348e26f5` |

