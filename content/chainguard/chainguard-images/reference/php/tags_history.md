---
title: "php Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the php Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-07 00:51:54
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
|  `latest-dev`     | March 6th    | `sha256:51f9978f38a80496eadcce468de9d92f392e2dab5d6fea3f50aee1677c67a572` |
|  `latest`         | March 6th    | `sha256:bbd566a6fb9c23669ff9a40b29159c89623a7ef8b1eb852f90b3d5fc047bb64d` |
|  `latest-fpm`     | March 6th    | `sha256:af0031a00a2cde7f964d15809c22af5344189382111a8964dadd97a1201661ff` |
|  `latest-fpm-dev` | March 6th    | `sha256:2e95c47eb3ea8717589aecac4941879a90f6f7e5db1ae02f538908a5595a6a63` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                          | Last Changed  | Digest                                                                    |
|----------------------------------------------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `8.2.16` `latest` `8.2` `8`                                                     | March 6th     | `sha256:59cab33d4ba0b7eac878e341e999eff3812e58a34de623927cc49841dfbf89cf` |
|  `8.2-fpm-dev` `8.2.16-fpm-dev` `8.2.16-r2-fpm-dev` `8-fpm-dev` `latest-fpm-dev` | March 6th     | `sha256:0f75b0e0347e47cf5ed8ed516720ca5c429c94a262fca020a3a85a4daaf459bd` |
|  `8.2-fpm` `8-fpm` `latest-fpm` `8.2.16-r2-fpm` `8.2.16-fpm`                     | March 6th     | `sha256:73b090efd47cb7133a0b033eb390d21ba82bb4a8e24aeea0158a624a292d609a` |
|  `8-dev` `latest-dev` `8.2.16-dev` `8.2-dev`                                     | March 6th     | `sha256:28206c5d5b149b4c0c2056110bf071b452d3bd2767b9d54272b8b0724e11b6b8` |
|  `8.2.16-r1-fpm`                                                                 | March 6th     | `sha256:13308e1d491d7a0f89a548b3b250b3b9de5973ecb5146a32f0a0771469d9dbcc` |
|  `8.2.16-r1-fpm-dev`                                                             | March 6th     | `sha256:9bad5615e1841275f5b05866500efffdea969487f1143c1bf446a552a72b43ef` |
|  `8.2.16-r0-fpm`                                                                 | March 2nd     | `sha256:610e014ac497a3d8a7ad34da62165ff9992e3811e3e744e38a1af51771bc24f0` |
|  `8.2.16-r0-fpm-dev`                                                             | March 2nd     | `sha256:27b1d34e2dba5c63a3b72604d21b89bfa93e753de0356aedd9e8316e41293a1f` |
|  `8.2.15-r0-fpm-dev` `8.2.15-fpm-dev`                                            | February 10th | `sha256:aaab9525db8eb05069f27cd5eb86c7e2608aef96a53e2a3c2b5e6be0392fa9fb` |
|  `8.2.15-dev`                                                                    | February 10th | `sha256:c0df0ce9b46035b96b3b2049c2fbfd347bb74785ee53019b6f3a34626e6f9668` |

