---
title: "maven Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the maven Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-19 00:54:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/maven/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/maven/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/maven/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/maven/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)                        | Last Changed | Digest                                                                    |
|--------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-21-dev` `latest-dev` | March 18th   | `sha256:ca86c479f26bdd431b5906b90ca4f5e29de96cdcb8b389cc91f258b2acce235f` |
|  `latest` `openjdk-21`         | March 18th   | `sha256:41ef6a7cd4f179d69b1c1e60a1988d4b03536f3609c486b9793d2c7ba585e4d6` |
|  `openjdk-17-dev`              | March 18th   | `sha256:d37d4cb62fb3d53de8f6025c54bf7dcfb460adc7001cb7c32e9e389c22cb1947` |
|  `openjdk-11-dev`              | March 18th   | `sha256:0bbb0b1a620290a6912c007ba524d901954827e9f873bf63f0f738beafb3dd4f` |
|  `openjdk-11`                  | March 18th   | `sha256:a036428b10135015ef6d1578b41b22339bb43dabc3e877a8fc9bc32adc71677e` |
|  `openjdk-17`                  | March 18th   | `sha256:d83d5aca9f32bdfc8fabee417487b4404128f941649a044e047cfb2ce24fdec6` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-17-3.9.6-dev` `openjdk-17-3-dev` `openjdk-17-3.9-dev` `openjdk-17-dev`              | March 18th   | `sha256:bed028496fa784cb986c351f092d49be7741619e4d60dfd0c834da056a1c7bc6` |
|  `openjdk-11-3.9.6` `openjdk-11` `openjdk-11-3.9` `openjdk-11-3`                              | March 18th   | `sha256:74d0262f3de51e156fd911e7a3b76b4114bbd1ffa00dab3b44653b138a647253` |
|  `openjdk-17-3.9` `openjdk-17-3` `openjdk-17` `openjdk-17-3.9.6`                              | March 18th   | `sha256:6e3557713dd649b1daddfe443369a9d8c2829dd87f3449d492358cf272404b75` |
|  `openjdk-21-3.9-dev` `openjdk-21-3-dev` `latest-dev` `openjdk-21-3.9.6-dev` `openjdk-21-dev` | March 18th   | `sha256:c99102dffab0381b0b3731225c9d8d17895079a88ea11f8c8d216bc8d5999633` |
|  `openjdk-21-3.9.6` `openjdk-21` `latest` `openjdk-21-3` `openjdk-21-3.9`                     | March 18th   | `sha256:8b9b9ec993ee6567eebdd105b0be3eec23d7300793c57f9e4face05ff8182be9` |
|  `openjdk-11-3.9.6-dev` `openjdk-11-3.9-dev` `openjdk-11-3-dev` `openjdk-11-dev`              | March 18th   | `sha256:06f6647167c0be6d2a023458d01da0f79095a479d97520b6557f15e648b5aadf` |

