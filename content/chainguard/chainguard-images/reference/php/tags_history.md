---
title: "php Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the php Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-08 00:38:35
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
|  `latest-laravel`     | April 5th    | `sha256:93962d472f713d79e2139f9352234b8a81258f4c07362aea3b54e044fd308187` |
|  `latest-laravel-dev` | April 5th    | `sha256:7b1602ecab8b5e71aae7fa76d26c1dce774795c06fd24444af293d87689f3ca5` |
|  `latest-fpm-dev`     | April 5th    | `sha256:cc06ca8e270f2f9e79315a8336b34bbb1ffa697dbedf9396e0e86d30d9d8fcdd` |
|  `latest-fpm`         | April 5th    | `sha256:bbf315baf73a330d5641db9eef0eb693e88425d2ae3392b58af851e818c66eb0` |
|  `latest-dev`         | April 5th    | `sha256:a4da2b59aeece59d4fa9f789b7a08a82740461bd780d9ce8e4ddc74667386893` |
|  `latest`             | April 5th    | `sha256:76626bf58900dce4fa87024006cc716b6ea3e5143277f51c4b829a9ed1c112fe` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                          | Last Changed | Digest                                                                    |
|----------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `8-fpm-dev` `latest-fpm-dev` `8.2.17-r0-fpm-dev` `8.2.17-fpm-dev` `8.2-fpm-dev` | April 5th    | `sha256:f3b3275c86c88d9b595bcf988916014dca7f463ab7acf5284374bf59b760810f` |
|  `latest-fpm` `8.2.17-r0-fpm` `8.2.17-fpm` `8.2-fpm` `8-fpm`                     | April 5th    | `sha256:70df938cfe5ce70f6fdaa7352810df8a5a932e83c7d1f7e6577f461ce540de8f` |
|  `8.2` `latest` `8` `8.2.17`                                                     | April 5th    | `sha256:401ddd0c849f14a91d4da7b65a00003e7200df71b2afbd1c080029e24ae1309b` |
|  `8.2-dev` `latest-dev` `8-dev` `8.2.17-dev`                                     | April 5th    | `sha256:b1707c9bc4aa241fc171d2accbd3b062c9f270fa7d35c3390470d1614b1fbebd` |
|  `8.2.16-fpm-dev` `8.2.16-r2-fpm-dev`                                            | March 12th   | `sha256:97f58bfd708efb00b13ae23147578742f71b69418cf63ac57f84207f3712264c` |
|  `8.2.16-dev`                                                                    | March 12th   | `sha256:e00efa792d0cabce50f11a8aca51fe58801754f3900d1f1a748169b15186b84a` |
|  `8.2.16-r2-fpm` `8.2.16-fpm`                                                    | March 9th    | `sha256:4bd1cd3d6bf2a801bdf5f948742ab0133ffdb50bc787e2be65f16ed2feeb191c` |
|  `8.2.16`                                                                        | March 9th    | `sha256:dae5dfc98fcc7664617d89c77a0a728b68b3558a5281a58c6f1d9d7aee3e98c4` |

