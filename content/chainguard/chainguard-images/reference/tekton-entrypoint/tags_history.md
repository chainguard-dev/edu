---
title: "tekton-entrypoint Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the tekton-entrypoint Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-01 00:46:56
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/tekton-entrypoint/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/tekton-entrypoint/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/tekton-entrypoint/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/tekton-entrypoint/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 30th   | `sha256:1e177c7ed5615a87d648726820d0a15c1824baf208c22596d54a55e6fc3277ed` |
|  `latest`     | April 26th   | `sha256:f96ae0e638c9946d55fa83c12ac74e8b87cfac17176ee3b883b5d87e496bd17d` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0-dev` `latest-dev` `0.59.0-dev` `0.59-dev` | April 30th   | `sha256:9dbb6b68aad960f06d5d457cad487544b31c06f4a1c2edce826a41e23efa2546` |
|  `0.59.0` `0` `latest` `0.59`                 | April 26th   | `sha256:51fcf09c64c4a6d4297ea5be8db8d48aad7935fa49365ea67a348463e76f5f40` |
|  `0.58` `0.58.0`                              | April 21st   | `sha256:01eb12e317c5273f23db4f6a8de73701958bdf999c876c1f6dea7f6f398e7fba` |
|  `0.58-dev` `0.58.0-dev`                      | April 21st   | `sha256:ba941d5bde633cea4ce877b5a8ef0f90086f95cbec9184b91b0b1112c3fb1a3c` |

