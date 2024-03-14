---
title: "ingress-nginx-controller Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the ingress-nginx-controller Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-14 00:37:02
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
|  `latest-dev` | March 13th   | `sha256:9f4053165a79f9411e0724b98a8d91bd2e995496f22663226e4a91b9d5dd9803` |
|  `latest`     | March 13th   | `sha256:2cdd33b3bc26d04bd26c39a9f9bc9d4e9255e2995d7a3801ab56bfd274ffa69a` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed  | Digest                                                                    |
|-----------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `1` `1.10.0` `latest` `1.10`                 | March 13th    | `sha256:1f4ac0e7f1c3d4e35ac3737d7b8b8f4a01eb5300a4261454843f4e127441a870` |
|  `1.10-dev` `1-dev` `latest-dev` `1.10.0-dev` | March 13th    | `sha256:835bf8d45a99b54a3b4692207902a449540268817194e81d516621f7387e4118` |
|  `1.9-dev` `1.9.6-dev`                        | February 26th | `sha256:800dddda1d5869e675b7a72711838d4ed267a2fa3f38bbd828e3ef829f728a61` |
|  `1.9.6` `1.9`                                | February 26th | `sha256:f10203f14a6e462a77762f4186ab89f1e35222b64c22e06b04625c8dccd5af88` |

