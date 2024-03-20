---
title: "jenkins Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jenkins Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-20 01:10:09
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
|  `latest-dev` | March 18th   | `sha256:331d374537af3283efbef2c711646f9fd59f4f75f0da076f26fb7d7aa82838b8` |
|  `latest`     | March 18th   | `sha256:6a2281ccd8d40e6185019f4095055ef9178d1240341a4f018f665aecc13cc3d8` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                           | Last Changed  | Digest                                                                    |
|-----------------------------------|---------------|---------------------------------------------------------------------------|
|  `2` `latest` `2.449`             | March 18th    | `sha256:21a92280f0a73be522e892d8e8e766f250b7787543cb03d256d35b80a4853478` |
|  `latest-dev` `2.449-dev` `2-dev` | March 18th    | `sha256:292423b9874e77b2dc9c5366790031fe61fd710c3e674706c9441915fe982db8` |
|  `2.448-dev`                      | March 12th    | `sha256:ddd808b7a77fdd50f568106f3ae2c479fb58b6e18bdce68391f3097ed538c4e4` |
|  `2.448`                          | March 11th    | `sha256:6f30bf9ced7433db4e6e0d113ec44de4181aa94f710a3808a94bdcc2619699fb` |
|  `2.447-dev`                      | March 2nd     | `sha256:9c1b659d74e346c9c17d2b9f8704e56e000126c93db80484d5b66567b8095c33` |
|  `2.447`                          | March 1st     | `sha256:615f25734272a8e39ebccdd8fd2e0746910e663caf400efee2bf2e6dd784a600` |
|  `2.446-dev`                      | February 26th | `sha256:fcfd00741ca3b778ca32691658c202278f84a24235902ab8d3260949a81ddcb9` |
|  `2.446`                          | February 26th | `sha256:d51373f342abbaac8803644e9d984fbd09c77d16d63ef036a5601c8d6a508f82` |

