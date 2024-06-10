---
title: "jenkins Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jenkins Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-10 00:50:47
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
|  `latest-dev` | June 9th     | `sha256:6bf766f0113c5c5812cd84dc9ff68a646a8f3cbba3d645c09021073502fba24d` |
|  `latest`     | June 9th     | `sha256:ef15f1763f8c53d6abe5a54495a9b17a5399b05e291d8d4575a8c11417f3e4bb` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                           | Last Changed | Digest                                                                    |
|-----------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `2.461` `2`             | June 8th     | `sha256:9d848881bebca774959b9a686819ae141e28b4b9ad9ad6d03835e5c3c02b79fd` |
|  `2.461-dev` `2-dev` `latest-dev` | June 8th     | `sha256:066df934f91ace1f3153c9f899911534686b641759e6e550f64d77207b052229` |
|  `2.460-dev`                      | June 4th     | `sha256:fc1f88b3cc5a1d62c344745ffffc3f042cfac76261be70ed698859fee0282d40` |
|  `2.460`                          | June 4th     | `sha256:3726fb8f8057d554174e0845da21bf1ed01915df7c3a569cb2733c9927d7b1d2` |

