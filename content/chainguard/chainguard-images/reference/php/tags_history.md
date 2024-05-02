---
title: "php Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the php Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-02 00:37:55
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
|  `latest-fpm-dev` | May 1st      | `sha256:f6a79bd871208f2afa3c80f5dc42d472353fd6c1ebd0b6bc86d8364600a3f1df` |
|  `latest-fpm`     | May 1st      | `sha256:b4e2aab30f3a4d973bcbc0c1d26ee40dc4dac5cc8a8726fda9d2daa7f039f264` |
|  `latest-dev`     | May 1st      | `sha256:b0532cb8cb1a7034e885b887fec3344e0e3a6e60f85b0e513608360a32860cfb` |
|  `latest`         | May 1st      | `sha256:ad8b643954f9236be948b22d9e00070bbaabbbc51892fe0bba316a97297a0cb2` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                          | Last Changed | Digest                                                                    |
|----------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `8-dev` `8.2-dev` `8.2.18-dev` `latest-dev`                                     | May 2nd      | `sha256:bf2764ed9621d8340b6382e410f643d5bf5f87dbd89839371e8febb4377b4a67` |
|  `8` `latest` `8.2` `8.2.18`                                                     | May 2nd      | `sha256:5b26175cb982708cc524449af46b12ea57524f02ba868bb98deccbfb556a3d72` |
|  `8-fpm` `latest-fpm` `8.2.18-r1-fpm` `8.2.18-fpm` `8.2-fpm`                     | May 2nd      | `sha256:4074b4c1c9721041e38f3e4bd3fd25963b2cb0e54d5d65186061dd813c26957e` |
|  `8-fpm-dev` `latest-fpm-dev` `8.2.18-r1-fpm-dev` `8.2-fpm-dev` `8.2.18-fpm-dev` | May 2nd      | `sha256:133947113a996bb848e55c7729e00c7036e2f28a8ecb49146dd5c9cc74ea0632` |
|  `8.2.18-r0-fpm`                                                                 | May 1st      | `sha256:791878d5aebb687bb30ce68730a0a56262f8ea6356b600446865ba75d76cdf93` |
|  `8.2.18-r0-fpm-dev`                                                             | May 1st      | `sha256:80655b81fc1fd386dc759a6ea02f9bad9763c4011370dc2025c7ce81e2fedd0e` |
|  `8.2.17-r0-fpm` `8.2.17-fpm`                                                    | April 5th    | `sha256:70df938cfe5ce70f6fdaa7352810df8a5a932e83c7d1f7e6577f461ce540de8f` |
|  `8.2.17-r0-fpm-dev` `8.2.17-fpm-dev`                                            | April 5th    | `sha256:f3b3275c86c88d9b595bcf988916014dca7f463ab7acf5284374bf59b760810f` |
|  `8.2.17`                                                                        | April 5th    | `sha256:401ddd0c849f14a91d4da7b65a00003e7200df71b2afbd1c080029e24ae1309b` |
|  `8.2.17-dev`                                                                    | April 5th    | `sha256:b1707c9bc4aa241fc171d2accbd3b062c9f270fa7d35c3390470d1614b1fbebd` |

