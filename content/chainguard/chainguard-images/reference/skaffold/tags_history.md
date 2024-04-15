---
title: "skaffold Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the skaffold Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-15 03:08:24
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
|  `latest-dev` | April 12th   | `sha256:e5bf39fe196d2ebf5c4369ad23b71f734d0e082809b3abeb066047095cf6a0d8` |
|  `latest`     | April 12th   | `sha256:25beece86b08853db28f26a2ab134fea23dee6938de4a13c35309c0c31515902` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2.11.1-dev` `latest-dev` `2.11-dev` `2-dev` | April 12th   | `sha256:6e6a27ebda4a700b121b33d4a0ddb090531b40a17afcf6b409c3b4bf3af36566` |
|  `2.11.1` `latest` `2.11` `2`                 | April 12th   | `sha256:9bbe39fd9e0a6227b2701d3486a8e603e075f1e98fd8b584faa5499534ae9761` |
|  `2.11.0`                                     | April 9th    | `sha256:4c164fcee27f736d0e8672b2f7f7b6ce92ddbcc50435c1d62ee2ae7e461c189b` |
|  `2.11.0-dev`                                 | April 9th    | `sha256:8040ff42c08ccf2cb330ac7be31362e40eeb0ff61fb10e8029593d0ea30d8555` |
|  `2.10-dev` `2.10.1-dev`                      | April 2nd    | `sha256:3c1c7adb0140d2eac476b6dcca8a5eda5cbfcc36b33f78b51764feb267328438` |
|  `2.10.1` `2.10`                              | April 1st    | `sha256:2dcb9e504cde7b7fa869b45408d14f0ac2c401df49cc5c1829bb076b71c80174` |

