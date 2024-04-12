---
title: "php Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the php Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-12 00:54:01
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
|  `latest`             | April 11th   | `sha256:cc17d7cc2bf52604db51c75903ee1893bcd914473c9d139f446e3d3e20ed42e8` |
|  `latest-dev`         | April 11th   | `sha256:94aaff8eec1165db1572b2f832b07640a844906d85fb04c2ba57921db5d665e8` |
|  `latest-laravel`     | April 11th   | `sha256:a74ff610496cd5124fbd94f6466140d1eba5f08f8baa88770792417906d7cc2b` |
|  `latest-laravel-dev` | April 11th   | `sha256:2e4289539792794f789768006d1587edef7312a82980ded2c71ef4aa342cdf6d` |
|  `latest-fpm`         | April 11th   | `sha256:b557b665e7207245532bf3809e86c367fb9cb5c2b2eb241e74ec2798cb8d42b5` |
|  `latest-fpm-dev`     | April 11th   | `sha256:238a0bb5452b2241be994238b1d43c6fce6b294a7a89c9807c3b9a0c6bcef127` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                          | Last Changed | Digest                                                                    |
|----------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `8.2.18-dev` `8.2-dev` `latest-dev` `8-dev`                                     | April 11th   | `sha256:d160bd8ad18fd189102599ceec68aa11cbff4c6029a1fecd1e42563b79556bf9` |
|  `latest` `8` `8.2` `8.2.18`                                                     | April 11th   | `sha256:0d1bffdf8dd6141dd04f13e929561c91e9fb39c3f962729b5b9789b08a6472c0` |
|  `8-fpm-dev` `8.2.18-fpm-dev` `latest-fpm-dev` `8.2.18-r0-fpm-dev` `8.2-fpm-dev` | April 11th   | `sha256:7d55b3abab4ca15491a0b2bef819aba3f751cd45c504d7e5fa7057a2163073fd` |
|  `8.2-fpm` `latest-fpm` `8.2.18-r0-fpm` `8.2.18-fpm` `8-fpm`                     | April 11th   | `sha256:08db7fc43487c9ff749040b254a65066a6dc372d204f1f358a1f5a7438211f8f` |
|  `8.2.17-r0-fpm` `8.2.17-fpm`                                                    | April 5th    | `sha256:70df938cfe5ce70f6fdaa7352810df8a5a932e83c7d1f7e6577f461ce540de8f` |
|  `8.2.17-r0-fpm-dev` `8.2.17-fpm-dev`                                            | April 5th    | `sha256:f3b3275c86c88d9b595bcf988916014dca7f463ab7acf5284374bf59b760810f` |
|  `8.2.17`                                                                        | April 5th    | `sha256:401ddd0c849f14a91d4da7b65a00003e7200df71b2afbd1c080029e24ae1309b` |
|  `8.2.17-dev`                                                                    | April 5th    | `sha256:b1707c9bc4aa241fc171d2accbd3b062c9f270fa7d35c3390470d1614b1fbebd` |
|  `8.2.16-fpm-dev` `8.2.16-r2-fpm-dev`                                            | March 12th   | `sha256:97f58bfd708efb00b13ae23147578742f71b69418cf63ac57f84207f3712264c` |
|  `8.2.16-dev`                                                                    | March 12th   | `sha256:e00efa792d0cabce50f11a8aca51fe58801754f3900d1f1a748169b15186b84a` |

