---
title: "fluentd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the fluentd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-02 00:37:55
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
|  `1` `1.16.5` `latest` `1.16`                                                | May 1st      | `sha256:8834728343010a7bd95d50fef487dc4f06d0bfa89252c0812ecc6ccaf7afb3a0` |
|  `1-splunk` `1.16.5-splunk` `1.16.5-r0-splunk` `1.16-splunk`                 | May 1st      | `sha256:68d5da028ab91e4686e67be48a94bd229fe44908151442b2a431b43d3ea1188d` |
|  `1-splunk-dev` `1.16.5-r0-splunk-dev` `1.16.5-splunk-dev` `1.16-splunk-dev` | May 1st      | `sha256:c23f1ce7cabfc4cf95d3c80ec74c5d6ec60f2987f2be7eae0e09b42df030a301` |
|  `latest-dev` `1.16-dev` `1-dev` `1.16.5-dev`                                | May 1st      | `sha256:b4d17d434efc2b6ea98a2b7ef7294e7c63eb388553e7a833c4662aa56ad8f81d` |

