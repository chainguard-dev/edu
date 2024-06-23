---
title: "ingress-nginx-controller Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the ingress-nginx-controller Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-23 00:43:06
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/ingress-nginx-controller/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/ingress-nginx-controller/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/ingress-nginx-controller/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/ingress-nginx-controller/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 22nd    | `sha256:46a904668d2cdc917b48f0f6988784cf9187a6f369c3d7f6d868f3841970200d` |
|  `latest`     | June 22nd    | `sha256:3cb56e54bcfbaf08e8ac3f6334072e232fec757d4bb615e71c4c11a9b86c50dc` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.9.6` `1.9`                                | June 21st    | `sha256:8ef9305f977cccb1652434292541b78c7854e57cc72d5228447285cada5af38e` |
|  `1.10.1-dev` `latest-dev` `1-dev` `1.10-dev` | June 21st    | `sha256:b089f17d763aa7573493668c2fa70a445ca719e84c3a7182a776f8c35471c3a2` |
|  `1.10` `1` `1.10.1` `latest`                 | June 21st    | `sha256:5a6e2019dc966e75c84cdbc59f9709f8e58f0923ebcbfe62a138ff80ae63c8dd` |
|  `1.9.6-dev` `1.9-dev`                        | June 21st    | `sha256:ccf2e35a8e755ccd025af18e77a15ec604388de5f4580172d882d6dc0e8dc23a` |

