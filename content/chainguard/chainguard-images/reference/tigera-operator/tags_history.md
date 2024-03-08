---
title: "tigera-operator Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the tigera-operator Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-08 00:56:03
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
|  `latest-dev` | March 7th    | `sha256:cfe3042b5830feed379cb22c9bc90ed39856b022d93494a048ecf151ccf8db9e` |
|  `latest`     | March 7th    | `sha256:b8384049e58c7441144a6c87f2d34873f26ff23bcbf0d7befababcaff9dc1e5f` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                        | Last Changed  | Digest                                                                    |
|------------------------------------------------------------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `1.30.9-dev` `1.30-dev` `v1.30.9-dev` `v1.30-dev`                                             | March 7th     | `sha256:caf5c23d0e190bff11e3ec4a61a26391a2a66ee1895398c1ecb704425fc2ab20` |
|  `v1.31.2` `v1.31` `1.31` `1.31.2`                                                             | March 7th     | `sha256:c0d8fcfd4271dbace07a427e42649985cac76451cd490c429f5562877d04aab7` |
|  `v1` `1.33.0` `vlatest` `1` `1.33` `v1.33` `v1.33.0` `latest`                                 | March 7th     | `sha256:93eb20912318ffbc63d932b98b6bfa63a382a2bc3ff5ed8b6cbdd4564bdf5e5e` |
|  `v1.33-dev` `1-dev` `latest-dev` `1.33.0-dev` `v1-dev` `1.33-dev` `vlatest-dev` `v1.33.0-dev` | March 7th     | `sha256:5f69d1ecf070b1a1e3e43f7e32bfb5ce4c5bf82da461f4a3002301266ecb6a76` |
|  `1.31-dev` `1.31.2-dev` `v1.31-dev` `v1.31.2-dev`                                             | March 7th     | `sha256:1bfddca13e9d5c328150635ec0d6f12152f7254df4fd4244b688c9f0194b26ff` |
|  `v1.32.5-dev` `v1.32-dev` `1.32.5-dev` `1.32-dev`                                             | March 7th     | `sha256:df7b73cbed7e49958075c351d9f6498cbf6dfc340333b48c4611e4da4b74bb31` |
|  `v1.32.5` `v1.32` `1.32.5` `1.32`                                                             | March 7th     | `sha256:ed97fc8090194fdfcdc82827ef4daf9bf2cc354dd2c4048802ff8a84c68be23b` |
|  `v1.30` `v1.30.9` `1.30` `1.30.9`                                                             | March 7th     | `sha256:18e6af7351c503656466ca2763b3504a4c25c870cfb86c3dbea39fcc41372969` |
|  `1.32.4-dev` `v1.32.4-dev`                                                                    | February 13th | `sha256:5576b9899a6dc5638c218802c06b88317e76b27fb8c3cbb940b7e6bc266cd669` |

