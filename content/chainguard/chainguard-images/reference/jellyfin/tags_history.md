---
title: "jellyfin Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jellyfin Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-30 00:52:22
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/jellyfin/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/jellyfin/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/jellyfin/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/jellyfin/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 29th   | `sha256:f5aa2ec95931e4363d4d8d523b62a735d8d2e7d5e13ce796bdefa9148e1ad7b0` |
|  `latest`     | April 25th   | `sha256:f28af141cda84400a7514994680ded3a0819497a586a473cb0da6c8b1ffeb539` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                         | Last Changed | Digest                                                                    |
|-------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `10-dev` `10.8.13-dev` `latest-dev` `10.8-dev` | April 29th   | `sha256:e31dc603610ccd47542d24d74a064851b98fb44a3cf85450c32a70a3446296d1` |
|  `latest` `10` `10.8` `10.8.13`                 | April 25th   | `sha256:bc2098a43e9dc611d465c95a20b07df04356178dc72bc9b837507b45542630a6` |

