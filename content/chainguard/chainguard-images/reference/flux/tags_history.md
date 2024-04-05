---
title: "flux Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the flux Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-05 00:47:12
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/flux/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/flux/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/flux/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/flux/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | April 4th    | `sha256:649ed8c583b4bd4acee71d61d1fbf3df865bb8b190f181cd491dc9b151184bdb` |
|  `latest-dev` | April 4th    | `sha256:ed98d37fd14bab6225799eda4d5e25f79c0d7c5d1da4f3661b678b6d749e9b8f` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2-dev` `latest-dev` `2.2-dev` `2.2.3-dev` | April 3rd    | `sha256:759f3c3f3e95ffb8e5a5ad87ad4905f9bdfc18e6ac4161febc519c5eea4f3c8a` |
|  `2.2.3` `latest` `2.2` `2`                 | April 3rd    | `sha256:62dcc50b3860f4ebf2b1e86fd4755049f25589e1619945bafae8db034cde8830` |
|  `2.0.1-dev` `2.0-dev`                      | March 18th   | `sha256:450718cfc4046e79d088812a0f0f41c843a0f2f2bc81bca9338248f0d698acdc` |
|  `2.0.1` `2.0`                              | March 18th   | `sha256:d61ee022c0891cc78882e60aa2cb1a2ed1ce6e42aff5a5d6df3502904faa27e3` |

