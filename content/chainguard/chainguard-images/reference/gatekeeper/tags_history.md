---
title: "gatekeeper Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the gatekeeper Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-14 00:37:02
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/gatekeeper/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/gatekeeper/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/gatekeeper/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/gatekeeper/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | March 13th   | `sha256:941e0219561668302da8faf13c1963539b76375478d0dc995d84138cac1d385d` |
|  `latest`     | March 13th   | `sha256:fd17dca98677c6e2503508cf3122abb52bae007b964c8f6b5acce01671d811ec` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `3.12-dev` `3.12.0-dev`                      | March 13th   | `sha256:76960d225d641be855deaa6b8cc0ed372c6f32da9f4c6e18dfa811841c7a6747` |
|  `3.14.1-dev` `latest-dev` `3-dev` `3.14-dev` | March 13th   | `sha256:51f0c4696e417934d0937d774ef4a218e3fdc227f63a7125f29d7570cccc98a0` |
|  `3.13-dev` `3.13.4-dev`                      | March 13th   | `sha256:09bcb6cf283074fc0fc53610d86e4c08939cb69d1e4cf761fc193c4e7fbf05d0` |
|  `latest` `3` `3.14.1` `3.14`                 | March 13th   | `sha256:558a7d7841e91875f25e0a84f49c66edd0f573c5e2e9fe3b2280a11fffc1fe29` |
|  `3.14.0-dev`                                 | March 12th   | `sha256:b4b3ef5c89c9f443b9f12a2199c3c4dffb1260770cb5c30f8d0f8dd33eca2eb1` |
|  `3.13` `3.13.4`                              | March 8th    | `sha256:a8e08b8790351aba35211f1aeeb60dfd6b963e8f9e27ae144163a4b2d471afe9` |
|  `3.12` `3.12.0`                              | March 8th    | `sha256:98ffcc064c6f2f3e949d8e217ead5f669bc0fa368b8854cdd77f25d5d3a51845` |
|  `3.14.0`                                     | March 8th    | `sha256:60eb7d52e5c4c4d8c92191863c96dbd49b2da96da1b685bc3909cb518456e85c` |

