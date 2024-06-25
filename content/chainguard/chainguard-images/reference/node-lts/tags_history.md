---
title: "node-lts Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the node-lts Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-25 00:42:19
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
|  `next-dev` `latest-dev` | June 24th    | `sha256:94ac8127251472812b335c47b981549b86e9e99b87aef5a7295223d14e7290e6` |
|  `latest`                | June 24th    | `sha256:d38ff06dccf8fed3752836ae72a8b10bf9862c9cb297efb48c94c419c87fbe6c` |
|  `next`                  | June 24th    | `sha256:5bbc9dda2d853a5c671ff6bdb324f91a2bda5cc8166232b1f0aacb9feb7148b6` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                     | Last Changed | Digest                                                                    |
|-------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `next-dev` `20.15.0-dev` `20-dev` `20.15-dev` | June 24th    | `sha256:6fb63ad4b4db95a43db2096ef20e6203ff7a76d1a601c6754ef900d37414f570` |
|  `20` `20.15` `latest` `20.15.0`                            | June 24th    | `sha256:344f96ca1c379a1b3f753f8c068f3727407acbce10dd657ccc4cc7ab22577605` |
|  `next`                                                     | June 24th    | `sha256:3de997ef090def04b43f0510d277a43fc8bac832461d812fe9433ddc86767710` |
|  `20.14.0-dev` `20.14-dev`                                  | June 20th    | `sha256:1bd3303c076c8ec56df3ef088bc78efddc289b1119614d5d21324e7ee6473f1a` |
|  `20.14.0` `20.14`                                          | June 20th    | `sha256:6c1f47f8b698917c5ffd08be5840e974b02750448840fce37db90a888c222e23` |

