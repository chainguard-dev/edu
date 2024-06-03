---
title: "node-lts Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the node-lts Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-03 00:46:08
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/node-lts/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/node-lts/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/node-lts/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/node-lts/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)                  | Last Changed | Digest                                                                    |
|--------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `next-dev` | June 1st     | `sha256:d203f8de85bbba602c4e2f6d51d0992a2cb669efbc9ccba708e8b340d1e522fd` |
|  `latest`                | May 31st     | `sha256:3d635a3537e82a6bf1cf6ef571199cc8533fa45cb3c664777d7eb8930a14ec33` |
|  `next`                  | May 31st     | `sha256:6be4159203a9550eb2df4d4e38cd52c887d87e0f5676dd28491f4a916ecc8af8` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                     | Last Changed | Digest                                                                    |
|-------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `next-dev` `20.14.0-dev` `20-dev` `20.14-dev` | June 1st     | `sha256:837febe5fa9b4cc5bf5e18482809a391e21de955a53162b362bc3e8dee056979` |
|  `next`                                                     | May 30th     | `sha256:3db662491a4eaf16aa6ad123dd697ad69d30c13f7c863025cb2160dcc8221a4f` |
|  `20.14` `latest` `20.14.0` `20`                            | May 30th     | `sha256:25366d35072bf38af0107587b4a9d1d1e684bfb6b3b44719f29d2d12eb9d7bd1` |
|  `20.13-dev` `20.13.1-dev`                                  | May 28th     | `sha256:e8d44ddf859b463a39a89dc23310120f3b676f790a02395e6d029daa10adc5b8` |
|  `20.13.1` `20.13`                                          | May 24th     | `sha256:cdcb55f5afb9fd31acaa01e957aa6eff12aa9fdca6aaff0cd5fd748611c56cc0` |
|  `20.13.0-dev`                                              | May 8th      | `sha256:2360a32e40e19b859f6d47a78ff722b6e3533260547e961a24aae47ad2603aa1` |
|  `20.13.0`                                                  | May 7th      | `sha256:9e605246896ec5e57b3ca2c840df46d2736a52d8093823a237437374d1c1c788` |

