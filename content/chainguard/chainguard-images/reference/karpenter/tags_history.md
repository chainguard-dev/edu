---
title: "karpenter Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the karpenter Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-23 00:43:06
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/karpenter/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/karpenter/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/karpenter/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/karpenter/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 22nd    | `sha256:621a9e4f3260ba1c5207fb7d9198c5be421123860ed1a91e3fc425cbdf12d605` |
|  `latest`     | June 19th    | `sha256:a575f99fc385fc7d502721569abac7e556bc32b45d26499ae16e63caf0b15a04` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0.35-dev` `0.35.5-dev`                      | June 21st    | `sha256:6adfd525ef1519b90d46cada7de9a36a2c972fb3c8a977b4cc00d934e0a9f00d` |
|  `0.37.0-dev` `latest-dev` `0-dev` `0.37-dev` | June 21st    | `sha256:df7eb90534ab2bccd3657fb2c733a3c4502c6b68d6db327349833d43eb33d950` |
|  `0` `latest` `0.37.0` `0.37`                 | June 20th    | `sha256:47ec29b9394a8706a72c8d8173f4495d5803441d626510909112bd9769a94abc` |
|  `0.35.5` `0.35`                              | June 20th    | `sha256:96a3243f9f52e8ac0dcf869a74a690e52bd56bd32a3db21edcbd821ae339a550` |

