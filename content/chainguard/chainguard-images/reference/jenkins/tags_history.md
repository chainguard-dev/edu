---
title: "jenkins Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jenkins Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-07 00:46:50
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/jenkins/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/jenkins/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/jenkins/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/jenkins/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 5th     | `sha256:a54204e1c076a5350d68360665c3cb52115fc7645be568a795d5467b1270cad3` |
|  `latest`     | June 5th     | `sha256:7ada09c259c9ab5dd182354ab95854b26a0800d861e10ae0943e282a5e680621` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                           | Last Changed | Digest                                                                    |
|-----------------------------------|--------------|---------------------------------------------------------------------------|
|  `2` `latest` `2.461`             | June 5th     | `sha256:a8df74748d3ff19e4ecc25b25daaa1c826266eb0435eb768576dc8aaaddf31ec` |
|  `latest-dev` `2.461-dev` `2-dev` | June 5th     | `sha256:b9fb72ade4ff08f1fb8e4fb8a3f06bd354ba5de46d4e5a4e7ce251e91986ee7a` |
|  `2.460-dev`                      | June 4th     | `sha256:fc1f88b3cc5a1d62c344745ffffc3f042cfac76261be70ed698859fee0282d40` |
|  `2.460`                          | June 4th     | `sha256:3726fb8f8057d554174e0845da21bf1ed01915df7c3a569cb2733c9927d7b1d2` |

