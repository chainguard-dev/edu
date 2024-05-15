---
title: "fluentd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the fluentd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-15 00:39:35
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/fluentd/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/fluentd/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/fluentd/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/fluentd/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)              | Last Changed | Digest                                                                    |
|----------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev`        | April 29th   | `sha256:18b78363e9cceaf46799777e3465821dbc79624b75ba6fa4508ad0a7d0cea906` |
|  `latest-splunk-dev` | April 29th   | `sha256:706259c4cb4d72e5bd4272b50c20e7b673176a3deb1a9810932774afe6348345` |
|  `latest`            | April 25th   | `sha256:8ded105e53fa1d3bbccafe2b0ced19b749b50b23e6e41099d8b9d993b0425f7e` |
|  `latest-splunk`     | April 25th   | `sha256:fd5e9086427e1884b645f6675b3a5dca3db2f0c56aa2cd856a920fc4cdf05ae5` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                      | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.16.5-r0-splunk-dev` `1-splunk-dev` `1.16-splunk-dev` `1.16.5-splunk-dev` | May 14th     | `sha256:2cc043d14255027a8e2bd3ae2085293603709547bf825ed95c85e0ea624ab592` |
|  `1.16.5-dev` `1-dev` `1.16-dev` `latest-dev`                                | May 14th     | `sha256:806cc2d0de154dbd69abea9a1df87c334c8b808fbf548f420ade0ff0ce845098` |
|  `1.16-splunk` `1.16.5-splunk` `1-splunk` `1.16.5-r0-splunk`                 | May 13th     | `sha256:108a45f2731a99a830b1467f2132e8379aac4bf18f4808e51863c5d252292e61` |
|  `latest` `1.16` `1.16.5` `1`                                                | May 13th     | `sha256:0c6d2bb8277db0bb672e66a151ca3d14fd0d2b53eb63842ee0c0e7a2fbce6ea8` |

