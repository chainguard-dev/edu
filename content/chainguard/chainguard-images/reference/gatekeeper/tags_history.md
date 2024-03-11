---
title: "gatekeeper Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the gatekeeper Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-11 00:52:51
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
|  `latest-dev` | March 8th    | `sha256:7c9e8b155d77baa15b00d83ce8a76afbc3ba9fbabab17ad08a82cc16befe73d7` |
|  `latest`     | March 6th    | `sha256:f07c063df78dc741a38636b9c5e1b7610f14ee38099925f7158acdf526927464` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `3.14.0-dev` `latest-dev` `3-dev` `3.14-dev` | March 10th   | `sha256:1190c8a7cae298ad6ee96b58f5d6c552ed6c51d14f0258e47b862b2cebc83c66` |
|  `3.12-dev` `3.12.0-dev`                      | March 10th   | `sha256:361e62f4d08e1dd665de4cc2360fd1481ede8998edeec9d34b6bb3f365b311fe` |
|  `3.13-dev` `3.13.4-dev`                      | March 10th   | `sha256:751b475e06da180454ff0fb25c5ee234fc01bf815699dcd39fc2a1830c083702` |
|  `3.13` `3.13.4`                              | March 8th    | `sha256:a8e08b8790351aba35211f1aeeb60dfd6b963e8f9e27ae144163a4b2d471afe9` |
|  `3.12` `3.12.0`                              | March 8th    | `sha256:98ffcc064c6f2f3e949d8e217ead5f669bc0fa368b8854cdd77f25d5d3a51845` |
|  `3.14.0` `3` `3.14` `latest`                 | March 8th    | `sha256:60eb7d52e5c4c4d8c92191863c96dbd49b2da96da1b685bc3909cb518456e85c` |

