---
title: "tigera-operator Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the tigera-operator Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-31 00:48:45
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/tigera-operator/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/tigera-operator/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/tigera-operator/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/tigera-operator/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | May 23rd     | `sha256:3349d624694d760105cebeb385fc0c48dc6addc2d143cf533357c565d72e589f` |
|  `latest-dev` | May 23rd     | `sha256:f27c42de901797ba4af0619fe4212258bdf99fc0b5be305fcc342cd28e9ddbfa` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                        | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `v1.31-dev` `1.31.2-dev` `v1.31.2-dev` `1.31-dev`                                             | May 30th     | `sha256:abc69cce0fd0b33aff35d0d6a87e1864e01a14e18d4bddfeeb4e384a5ca0cace` |
|  `1.33.0-dev` `v1.33-dev` `vlatest-dev` `1.33-dev` `1-dev` `v1.33.0-dev` `v1-dev` `latest-dev` | May 30th     | `sha256:e6a7bc0767f2a0cca0adc27ae08f872655abb1c3f638763440e5b964e17d9e79` |
|  `v1.30-dev` `1.30-dev` `1.30.10-dev` `v1.30.10-dev`                                           | May 30th     | `sha256:2787b7f22a7ab7375cbd4dcfb506d83adac674519395bf9aabe52e5e1505e128` |
|  `1.30.10` `1.30` `v1.30.10` `v1.30`                                                           | May 30th     | `sha256:37ee4f934cd66489769371350d216ce8f58a37034aa9a498cd33902712afc449` |
|  `v1.32-dev` `1.32.8-dev` `1.32-dev` `v1.32.8-dev`                                             | May 30th     | `sha256:27c4377ddeb3abfd9e7e877aa08920206036672fdb19e2c0a4a403e0e5d7c47d` |
|  `1.31` `v1.31.2` `v1.31` `1.31.2`                                                             | May 30th     | `sha256:2544ce7e29204e46f28a1aeb5ea2bbaecfcaed621f923196c364d2f5a35b62a3` |
|  `1.32` `1.32.8` `v1.32.8` `v1.32`                                                             | May 30th     | `sha256:98b2c878002f816d07dbf8a02009589b99e4bc3675f2e5e0f2b3c4728863bcd6` |
|  `v1` `1.33` `1.33.0` `latest` `1` `vlatest` `v1.33.0` `v1.33`                                 | May 23rd     | `sha256:cd4c7f06eb80bb43eed132684f5f682c989d3a4b101cae9ad53f3eb238acbd64` |

