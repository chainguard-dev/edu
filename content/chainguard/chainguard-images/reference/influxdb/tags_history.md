---
title: "influxdb Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the influxdb Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-22 00:47:17
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/influxdb/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/influxdb/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/influxdb/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/influxdb/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | May 21st     | `sha256:e1de2f2dac00536da2efe8082df83d224195ee25cd0d192842474baa260160ab` |
|  `latest-dev` | May 21st     | `sha256:80efaebc440ed03f75d4bdb2722c1a460d145131f740970fc8a5c3e0ab02532d` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `2` `2.7.5` `2.7`                 | May 21st     | `sha256:9e35d0a21a47f71479a201ccefa44cea59762041ecae40aaf1d7e6a3852592ce` |
|  `2.7.5-dev` `latest-dev` `2.7-dev` `2-dev` | May 21st     | `sha256:ba1e6d41df5c48e06007787cd37d8c7e1d686f0ebd070688f7387617b97c167d` |
|  `2.7.0-dev`                                | April 27th   | `sha256:8010a5bd4f42fdf112b072d563a4aca28195ba81f383919cad600b75b539953f` |
|  `2.7.0`                                    | April 27th   | `sha256:8bc8be1c00b8da700bca9293a2d274e98b44ef37c64d1b9ab2a9c15078a27947` |

