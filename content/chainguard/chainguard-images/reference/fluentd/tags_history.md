---
title: "fluentd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the fluentd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-26 00:36:54
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
|  `latest`            | April 25th   | `sha256:8ded105e53fa1d3bbccafe2b0ced19b749b50b23e6e41099d8b9d993b0425f7e` |
|  `latest-dev`        | April 25th   | `sha256:c9fb7457ee3d8fcc074bb2845e882e4d1697f7beaf370e2050e13b1de9e5b9f4` |
|  `latest-splunk-dev` | April 25th   | `sha256:9f1e5df1a369c81d3ee21060d1bbad5ef00414d529e3124f1834e50956338bfe` |
|  `latest-splunk`     | April 25th   | `sha256:fd5e9086427e1884b645f6675b3a5dca3db2f0c56aa2cd856a920fc4cdf05ae5` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                      | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.16.5-r0-splunk` `1.16-splunk` `1.16.5-splunk` `1-splunk`                 | April 25th   | `sha256:544ed4aa98bf82acab7c33a2402706e1125152743a7165e02eacfa99f1ac61f5` |
|  `latest-dev` `1.16-dev` `1.16.5-dev` `1-dev`                                | April 25th   | `sha256:f5d020decb7d2ae450da3a978da4d647e512a53ace3f25b0a1a359be78bb56c8` |
|  `1` `1.16` `latest` `1.16.5`                                                | April 25th   | `sha256:eeb60819ca819e2ecb123944f286cc794c55c4f04fefd0358969fcb9f78409e0` |
|  `1-splunk-dev` `1.16.5-splunk-dev` `1.16-splunk-dev` `1.16.5-r0-splunk-dev` | April 25th   | `sha256:5cdba7414224216d83559498232b9f4b3d0f569ba594e0cf6e296b871486be7e` |
|  `1.16.4-splunk-dev` `1.16.4-r0-splunk-dev`                                  | March 27th   | `sha256:3b27787033b3648c3de96fcd0654098ce79a13f43b2ad6d7dc4f80f2d2db32ba` |
|  `1.16.4-dev`                                                                | March 27th   | `sha256:11600998fec349115f2dce10d0676de2604ee2cfe9e5d9af79d99dd0d19a1a1a` |

