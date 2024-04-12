---
title: "gitness Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the gitness Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-12 00:54:01
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/gitness/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/gitness/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/gitness/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/gitness/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | April 11th   | `sha256:0f71ed01d1d939ee12d7dc4e0f9256c2e42d3421ae8587f19ba4956155e18d5d` |
|  `latest-dev` | April 11th   | `sha256:0be09dc90f86f5123e0867ff4280c3d7a3f98e1c6fb3898226e327dda51d8169` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                           | Last Changed | Digest                                                                    |
|---------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `3-dev` `3.0.0_beta6-dev` `3.0-dev` `latest-dev` | April 11th   | `sha256:2a1ecda18e8a8f2f186efe1ed89c1de1ee1d1199121ff4160794c0191523affc` |
|  `3.0.0_beta6` `3` `latest` `3.0`                 | April 11th   | `sha256:64016e50c4dfaf7811f21c9032b35af8d481c1e26c6cf36c46d936a393b990e8` |
|  `3.0.0_beta5-dev`                                | March 28th   | `sha256:f2b14f3832e3d9d519de797e9e1b6118c984640ab152da2a5eedf71cf1fda830` |
|  `3.0.0_beta5`                                    | March 28th   | `sha256:9e45a6ef0329e840054375cd4c136a5d00b1809e4dfa5782c70b1dba53c43c2f` |

