---
title: "fluentd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the fluentd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-25 00:53:12
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
|  `latest-splunk-dev` | April 24th   | `sha256:7a8941aaa773f834ecae6ebc9f5616000bd6ee773e512629e75a7aacdf1bd35c` |
|  `latest`            | April 24th   | `sha256:9374f67c8b3f62b9fbc15789f6850f2871473705e229cb6f7ce8100df198456a` |
|  `latest-dev`        | April 24th   | `sha256:454beb1d13c1c4936ea1ea9b8ce7ab8a0e0cd4e046e865bab8e7bc6322327c46` |
|  `latest-splunk`     | April 24th   | `sha256:397ec7bd75d5f94fe2b4c328a82c91dedf2b213698547aafe0484d677d5b7b57` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                      | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.16-dev` `1-dev` `latest-dev` `1.16.5-dev`                                | April 24th   | `sha256:1ec7ff2cc6cabb159df7b050a416fe1a8c9d5c6d052d409062bd7f9c4b6ac897` |
|  `1.16-splunk` `1.16.5-splunk` `1-splunk` `1.16.5-r0-splunk`                 | April 24th   | `sha256:4c440e502d953afe9a7f2c2db22ee0e6e9507be5ff334231b040e5186af98bfa` |
|  `latest` `1.16.5` `1` `1.16`                                                | April 24th   | `sha256:ccb94df222bca6eb1b20e87892d608f5470479296615078cbe3a83548c672b5a` |
|  `1.16.5-r0-splunk-dev` `1.16-splunk-dev` `1-splunk-dev` `1.16.5-splunk-dev` | April 24th   | `sha256:79405d10565a8bd7d8aac10376308c7248a473e1fcd63c185f7df573d45824fb` |
|  `1.16.4-splunk-dev` `1.16.4-r0-splunk-dev`                                  | March 27th   | `sha256:3b27787033b3648c3de96fcd0654098ce79a13f43b2ad6d7dc4f80f2d2db32ba` |
|  `1.16.4-dev`                                                                | March 27th   | `sha256:11600998fec349115f2dce10d0676de2604ee2cfe9e5d9af79d99dd0d19a1a1a` |

