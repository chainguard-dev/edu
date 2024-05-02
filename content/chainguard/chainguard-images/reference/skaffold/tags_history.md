---
title: "skaffold Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the skaffold Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-02 00:37:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/skaffold/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/skaffold/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/skaffold/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/skaffold/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 1st      | `sha256:cd23735a2d360dbf26fb4644f1247752e398de7e6de88512a3eeaca97c263bf8` |
|  `latest`     | May 1st      | `sha256:c06b71db25d918d88503b5e730d6b5bb21a80ab5a391af00f0e804d710c89399` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2.11.1-dev` `2-dev` `latest-dev` `2.11-dev` | May 1st      | `sha256:22c8a8bab9399e382eb02841e4f5a4ef74d31426ad8d16f57a8ecfe2c9e835b9` |
|  `2.11` `latest` `2.11.1` `2`                 | May 1st      | `sha256:ab60d8bcb2640a3c4d330da48ce0f4137c779db62e71ea84ae4743473c096256` |
|  `2.11.0`                                     | April 9th    | `sha256:4c164fcee27f736d0e8672b2f7f7b6ce92ddbcc50435c1d62ee2ae7e461c189b` |
|  `2.11.0-dev`                                 | April 9th    | `sha256:8040ff42c08ccf2cb330ac7be31362e40eeb0ff61fb10e8029593d0ea30d8555` |
|  `2.10-dev` `2.10.1-dev`                      | April 2nd    | `sha256:3c1c7adb0140d2eac476b6dcca8a5eda5cbfcc36b33f78b51764feb267328438` |
|  `2.3.1` `2.3`                                | May 1st      | `sha256:6fe0d91b705f98ba087ab48a319e1894ac7ab9cd56a829d7e51e770f2965a867` |
|  `2.3.1-dev` `2.3-dev`                        | April 25th   | `sha256:f275f0c8dd5f8ee1cfe11d6f9bbb2a25c44ff6fe276b2af1dbbde9ad3bcf4386` |

