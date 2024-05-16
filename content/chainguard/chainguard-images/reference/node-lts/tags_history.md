---
title: "node-lts Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the node-lts Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-16 00:37:58
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
|  `next`                  | May 15th     | `sha256:ce6106d72e1ffe955f350f2226fe56fc1baa2406eac32af4fce99f0f37fd3f1e` |
|  `next-dev` `latest-dev` | May 15th     | `sha256:5d3c31d95ad940483d6a42a6aba0c72383fba099fbe1f3dca1875555833b4bc2` |
|  `latest`                | May 15th     | `sha256:1fa615d46ab7175a3cbb34d9ae9950e06ef68ac86f84e3c9873ea57fb425cb8c` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                     | Last Changed | Digest                                                                    |
|-------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `20` `20.13.1` `20.13` `latest`                            | May 15th     | `sha256:5ac4bf1af5dbbb583f9e406fa4520310631f49ea448880cd8515e43d476544af` |
|  `next`                                                     | May 15th     | `sha256:8ca1af10a1b7403b051525faa79c29ccafd193e47f740e8fd542b1404f2c32bc` |
|  `20.13-dev` `20-dev` `next-dev` `20.13.1-dev` `latest-dev` | May 15th     | `sha256:46c14a05683cfbca8cb47949ce72a474727ab8242c1cdbc5f970fb7c31d90799` |
|  `20.13.0-dev`                                              | May 8th      | `sha256:2360a32e40e19b859f6d47a78ff722b6e3533260547e961a24aae47ad2603aa1` |
|  `20.13.0`                                                  | May 7th      | `sha256:9e605246896ec5e57b3ca2c840df46d2736a52d8093823a237437374d1c1c788` |
|  `20.12-dev` `20.12.2-dev`                                  | May 2nd      | `sha256:e8836f7cb1c3a413655996eb25cda5e87fe8950b6af44ff77a39f0ca39b32bd0` |
|  `20.12` `20.12.2`                                          | May 2nd      | `sha256:a55a71363129778395bcc88cc8c2fe6a0f26affb1d7ee94862bef5c6e1f1c873` |

