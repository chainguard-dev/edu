---
title: "harbor-core Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the harbor-core Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-22 00:47:17
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/harbor-core/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/harbor-core/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/harbor-core/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/harbor-core/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | May 21st     | `sha256:3cf2bed0097bdd36aeaf31d5a80366c88002e788adc1c00b937016bea6e3953f` |
|  `latest-dev` | May 21st     | `sha256:153a55b51b86717c016a6031a28f875030dacd02614aee1536cf59ac630c20cd` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `2-dev` `2.10.2-dev` `2.10-dev` | May 21st     | `sha256:0abec5afc3f18986ef62713dad11fb6668c87b0d323231414661a783b0763f1a` |
|  `2` `2.10` `latest` `2.10.2`                 | May 21st     | `sha256:647bf60b938feba9a29798f475922e3fa16c3057e5d311b65675d32dda64d53b` |
|  `2.8.6-dev` `2.8-dev`                        | May 21st     | `sha256:c5d3bd294d671dd4f4ce2412ce5201ad7f7ca3dfbfa5cc14c5f2f8b2d1c90238` |
|  `2.9` `2.9.4`                                | May 21st     | `sha256:4350a88e53a38f5f1eb28813a1383e163b9344db51ffbb111d2828e6a864f1a2` |
|  `2.9.4-dev` `2.9-dev`                        | May 21st     | `sha256:4fac543640b5fbcebf3ec506b002438817fe0231f6d3724d6321000c6549e444` |
|  `2.8` `2.8.6`                                | May 21st     | `sha256:8cd2f8c3410d90d9f61449d4cb1aef3a2260c375a48dd16bd81fa253e35cce26` |

