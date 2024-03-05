---
title: "php Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the php Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-05 17:06:05
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
|  `latest-dev`     | March 1st    | `sha256:978fc84cf048654ba415856797e436784a846d46942f8bb3399adb35a51a61cd` |
|  `latest-fpm`     | March 1st    | `sha256:4c29a748a1a2db9fc04778da7633897d1bc342215e3dc26e7361ca7a46410c6e` |
|  `latest`         | March 1st    | `sha256:4cabd85819d4fc3ae4f9fb6e0c67b570156915ee197c4cd614e5b0dc4dda90cd` |
|  `latest-fpm-dev` | March 1st    | `sha256:3b09b59c530914b054d6e296e6a43cb2d51694c32b1aac92ec5e0a2a2c283705` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                          | Last Changed  | Digest                                                                    |
|----------------------------------------------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `8.2` `latest` `8.2.16` `8`                                                     | March 2nd     | `sha256:f23c568711ebd95e2f3317da4dd6813fd2d898d66b3062947759410ee77e276b` |
|  `latest-dev` `8-dev` `8.2.16-dev` `8.2-dev`                                     | March 2nd     | `sha256:b403988f22a5b55fb3ba19a2fc3d69ad279311ca4101f37684a186bcb7bf05dd` |
|  `8.2-fpm` `8.2.16-fpm` `latest-fpm` `8.2.16-r0-fpm` `8-fpm`                     | March 2nd     | `sha256:610e014ac497a3d8a7ad34da62165ff9992e3811e3e744e38a1af51771bc24f0` |
|  `8.2-fpm-dev` `latest-fpm-dev` `8.2.16-r0-fpm-dev` `8-fpm-dev` `8.2.16-fpm-dev` | March 2nd     | `sha256:27b1d34e2dba5c63a3b72604d21b89bfa93e753de0356aedd9e8316e41293a1f` |
|  `8.2.15-r0-fpm-dev` `8.2.15-fpm-dev`                                            | February 10th | `sha256:aaab9525db8eb05069f27cd5eb86c7e2608aef96a53e2a3c2b5e6be0392fa9fb` |
|  `8.2.15-dev`                                                                    | February 10th | `sha256:c0df0ce9b46035b96b3b2049c2fbfd347bb74785ee53019b6f3a34626e6f9668` |

