---
title: "php Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the php Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-18 00:43:55
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

| Tag (s)               | Last Changed | Digest                                                                    |
|-----------------------|--------------|---------------------------------------------------------------------------|
|  `latest-fpm`         | April 17th   | `sha256:c4166e4b58f5d9f463e81647928015ff93db78bb15e79ee93376c814d83f828e` |
|  `latest-fpm-dev`     | April 17th   | `sha256:ec9b2af56f429f32983130404763a50230b174e73a96854a96e84ca81e5875e4` |
|  `latest`             | April 11th   | `sha256:cc17d7cc2bf52604db51c75903ee1893bcd914473c9d139f446e3d3e20ed42e8` |
|  `latest-dev`         | April 11th   | `sha256:94aaff8eec1165db1572b2f832b07640a844906d85fb04c2ba57921db5d665e8` |
|  `latest-laravel`     | April 11th   | `sha256:a74ff610496cd5124fbd94f6466140d1eba5f08f8baa88770792417906d7cc2b` |
|  `latest-laravel-dev` | April 11th   | `sha256:2e4289539792794f789768006d1587edef7312a82980ded2c71ef4aa342cdf6d` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                          | Last Changed | Digest                                                                    |
|----------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `8-fpm` `latest-fpm` `8.2.18-fpm` `8.2-fpm` `8.2.18-r0-fpm`                     | April 17th   | `sha256:79d3391d16223e3488089daab1395beff33b5623e1255e04638a373771f42cdd` |
|  `8.2-fpm-dev` `latest-fpm-dev` `8.2.18-fpm-dev` `8-fpm-dev` `8.2.18-r0-fpm-dev` | April 17th   | `sha256:8d89115e2281dd5f8551a8582f500683dad2e62b41ad72d5043074622c2cd723` |
|  `8.2.18-dev` `8.2-dev` `latest-dev` `8-dev`                                     | April 11th   | `sha256:d160bd8ad18fd189102599ceec68aa11cbff4c6029a1fecd1e42563b79556bf9` |
|  `latest` `8` `8.2` `8.2.18`                                                     | April 11th   | `sha256:0d1bffdf8dd6141dd04f13e929561c91e9fb39c3f962729b5b9789b08a6472c0` |
|  `8.2.17-r0-fpm` `8.2.17-fpm`                                                    | April 5th    | `sha256:70df938cfe5ce70f6fdaa7352810df8a5a932e83c7d1f7e6577f461ce540de8f` |
|  `8.2.17-r0-fpm-dev` `8.2.17-fpm-dev`                                            | April 5th    | `sha256:f3b3275c86c88d9b595bcf988916014dca7f463ab7acf5284374bf59b760810f` |
|  `8.2.17`                                                                        | April 5th    | `sha256:401ddd0c849f14a91d4da7b65a00003e7200df71b2afbd1c080029e24ae1309b` |
|  `8.2.17-dev`                                                                    | April 5th    | `sha256:b1707c9bc4aa241fc171d2accbd3b062c9f270fa7d35c3390470d1614b1fbebd` |

