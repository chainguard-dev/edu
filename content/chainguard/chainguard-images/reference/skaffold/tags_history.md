---
title: "skaffold Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the skaffold Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-22 00:47:17
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
|  `latest`     | May 21st     | `sha256:a504557505f78e9541bac214d28c04dfe0b9fb7ca57a886e08b5412e63e7829b` |
|  `latest-dev` | May 20th     | `sha256:041869efc422df927518c0425ee1e8a2f3ba0a51b04099af726c30063ea719b8` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2.12.0` `2` `latest` `2.12`                 | May 21st     | `sha256:bf9f4411eeb238fd0e97fec78cf509ddd3055ce6b48ae06e34ebaef2d657515a` |
|  `latest-dev` `2.12.0-dev` `2-dev` `2.12-dev` | May 21st     | `sha256:85f9056fbf72b023a0a28756173fe75fb209ba6f0606ce82b3dd38948bc90b69` |
|  `2.11.1-dev` `2.11-dev`                      | May 14th     | `sha256:792efada85093dc16330dd58d8f517ef7314dfff906ccf2b14e370a3472a112c` |
|  `2.11` `2.11.1`                              | May 13th     | `sha256:3043b565d3e1e4940534b5b57c3998bc25988e6e9ed3e63276eee81c31f6c803` |
|  `2.4.0-dev`                                  | May 9th      | `sha256:372a7be3e7c7d86ae162e51e4d46de6d3df2e16df4139b02b2a67cf4d3bd5a08` |
|  `2.4.0`                                      | May 9th      | `sha256:997c86d21f52ab05db7cd830b687fdbc45906f787869659acc3e5ece9539b08a` |
|  `2.3.1` `2.3`                                | May 1st      | `sha256:6fe0d91b705f98ba087ab48a319e1894ac7ab9cd56a829d7e51e770f2965a867` |
|  `2.3.1-dev` `2.3-dev`                        | April 25th   | `sha256:f275f0c8dd5f8ee1cfe11d6f9bbb2a25c44ff6fe276b2af1dbbde9ad3bcf4386` |

