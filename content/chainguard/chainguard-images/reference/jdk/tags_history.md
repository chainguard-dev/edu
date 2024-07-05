---
title: "jdk Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jdk Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-05 00:42:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/jdk/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/jdk/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/jdk/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/jdk/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | July 3rd     | `sha256:d94570946c2c26a6a5efdaae31a2d04e5c997eb6762b80eb63ed5922a42f5136` |
|  `latest`     | July 3rd     | `sha256:c387dbd74f25a9b76f9ad1fcb584dbaa959be1aa464003fa0d05b8013b1aa309` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-14-dev` `openjdk-14.0.2.12-dev` `openjdk-14.0.2-dev` `openjdk-14.0-dev`  | July 4th     | `sha256:cf4c92187e9b75cc314959039d88964f710fff40ef0991ab9fed106ef7d467cf` |
|  `latest-dev` `openjdk-22.0.1-dev` `openjdk-22.0-dev` `openjdk-22-dev`             | July 4th     | `sha256:c9caa7ae0e6190c174b17a997101f71057f2ce28bd14399671446f168225f0a0` |
|  `openjdk-15.0` `openjdk-15.0.10.5` `openjdk-15.0.10` `openjdk-15`                 | July 4th     | `sha256:8441e99b2c21e16af0184cdc4f1eec9fe1bf9a86cc92a22736ebf35a1b0048ad` |
|  `openjdk-8.412.08-dev` `openjdk-8-dev` `openjdk-8.412-dev`                        | July 4th     | `sha256:fc8bab5dbe644d128b09599617157f153207137999b73f49d8a1495cd8bbca53` |
|  `openjdk-14.0` `openjdk-14.0.2` `openjdk-14.0.2.12` `openjdk-14`                  | July 4th     | `sha256:2b19f71aa0197ab8b7e6dea6472657f31be54fbacc3be6da3301f3d9fef02103` |
|  `openjdk-17.0.11` `openjdk-17` `openjdk-17.0`                                     | July 4th     | `sha256:ba3ab07f3b15e33951241943538c82312e2c0975a431c3f0d0d1acfcc9ae6bb5` |
|  `openjdk-22.0.1` `latest` `openjdk-22` `openjdk-22.0`                             | July 4th     | `sha256:6f599d5c92e94bd00c1471d0bbfb5ab39f67b7b499f0c1bba529c328c8c24210` |
|  `openjdk-11-dev` `openjdk-11.0-dev` `openjdk-11.0.23-dev`                         | July 4th     | `sha256:dd07c4e70e4f9d42f17913d5d9b2c5a027fffe1b4e029e82150e8bfb2cc5650b` |
|  `openjdk-16-dev` `openjdk-16.0-dev` `openjdk-16.0.2-dev` `openjdk-16.0.2.7-dev`   | July 4th     | `sha256:b8577d0f9b18acf24ccc78be0b8a41feda02a233597745d966db45be841027b2` |
|  `openjdk-17.0-dev` `openjdk-17.0.11-dev` `openjdk-17-dev`                         | July 4th     | `sha256:f11a4f368d4d62ac23e70d3ba5fb37cf001b50e67644a6aeb4282848bd3afff3` |
|  `openjdk-21-dev` `openjdk-21.0.3-dev` `openjdk-21.0-dev`                          | July 4th     | `sha256:4e68cd7f29d51b898c8102f7943423a033afe0ebc7dabcdb9faac0953c9ce9ec` |
|  `openjdk-21.0.3` `openjdk-21.0` `openjdk-21`                                      | July 4th     | `sha256:4cc542832afff8517852d515ce7dfcc9a9781278b745f4890e63b26407c2a4c4` |
|  `openjdk-16.0` `openjdk-16.0.2` `openjdk-16` `openjdk-16.0.2.7`                   | July 4th     | `sha256:3f086ed9aaae8623ba356df9ed8bd09863b8aa56e14b81a54be2c2a8dc142fa4` |
|  `openjdk-15.0-dev` `openjdk-15.0.10-dev` `openjdk-15.0.10.5-dev` `openjdk-15-dev` | July 4th     | `sha256:6301e33ef7a56613056ab2fec20caff36ebbd312fd4c4587b3ee10bafc65d5e4` |
|  `openjdk-11.0` `openjdk-11.0.23` `openjdk-11`                                     | July 4th     | `sha256:35a6bb900bcd6d57caf573c04cdc372f7255f187fb1d54834ee84787ad5bf00b` |
|  `openjdk-8` `openjdk-8.412.08` `openjdk-8.412`                                    | July 4th     | `sha256:adab1cf95e759fa5b3ed3c797c0eb9e74bb6093f26e5c2e5c46037dcc97b49a7` |

