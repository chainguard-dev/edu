---
title: "hugo Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the hugo Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-27 00:41:27
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/hugo/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/hugo/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/hugo/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/hugo/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 26th    | `sha256:04e1c51484dca8df84bd5379723a6055ffe8a33ab95b876961721a1536c98d58` |
|  `latest`     | June 26th    | `sha256:787ef71b03841057c6aba6aa691908893093d438fa9dfd4a4db7146a8590bfdd` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                         | Last Changed | Digest                                                                    |
|-------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `0-dev` `0.128-dev` `0.128.0-dev` | June 26th    | `sha256:703c5e7ce59e80c1d5a5c23572a38468f82538d25173109337d22164b0f58fad` |
|  `0.128` `0.128.0` `0` `latest`                 | June 26th    | `sha256:31b3818bcc785d6244ece8624d7754d8c7e3c864c3da671902c976a587d103fc` |
|  `0.127.0-dev` `0.127-dev`                      | June 25th    | `sha256:8d7a064444f30bbbbbb7c571d8a0a5624af4543de18a889ad53157ab4a1b948e` |
|  `0.127` `0.127.0`                              | June 20th    | `sha256:856878022528bef43f9a8e5db55429fec8af5cd26ef2efdd3ca5c35989789dff` |

