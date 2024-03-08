---
title: "php Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the php Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-08 00:56:03
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
|  `latest`         | March 7th    | `sha256:3ac47b8661ce885f210229fb87d83fc31854fd26fb2322fe78c88e0ef6acc329` |
|  `latest-dev`     | March 7th    | `sha256:d355c70a2863fc9fb7b0e10b26ebaf00eb4e36a5be948189da6ece18a5771df6` |
|  `latest-fpm`     | March 7th    | `sha256:dbd59edae0d23ee7e43e75e100ffb8a04dd649795e71b991fdece721a9355b9d` |
|  `latest-fpm-dev` | March 7th    | `sha256:78a4365b4da346c0699adabe4445694bc624ed3de3b6338ca96f941ac36e8b80` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                          | Last Changed  | Digest                                                                    |
|----------------------------------------------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `latest-dev` `8.2.16-dev` `8-dev` `8.2-dev`                                     | March 7th     | `sha256:415fb7516999a2616c6f747d026e425756289f326993bd725c70eb0b165d7e4a` |
|  `8.2.16-r2-fpm-dev` `8.2.16-fpm-dev` `8-fpm-dev` `latest-fpm-dev` `8.2-fpm-dev` | March 7th     | `sha256:3ac978939828b6eed421fb9ad3fa6214451815e62ab0f0a4550f3fbc651b68d1` |
|  `8.2` `latest` `8` `8.2.16`                                                     | March 7th     | `sha256:a2d05fb5ee517f4b4007e2839d366c409f06a3b77e3026d12d0848e30c11673c` |
|  `8-fpm` `8.2.16-r2-fpm` `8.2.16-fpm` `latest-fpm` `8.2-fpm`                     | March 7th     | `sha256:945a24b430c1dadd903de162e577c995d1cf3a47d7d1f7bc89be4c4125cd20f8` |
|  `8.2.16-r1-fpm`                                                                 | March 6th     | `sha256:13308e1d491d7a0f89a548b3b250b3b9de5973ecb5146a32f0a0771469d9dbcc` |
|  `8.2.16-r1-fpm-dev`                                                             | March 6th     | `sha256:9bad5615e1841275f5b05866500efffdea969487f1143c1bf446a552a72b43ef` |
|  `8.2.16-r0-fpm`                                                                 | March 2nd     | `sha256:610e014ac497a3d8a7ad34da62165ff9992e3811e3e744e38a1af51771bc24f0` |
|  `8.2.16-r0-fpm-dev`                                                             | March 2nd     | `sha256:27b1d34e2dba5c63a3b72604d21b89bfa93e753de0356aedd9e8316e41293a1f` |
|  `8.2.15-r0-fpm-dev` `8.2.15-fpm-dev`                                            | February 10th | `sha256:aaab9525db8eb05069f27cd5eb86c7e2608aef96a53e2a3c2b5e6be0392fa9fb` |
|  `8.2.15-dev`                                                                    | February 10th | `sha256:c0df0ce9b46035b96b3b2049c2fbfd347bb74785ee53019b6f3a34626e6f9668` |

