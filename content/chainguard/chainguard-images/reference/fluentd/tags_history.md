---
title: "fluentd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the fluentd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-07 00:45:47
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
|  `1.16-splunk` `1.16.5-splunk` `1.16.5-r0-splunk` `1-splunk`                 | May 6th      | `sha256:24b3a1f3ed60623fd53235a2abda496d93c1b1230b656a101b96bf0130864134` |
|  `1.16.5-r0-splunk-dev` `1-splunk-dev` `1.16.5-splunk-dev` `1.16-splunk-dev` | May 6th      | `sha256:4d6b7673c788186d060a8d743ba97f760b4c87ae84483ad4089de4081485f0b0` |
|  `1` `latest` `1.16` `1.16.5`                                                | May 3rd      | `sha256:f37ff0019ba55729ec8b200bcb1d3ce605dad459795a586e05a473ce51b79e7b` |
|  `latest-dev` `1.16-dev` `1-dev` `1.16.5-dev`                                | May 3rd      | `sha256:122b44672f743e81debeccd5df5538943e5e9e0bc6ff73f3ac052ec29a30476e` |

