---
title: "php Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the php Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-03 00:45:55
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
|  `latest-fpm-dev` | May 2nd      | `sha256:a3ceecc9042e30f0ba5fcb1e3fe9a4249ca80f72229453e5f599574a156b9151` |
|  `latest-fpm`     | May 2nd      | `sha256:06ea35af0c0aba04a29e39acf4f2e0b9aeaf0b4291f53507807ab9920dcb96ac` |
|  `latest`         | May 2nd      | `sha256:f7b564b007ba7387a2095bb6039f0badf11b7cb810d1549f36f6d9997143a9e5` |
|  `latest-dev`     | May 2nd      | `sha256:7ee76e7035c7ed9975687801bc96e165082b0366d9cbd0ef31a3da422eaf7f26` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                          | Last Changed | Digest                                                                    |
|----------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `8.2-fpm` `8.2.18-fpm` `8.2.18-r1-fpm` `8-fpm` `latest-fpm`                     | May 2nd      | `sha256:824014d1dea3f1263c736ecf25e36b4abb270ebf7d6f4960b9800bc004e4dc7d` |
|  `latest-fpm-dev` `8.2-fpm-dev` `8.2.18-fpm-dev` `8-fpm-dev` `8.2.18-r1-fpm-dev` | May 2nd      | `sha256:fb4f018bdde359c8613396f8451383aa85efbb38fb7ed54033fcc5c9de5f0f49` |
|  `latest` `8.2.18` `8` `8.2`                                                     | May 2nd      | `sha256:a97a063904682f4ecd90164cd59cbd6c88337a6f7f9762ac19b2a573d204b38a` |
|  `latest-dev` `8-dev` `8.2-dev` `8.2.18-dev`                                     | May 2nd      | `sha256:d0792ac3542ce5e175ed4363bf6539c496e348f7aaf06a1af250a30802dc27fc` |
|  `8.2.18-r0-fpm`                                                                 | May 1st      | `sha256:791878d5aebb687bb30ce68730a0a56262f8ea6356b600446865ba75d76cdf93` |
|  `8.2.18-r0-fpm-dev`                                                             | May 1st      | `sha256:80655b81fc1fd386dc759a6ea02f9bad9763c4011370dc2025c7ce81e2fedd0e` |
|  `8.2.17-r0-fpm` `8.2.17-fpm`                                                    | April 5th    | `sha256:70df938cfe5ce70f6fdaa7352810df8a5a932e83c7d1f7e6577f461ce540de8f` |
|  `8.2.17-r0-fpm-dev` `8.2.17-fpm-dev`                                            | April 5th    | `sha256:f3b3275c86c88d9b595bcf988916014dca7f463ab7acf5284374bf59b760810f` |
|  `8.2.17`                                                                        | April 5th    | `sha256:401ddd0c849f14a91d4da7b65a00003e7200df71b2afbd1c080029e24ae1309b` |
|  `8.2.17-dev`                                                                    | April 5th    | `sha256:b1707c9bc4aa241fc171d2accbd3b062c9f270fa7d35c3390470d1614b1fbebd` |

