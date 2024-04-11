---
title: "php Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the php Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-11 00:54:43
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
|  `latest-fpm`         | April 9th    | `sha256:9b56e4974bcbb93b71ec940dbc949ec58b90999b6f16a3a58a60d728058334dc` |
|  `latest-fpm-dev`     | April 9th    | `sha256:667e2269b70403a9ee3c1fb85223f1dd9207f4bc752ed22291288f9217beea7d` |
|  `latest`             | April 9th    | `sha256:a57e6070f56c4706683a18e8240e3c3d1b10dfa26ea18924556df70d0830f176` |
|  `latest-dev`         | April 9th    | `sha256:1b8954a83925774039f2d8144598ba2792cd999b6a32e39cfde0fa6fa1ace499` |
|  `latest-laravel-dev` | April 9th    | `sha256:d559ae527a000efff5436aba5bce8cca55328bb379d1df3a604d66af60b323e7` |
|  `latest-laravel`     | April 9th    | `sha256:e5dd60611c4f83d245640a355c52b039cd3352455bfb9e77c5f217d8b31eb862` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                          | Last Changed | Digest                                                                    |
|----------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `8.2` `8.2.18` `8`                                                     | April 9th    | `sha256:050ff424431fc2b9cbec0934ef5c17061907181dd529efbfb533737f7e5abdc6` |
|  `8.2.18-dev` `8.2-dev` `8-dev` `latest-dev`                                     | April 9th    | `sha256:78ebcea5c5bd40f4759c06c2b60dae7afab4cfb1533657d0f3dd8b2f590242a1` |
|  `8.2.18-r0-fpm-dev` `8.2.18-fpm-dev` `latest-fpm-dev` `8-fpm-dev` `8.2-fpm-dev` | April 9th    | `sha256:7287f55041c7fd61a804d6cac682a9a1e10578d447173796b0dd9cee2d355be6` |
|  `8-fpm` `8.2.18-fpm` `8.2.18-r0-fpm` `latest-fpm` `8.2-fpm`                     | April 9th    | `sha256:0a2225e241aac7814f3366d6ad2ed509929935767c6d4864ce3eeee2b4b2105e` |
|  `8.2.17-r0-fpm` `8.2.17-fpm`                                                    | April 5th    | `sha256:70df938cfe5ce70f6fdaa7352810df8a5a932e83c7d1f7e6577f461ce540de8f` |
|  `8.2.17-r0-fpm-dev` `8.2.17-fpm-dev`                                            | April 5th    | `sha256:f3b3275c86c88d9b595bcf988916014dca7f463ab7acf5284374bf59b760810f` |
|  `8.2.17`                                                                        | April 5th    | `sha256:401ddd0c849f14a91d4da7b65a00003e7200df71b2afbd1c080029e24ae1309b` |
|  `8.2.17-dev`                                                                    | April 5th    | `sha256:b1707c9bc4aa241fc171d2accbd3b062c9f270fa7d35c3390470d1614b1fbebd` |
|  `8.2.16-fpm-dev` `8.2.16-r2-fpm-dev`                                            | March 12th   | `sha256:97f58bfd708efb00b13ae23147578742f71b69418cf63ac57f84207f3712264c` |
|  `8.2.16-dev`                                                                    | March 12th   | `sha256:e00efa792d0cabce50f11a8aca51fe58801754f3900d1f1a748169b15186b84a` |

