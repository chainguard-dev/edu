---
title: "ko Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the ko Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-15 00:39:35
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/ko/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/ko/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/ko/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/ko/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 29th   | `sha256:b58a1634c1b1e701b19767e525f9ed8e86deb1fb19951f3b5d63396b738b19c9` |
|  `latest`     | April 29th   | `sha256:2fca68260d67a48e8ea01b788c5b61d236bf427804568aa77c79a970f0ea6cb7` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0-dev` `latest-dev` `0.15.2-dev` `0.15-dev` | May 14th     | `sha256:78c2849b9e7cf63530a55d33a5810506cbedc8be51dfa9281cd3646505b0dfdc` |
|  `latest` `0.15.2` `0.15` `0`                 | May 14th     | `sha256:cfd1bde8c059ce46314a8dc5b298817851748469209b8a43803136a231a2d5db` |

