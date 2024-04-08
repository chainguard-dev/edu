---
title: "jellyfin Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jellyfin Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-08 00:38:35
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
|  `latest`     | April 5th    | `sha256:0922364ebdf94672167ee5dc79d9b5578720376a9a0ef7677a4b69317462ca99` |
|  `latest-dev` | April 5th    | `sha256:f563808d78a08f9738e9887060ade6023f92e11cd7cd3cee2f7c93e78a3b443f` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                         | Last Changed | Digest                                                                    |
|-------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `10.8` `10` `10.8.13`                 | April 5th    | `sha256:dfbeae5cae483f7626b20fc356ee528334dbffc062ba13681f979daa3ff714be` |
|  `10-dev` `latest-dev` `10.8.13-dev` `10.8-dev` | April 5th    | `sha256:9bf9910d65924b2121ebbf6eb77fc8ca3aef4cd122e4aa91bd28bdb262b2d774` |

