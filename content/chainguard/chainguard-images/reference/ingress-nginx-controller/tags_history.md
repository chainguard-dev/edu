---
title: "ingress-nginx-controller Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the ingress-nginx-controller Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-05 17:06:05
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
|  `latest`     | March 4th    | `sha256:c2aa99a274cfe996ee1d6bbdd5476fbf8adb88153625fcd37f28173d2d15e80d` |
|  `latest-dev` | March 4th    | `sha256:99d75f5a90c9c9d7ed6801ceafe65c0fccb1698bc4825aff197a2a46b0a1ef0c` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed  | Digest                                                                    |
|-----------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `1` `1.10.0` `1.10` `latest`                 | March 3rd     | `sha256:cb643281a87c51232754bda3e8e95383f673f18ab3560d4346bae4dbf01484d6` |
|  `latest-dev` `1-dev` `1.10-dev` `1.10.0-dev` | March 3rd     | `sha256:a5a7004508773ddc10a4b2ddc3355a46be5a336ab960aaef3599c761717f35d1` |
|  `1.9-dev` `1.9.6-dev`                        | February 26th | `sha256:800dddda1d5869e675b7a72711838d4ed267a2fa3f38bbd828e3ef829f728a61` |
|  `1.9.6` `1.9`                                | February 26th | `sha256:f10203f14a6e462a77762f4186ab89f1e35222b64c22e06b04625c8dccd5af88` |

