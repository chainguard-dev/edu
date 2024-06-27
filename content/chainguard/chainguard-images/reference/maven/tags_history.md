---
title: "maven Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the maven Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-27 00:41:27
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
|  `latest` `openjdk-21`         | June 26th    | `sha256:2856285538518c33058d616e58b18e42863efc4ebc1e71cc80a4002c6a00b3d6` |
|  `openjdk-21-dev` `latest-dev` | June 26th    | `sha256:a00fa1f412f2884bc876e798a8ee074f606e6d1b443cff0de3788ec1a65e637a` |
|  `openjdk-17-dev`              | June 26th    | `sha256:43d932999495ba1786e0d1d6a5be5379e5b9c0b3431a725e637628336565517d` |
|  `openjdk-11`                  | June 26th    | `sha256:f953bcb47b9247d9f5e79ac3f0e092748151f012ac7bf87b99d1cf6600b8cdc9` |
|  `openjdk-17`                  | June 26th    | `sha256:5cf19759b48cd761834c65d21955926810d159c1841160337617000aa810df08` |
|  `openjdk-11-dev`              | June 26th    | `sha256:55074d735acff5f8657945f03f8cdb0fb2e800925909765c14e747e3b1349e9f` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-11-3` `openjdk-11` `openjdk-11-3.9` `openjdk-11-3.9.8`                              | June 26th    | `sha256:21253e0e74b6361f28c2917140dcc31dcd37ca79b7644d26d0bd9ca6288d133c` |
|  `openjdk-21-3-dev` `openjdk-21-dev` `latest-dev` `openjdk-21-3.9-dev` `openjdk-21-3.9.8-dev` | June 26th    | `sha256:78f4fb93bb2bf3f54904ef39c069b2336674072a8f57522489c7718033026d1f` |
|  `openjdk-21-3` `openjdk-21` `openjdk-21-3.9.8` `latest` `openjdk-21-3.9`                     | June 26th    | `sha256:7ef2206ae66a50337ea30c6381d7b5575e74c4a52f5d58f87b551183f76c74d0` |
|  `openjdk-17-3.9.8` `openjdk-17-3` `openjdk-17` `openjdk-17-3.9`                              | June 26th    | `sha256:29334f2e9e7ad96362edb9fef10a2af7b6e4a37d7eece393ab7d7a046449843c` |
|  `openjdk-17-dev` `openjdk-17-3.9-dev` `openjdk-17-3-dev` `openjdk-17-3.9.8-dev`              | June 26th    | `sha256:cce9e791ae6b85a0d821a9d2f88768bea2e03cab41647e3a3516d86502fa8baf` |
|  `openjdk-11-3.9-dev` `openjdk-11-3-dev` `openjdk-11-3.9.8-dev` `openjdk-11-dev`              | June 26th    | `sha256:e198c9428092951ddeb532d7a1bc8114157a4159e5be7f22ffa00863e1b533b0` |

