---
title: "maven Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the maven Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-11 00:52:51
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
|  `openjdk-11`                  | March 8th    | `sha256:88cc40a9c37dee30f25713de19fab42101a4d3e852707b0ef7d96bf579cfcfb5` |
|  `openjdk-17` `latest`         | March 8th    | `sha256:b578fba4071246e8e0d1612b2c416670d776feaf680a4c00bdf1c57b3507c136` |
|  `openjdk-17-dev` `latest-dev` | March 8th    | `sha256:5d4597a0f58ae24839035e121f5c05524f1aa2c5691548ac6d7a19857c1f1e24` |
|  `openjdk-21-dev`              | March 8th    | `sha256:498a41227f026d5566d839a61734de869a1007cd785cd51fee7cbe966e8f57be` |
|  `openjdk-11-dev`              | March 8th    | `sha256:b4e3416dce0b1a9067e9a8a9cef9498623b33fb07ab78c85aadc16d2586bcdc1` |
|  `openjdk-21`                  | March 8th    | `sha256:ece0ba536b21486b7204689d846c2bffeb4e339832ea8f8959d8a92987b2110c` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-21-3-dev` `openjdk-21-dev` `openjdk-21-3.9.6-dev` `openjdk-21-3.9-dev`              | March 10th   | `sha256:7e5f2f81bdd241a4b8ed39b7a2f7cc30320ebfff602aa753de0779c61c15c2d5` |
|  `latest-dev` `openjdk-17-3-dev` `openjdk-17-dev` `openjdk-17-3.9.6-dev` `openjdk-17-3.9-dev` | March 10th   | `sha256:441d8d2da68c702d8bb956b6c4eb3213731ea49a1fe50adeb5bcdfc34ecae90b` |
|  `openjdk-11-3.9.6-dev` `openjdk-11-3.9-dev` `openjdk-11-3-dev` `openjdk-11-dev`              | March 10th   | `sha256:a4d1fe03f64dc8fedac7a6c72d17d47db7ed664910585fb8e4fd50db39d19bf6` |
|  `openjdk-21` `openjdk-21-3.9.6` `openjdk-21-3.9` `openjdk-21-3`                              | March 8th    | `sha256:6c328f51f0a41fd93f1a8c55b5b96011557594a73be2c599b657e8926345675a` |
|  `openjdk-17` `openjdk-17-3.9.6` `openjdk-17-3.9` `openjdk-17-3` `latest`                     | March 8th    | `sha256:f0dddc94e0d9711c059fc15f25fbdd7a895802ca139cbff9f7117f348dd6975a` |
|  `openjdk-11` `openjdk-11-3.9` `openjdk-11-3` `openjdk-11-3.9.6`                              | March 8th    | `sha256:1d2542a416a019e60f4c3aee4a884366ca7a32b0c67dc0361e687d7570f92ba9` |

