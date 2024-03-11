---
title: "php Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the php Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-11 00:52:51
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/php/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/php/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/php/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/php/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)           | Last Changed | Digest                                                                    |
|-------------------|--------------|---------------------------------------------------------------------------|
|  `latest-fpm-dev` | March 9th    | `sha256:9269eebdd230373e011e3416acd586ff7ef76a30c12561c06e38c6dd6c9a6112` |
|  `latest-dev`     | March 9th    | `sha256:a7a78fcc3c8783eba243d9f2723b7e16d82206ed3a1522a07cda7e2b4c21b979` |
|  `latest`         | March 9th    | `sha256:1e465f1b64d08c700dceeaef3a88652a70b0041c2916563315fbe517edc7c586` |
|  `latest-fpm`     | March 9th    | `sha256:fda2e607e7a50b03d536adeaa802cf411188ebc7f949c6b40655d869fd56229f` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                          | Last Changed | Digest                                                                    |
|----------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `8.2.16-r2-fpm-dev` `latest-fpm-dev` `8-fpm-dev` `8.2-fpm-dev` `8.2.16-fpm-dev` | March 10th   | `sha256:9564ffcad694cb09ccb57d62418c51b4e08d2607e7cf2c0158575a114683fa6d` |
|  `8.2.16-dev` `8-dev` `latest-dev` `8.2-dev`                                     | March 10th   | `sha256:bc936fba503c6a93c0931ef7d80cd73a30b6df8e18eabacdc4b6acfb8b79edae` |
|  `latest-fpm` `8.2.16-r2-fpm` `8-fpm` `8.2.16-fpm` `8.2-fpm`                     | March 9th    | `sha256:4bd1cd3d6bf2a801bdf5f948742ab0133ffdb50bc787e2be65f16ed2feeb191c` |
|  `latest` `8.2` `8` `8.2.16`                                                     | March 9th    | `sha256:dae5dfc98fcc7664617d89c77a0a728b68b3558a5281a58c6f1d9d7aee3e98c4` |
|  `8.2.16-r1-fpm`                                                                 | March 6th    | `sha256:13308e1d491d7a0f89a548b3b250b3b9de5973ecb5146a32f0a0771469d9dbcc` |
|  `8.2.16-r1-fpm-dev`                                                             | March 6th    | `sha256:9bad5615e1841275f5b05866500efffdea969487f1143c1bf446a552a72b43ef` |
|  `8.2.16-r0-fpm`                                                                 | March 2nd    | `sha256:610e014ac497a3d8a7ad34da62165ff9992e3811e3e744e38a1af51771bc24f0` |
|  `8.2.16-r0-fpm-dev`                                                             | March 2nd    | `sha256:27b1d34e2dba5c63a3b72604d21b89bfa93e753de0356aedd9e8316e41293a1f` |

