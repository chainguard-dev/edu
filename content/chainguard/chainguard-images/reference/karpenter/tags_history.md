---
title: "karpenter Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the karpenter Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-07 00:51:54
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/karpenter/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/karpenter/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/karpenter/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/karpenter/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | March 6th    | `sha256:e628177e411f94b73f6350a784af166049b2319c6ad0f997df5b24d99494bdf4` |
|  `latest-dev` | March 6th    | `sha256:ed8d5017ac641ad8ec02eeddfe16139ca2d4d5175d2a1aa00f4645669b522524` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed  | Digest                                                                    |
|-----------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `0.35.0` `0.35` `latest` `0`                 | March 6th     | `sha256:8465514ae53aaa3f50c6ce9b4693e22f17c53816a864e04266c5d22ade2f56c7` |
|  `latest-dev` `0.35-dev` `0-dev` `0.35.0-dev` | March 6th     | `sha256:afbccd58c77c9e4794d90129948ca030b33a528b0e2a5014ef92390d6acc698e` |
|  `0.34-dev` `0.34.1-dev`                      | February 26th | `sha256:ea6f1b7b07c884e7be07c3a93c716465b8220fbe2bf84a7f49cc1bf440c35865` |
|  `0.34` `0.34.1`                              | February 26th | `sha256:825d24feda8cac13f08fc41114b873f8a42b46b3037eabeb39f0de8a6ab20e08` |
|  `0.34.0-dev`                                 | February 17th | `sha256:bc792a458800ee813131a0f93d7621e8a6bd926b5a28fe296e502d5b23b22480` |

