---
title: "jdk Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jdk Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-17 00:46:08
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
|  `latest-dev` | April 11th   | `sha256:54df748abd9552d6a49d090662a5a3ebb5afc3bf522772d948c4db98ec0d4e6d` |
|  `latest`     | April 11th   | `sha256:08d05b82f98cf64c6efafbecb23b47a894e791a60c26dd3cc225157ba138e419` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-8-dev` `openjdk-8.392-dev` `openjdk-8.392.08-dev`                        | April 16th   | `sha256:0dee2fc26c4432e734df1c34c3e31c0a277e85045d2d6650314c89ea5b9475d7` |
|  `openjdk-8.392` `openjdk-8.392.08` `openjdk-8`                                    | April 16th   | `sha256:c09f514498438d5971cc0667e9cf8798a16a6b21634337d248ff5905ada10568` |
|  `openjdk-11-dev` `openjdk-11.0-dev` `openjdk-11.0.22-dev`                         | April 11th   | `sha256:1f6d7112bea7d3ecce9b904977e9d7b9c771a1456313b49baf7d180de6d6c7b9` |
|  `openjdk-22.0.0` `latest` `openjdk-22.0` `openjdk-22`                             | April 11th   | `sha256:7c0389db518bad161ca24bf21cb3ac79f7e724168847035994cc3a49c518a31a` |
|  `openjdk-21.0.2-dev` `openjdk-21.0-dev` `openjdk-21-dev`                          | April 11th   | `sha256:0fa62e4be3aaa872aae70cd282e4b3f3bbfba68b9c746c472c68fccdcb403a03` |
|  `openjdk-22.0-dev` `latest-dev` `openjdk-22.0.0-dev` `openjdk-22-dev`             | April 11th   | `sha256:580fc13a5ebd248e02273ec8dd432a490813ce8eb45005e0fde8dd05f6ae38d6` |
|  `openjdk-14` `openjdk-14.0.2` `openjdk-14.0.2.12` `openjdk-14.0`                  | April 11th   | `sha256:57f22a576651c565d892fafe1f33f49fee25ed612f977b59d5695363a2954f32` |
|  `openjdk-17.0.10-dev` `openjdk-17-dev` `openjdk-17.0-dev`                         | April 11th   | `sha256:55ea5ef998c15dcfb1ffb82780d17e89f68f8f0c65b1a96ff71ce71220589926` |
|  `openjdk-16.0.2` `openjdk-16.0` `openjdk-16.0.2.7` `openjdk-16`                   | April 11th   | `sha256:27a6c5802f783ad81b76c40e9df6fc82afa1640878555eae1628f8db3e3b1913` |
|  `openjdk-15.0.10.5` `openjdk-15.0.10` `openjdk-15` `openjdk-15.0`                 | April 11th   | `sha256:9f89d9c31d4d89a1fd16b40267378e1cdca79442666aeb99afffb4da06de5af1` |
|  `openjdk-11.0.22` `openjdk-11.0` `openjdk-11`                                     | April 11th   | `sha256:e0f2667d98d019f260105976d2ddad5eeebda2cdd66299bd43212707062354d8` |
|  `openjdk-15.0-dev` `openjdk-15.0.10.5-dev` `openjdk-15-dev` `openjdk-15.0.10-dev` | April 11th   | `sha256:cd3bdcad88606dd1029b6f7475e47b90a038bcf6bd25bff72f8c85349c76ad49` |
|  `openjdk-16-dev` `openjdk-16.0-dev` `openjdk-16.0.2-dev` `openjdk-16.0.2.7-dev`   | April 11th   | `sha256:007dcb61bfb8b063feee6cd1ace54c1549147a135e440801a18de6af8328b8e3` |
|  `openjdk-14.0.2-dev` `openjdk-14.0.2.12-dev` `openjdk-14.0-dev` `openjdk-14-dev`  | April 11th   | `sha256:a02380e20aaa5251b174987e69b3fa3036f8e78b89e06bbed1f5f8f8b0a9cc75` |
|  `openjdk-21.0.2` `openjdk-21.0` `openjdk-21`                                      | April 11th   | `sha256:4ece5af768c27dffcffb16780206dfdcd4b45c7edc682250d1b498cb2267d30c` |
|  `openjdk-17` `openjdk-17.0.10` `openjdk-17.0`                                     | April 11th   | `sha256:b34966b9212d2ce857f154b42bc4d242e0f46a68fb175a4b24d0dbdaafc6bf8b` |

