---
title: "maven Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the maven Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-13 00:52:18
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
|  `latest` `openjdk-21`         | March 12th   | `sha256:ece0ba536b21486b7204689d846c2bffeb4e339832ea8f8959d8a92987b2110c` |
|  `latest-dev` `openjdk-21-dev` | March 12th   | `sha256:8a4756562e87e02e543acc8667cda82b1c794ee692f92c7a47bfff33163176fa` |
|  `openjdk-11-dev`              | March 12th   | `sha256:90bae162fa94725152f4eb15ca9daa5fdb74c97fedba06c67c0e1c091562cf5d` |
|  `openjdk-17-dev`              | March 12th   | `sha256:ceec112d39893ca639d2cffdd31b84f91cc7342269dff88a56fde1da4f7a1271` |
|  `openjdk-11`                  | March 8th    | `sha256:88cc40a9c37dee30f25713de19fab42101a4d3e852707b0ef7d96bf579cfcfb5` |
|  `openjdk-17`                  | March 8th    | `sha256:b578fba4071246e8e0d1612b2c416670d776feaf680a4c00bdf1c57b3507c136` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `openjdk-21` `openjdk-21-3.9.6` `openjdk-21-3.9` `openjdk-21-3`                     | March 12th   | `sha256:6c328f51f0a41fd93f1a8c55b5b96011557594a73be2c599b657e8926345675a` |
|  `latest-dev` `openjdk-21-3.9-dev` `openjdk-21-dev` `openjdk-21-3.9.6-dev` `openjdk-21-3-dev` | March 12th   | `sha256:4f934e62d072646097254c25c0242beb2c6df8e1e8d519eb0c7493a1ea66b5f7` |
|  `openjdk-11-dev` `openjdk-11-3.9-dev` `openjdk-11-3.9.6-dev` `openjdk-11-3-dev`              | March 12th   | `sha256:5359e1fc56a4e4fcc4851c8f0736df94016c954d89c25be20d43b553800278d6` |
|  `openjdk-17-3.9.6-dev` `openjdk-17-dev` `openjdk-17-3.9-dev` `openjdk-17-3-dev`              | March 12th   | `sha256:926443e8235e9c9c5b8999ce177f9d116b027741728272f9e2f6d5ef36b0a687` |
|  `openjdk-17` `openjdk-17-3.9.6` `openjdk-17-3.9` `openjdk-17-3`                              | March 8th    | `sha256:f0dddc94e0d9711c059fc15f25fbdd7a895802ca139cbff9f7117f348dd6975a` |
|  `openjdk-11` `openjdk-11-3.9` `openjdk-11-3` `openjdk-11-3.9.6`                              | March 8th    | `sha256:1d2542a416a019e60f4c3aee4a884366ca7a32b0c67dc0361e687d7570f92ba9` |

