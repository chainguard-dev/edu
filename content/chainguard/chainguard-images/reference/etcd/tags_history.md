---
title: "etcd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the etcd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-05 17:06:05
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/etcd/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/etcd/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/etcd/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/etcd/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed  | Digest                                                                    |
|---------------|---------------|---------------------------------------------------------------------------|
|  `latest-dev` | March 1st     | `sha256:85c9d7c432255dcbc5758aa5de03c23febafec0c444b06f40ac780af80dff98c` |
|  `latest`     | February 28th | `sha256:3fc27ac704a2ff673c6728c0725c40a510e8b9bd13b80fbac162d40a5270a1be` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                      | Last Changed  | Digest                                                                    |
|----------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `3.5.12-dev` `3-dev` `latest-dev` `3.5-dev` | March 2nd     | `sha256:f7950039dc47166fd50a9e69caefac20ebe1b75a7daa7141a2f54324e817848c` |
|  `3` `latest` `3.5` `3.5.12`                 | February 28th | `sha256:830537522569f35af2141e7a5a3fb6f32855af4887bc5cd682447aa79e226e34` |

