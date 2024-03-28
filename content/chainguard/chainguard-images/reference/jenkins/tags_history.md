---
title: "jenkins Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jenkins Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-28 00:50:32
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
|  `latest`     | March 26th   | `sha256:5e912f3a13b85b9b1dbeb59221ec76ff10d80651639243a537d40ec46a125fec` |
|  `latest-dev` | March 26th   | `sha256:47e7e26af9c6c3a39826d7490d5a55e4e9762b2a8018c36b90c9d505bdcc7120` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                           | Last Changed | Digest                                                                    |
|-----------------------------------|--------------|---------------------------------------------------------------------------|
|  `2-dev` `latest-dev` `2.451-dev` | March 27th   | `sha256:bae777843076f9a927e4dd783e2a840fab0d1a61ec47308bc91bbc04c095890f` |
|  `2` `latest` `2.451`             | March 27th   | `sha256:931467437877b31da532b1e9f1dfce0eff3ddc308b01eaa16a74692adb955e28` |
|  `2.450-dev`                      | March 20th   | `sha256:ffa9168061690d1a11cd602234d62ca4de2ccfc5f7223d69e80af19a70886d0f` |
|  `2.450`                          | March 20th   | `sha256:90c4ac02f6893758fedbee5072779f8f48a5d19e09ea585608940a4506025b77` |
|  `2.449-dev`                      | March 18th   | `sha256:292423b9874e77b2dc9c5366790031fe61fd710c3e674706c9441915fe982db8` |
|  `2.449`                          | March 18th   | `sha256:21a92280f0a73be522e892d8e8e766f250b7787543cb03d256d35b80a4853478` |
|  `2.448-dev`                      | March 12th   | `sha256:ddd808b7a77fdd50f568106f3ae2c479fb58b6e18bdce68391f3097ed538c4e4` |
|  `2.448`                          | March 11th   | `sha256:6f30bf9ced7433db4e6e0d113ec44de4181aa94f710a3808a94bdcc2619699fb` |
|  `2.447-dev`                      | March 2nd    | `sha256:9c1b659d74e346c9c17d2b9f8704e56e000126c93db80484d5b66567b8095c33` |
|  `2.447`                          | March 1st    | `sha256:615f25734272a8e39ebccdd8fd2e0746910e663caf400efee2bf2e6dd784a600` |

