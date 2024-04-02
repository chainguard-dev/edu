---
title: "jenkins Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jenkins Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-02 00:36:12
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
|  `latest-dev` | April 1st    | `sha256:b05a9fd7d628f86b954a0235a3311595e972f483b3f32f2f0b1e4f363542b07d` |
|  `latest`     | March 28th   | `sha256:4ed3ab6fa8539144806fab19a2783d7de5414f7c2c9f4cf936ceb7f3bf8b5092` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                           | Last Changed | Digest                                                                    |
|-----------------------------------|--------------|---------------------------------------------------------------------------|
|  `2.451-dev` `2-dev` `latest-dev` | April 1st    | `sha256:39ccd8c0d6f83a841cc6889c124ca7f73d971cca8235e7314ebe1d0d44228d23` |
|  `latest` `2.451` `2`             | March 28th   | `sha256:6c0ebc567036320aa3956c042e38487f42f5678989a2e33570e8342a2c7dc2d4` |
|  `2.450-dev`                      | March 20th   | `sha256:ffa9168061690d1a11cd602234d62ca4de2ccfc5f7223d69e80af19a70886d0f` |
|  `2.450`                          | March 20th   | `sha256:90c4ac02f6893758fedbee5072779f8f48a5d19e09ea585608940a4506025b77` |
|  `2.449-dev`                      | March 18th   | `sha256:292423b9874e77b2dc9c5366790031fe61fd710c3e674706c9441915fe982db8` |
|  `2.449`                          | March 18th   | `sha256:21a92280f0a73be522e892d8e8e766f250b7787543cb03d256d35b80a4853478` |
|  `2.448-dev`                      | March 12th   | `sha256:ddd808b7a77fdd50f568106f3ae2c479fb58b6e18bdce68391f3097ed538c4e4` |
|  `2.448`                          | March 11th   | `sha256:6f30bf9ced7433db4e6e0d113ec44de4181aa94f710a3808a94bdcc2619699fb` |

