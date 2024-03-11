---
title: "argo-cli Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the argo-cli Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-11 00:52:51
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/argo-cli/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/argo-cli/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/argo-cli/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/argo-cli/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | March 9th    | `sha256:a6482cd95262f413de6eb38892134c273931f2d31a16b466da0bd8001671da15` |
|  `latest-dev` | March 9th    | `sha256:8a23f407805462d58b03e43ee37fad6f99aa10acbff479c9a0749203766525e9` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed  | Digest                                                                    |
|---------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `3-dev` `latest-dev` `3.5.5-dev` `3.5-dev` | March 10th    | `sha256:95c2bd81d1da7f902e30e2ec4645efa065df400f6f907ae70cf53b1e7eadeb00` |
|  `3.5.5` `latest` `3.5` `3`                 | March 8th     | `sha256:b3a81d77651c067b0bfaf547d3e3a4af7fdde1ebcd4297bf3b5a0dd53af11bde` |
|  `3.5.4-dev`                                | February 26th | `sha256:86c213c06f0d0f0e38dd1c1aeb0155da436fb04589e8568bcff049fefb8e43b1` |
|  `3.5.4`                                    | February 26th | `sha256:1b9b7d9b981b08b786d6f6d303c8ed2efa8357511dab12b5d69c2891d3079377` |

