---
title: "tigera-operator Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the tigera-operator Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-14 00:37:02
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
|  `latest-dev` | March 13th   | `sha256:25161f56135ed98cd58f18852ed4149572aafdbd1bb8502699bb9f32722409d0` |
|  `latest`     | March 8th    | `sha256:78ff5086c97d67db515e26b40b59c1a9f270bb2669855d30157977e5c4635eeb` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                        | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `v1.30-dev` `1.30.9-dev` `1.30-dev` `v1.30.9-dev`                                             | March 13th   | `sha256:c98b6378328a6cc2ceb3454272c79c8185609985dceff38d8c169e7269e13905` |
|  `1.31-dev` `v1.31.2-dev` `1.31.2-dev` `v1.31-dev`                                             | March 13th   | `sha256:c4da8954b4f9b2e343c40f7553228b45328846ac0e5ff779f781120b45733e25` |
|  `latest-dev` `1-dev` `v1.33-dev` `1.33-dev` `vlatest-dev` `v1.33.0-dev` `1.33.0-dev` `v1-dev` | March 13th   | `sha256:84e4cb534d0a230826c6346f5ba4bea0ba4b092663b919ef665a4b0c585f3fb2` |
|  `1.32.5-dev` `v1.32-dev` `v1.32.5-dev` `1.32-dev`                                             | March 13th   | `sha256:697137fa7ca36c7eeb041f92d17839d352455a8442abf62631bb07f2366e37e4` |
|  `v1.32.5` `1.32.5` `1.32` `v1.32`                                                             | March 9th    | `sha256:5291e21e1258055f33673432f42764c847c4f39ad2be2a79c95de2263368349a` |
|  `1.30.9` `v1.30.9` `1.30` `v1.30`                                                             | March 9th    | `sha256:fd95757c80b3211d382693fc3b81f054c120a53b6c70cbd262231379765d6e38` |
|  `1.31.2` `v1.31.2` `1.31` `v1.31`                                                             | March 9th    | `sha256:64a785804f14909c8bb4382a6cd92c128119d1269630fbb5bffcbae2bcce098e` |
|  `v1` `v1.33` `1.33` `1.33.0` `latest` `v1.33.0` `vlatest` `1`                                 | March 8th    | `sha256:8c89dacd9bd6cf42ec45d5b34911ee694272b4ff1b077aba65f55b8c18070013` |

