---
title: "gradle Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the gradle Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-25 00:49:44
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/gradle/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/gradle/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/gradle/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/gradle/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)   | Last Changed | Digest                                                                    |
|-----------|--------------|---------------------------------------------------------------------------|
|  `latest` | March 22nd   | `sha256:2d0271ecb93e050b448310ca3c43b3fe0d235f6f62df2018e521825fe7a805b4` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-17-dev` `openjdk-17-8.7.0-dev` `openjdk-17-8.7-dev` `openjdk-17-8-dev`              | March 22nd   | `sha256:a6ed528866b4d36d9444f60528937799b458c2d765c42672d3308c4ee31f2008` |
|  `openjdk-21-dev` `openjdk-21-8.7-dev` `latest-dev` `openjdk-21-8-dev` `openjdk-21-8.7.0-dev` | March 22nd   | `sha256:c873d27c8f0c24102000508df8d294025414b37ef75da313721bb49fa111ff8d` |
|  `openjdk-21` `openjdk-21-8` `latest` `openjdk-21-8.7` `openjdk-21-8.7.0`                     | March 22nd   | `sha256:f68025b7cd6729bab687d64c45b0397b724c5e4f3abb428d92df626f0bfe61d8` |
|  `openjdk-17-8.7.0` `openjdk-17` `openjdk-17-8.7` `openjdk-17-8`                              | March 22nd   | `sha256:a3549bc077da83a5625ab8a16e86ef0471c0a546d449ed2c36ab908e108f9101` |
|  `openjdk-21-8.6.0` `openjdk-21-8.6`                                                          | March 18th   | `sha256:0ce6d8d683f2399fce2cfe4447d79f80d123a70512d344d162fa2c319b87d3c8` |
|  `openjdk-17-8.6.0` `openjdk-17-8.6` `8.6` `8.6.0` `8`                                        | March 18th   | `sha256:4a6a4439baabe5b258b08708670bd38fa47707efc387dd6d3b7b41821ffbf1b7` |
|  `openjdk-17-8.6-dev` `openjdk-17-8.6.0-dev` `8-dev` `8.6.0-dev` `8.6-dev`                    | March 18th   | `sha256:4bad8ea8f7e412179408686c2376c770a33cbb22867d54de5e0a8245bc484c62` |
|  `openjdk-21-8.6.0-dev` `openjdk-21-8.6-dev`                                                  | March 18th   | `sha256:7c5bd6899907cd1f1cacb8fc0617472843a66650bb8960d24342d4283f90649d` |

