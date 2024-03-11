---
title: "jenkins Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jenkins Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-11 00:52:51
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
|  `latest`     | March 8th    | `sha256:e688a3cae9b2d9f18e244957a76b8df3f2afdadeb3688006f7465fc662aa100e` |
|  `latest-dev` | March 8th    | `sha256:04587df087bb1d3698dcd7e358210eaeea2f73e262351cafa6fc980fc59efd86` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                           | Last Changed  | Digest                                                                    |
|-----------------------------------|---------------|---------------------------------------------------------------------------|
|  `2.448-dev` `2-dev` `latest-dev` | March 10th    | `sha256:55c2d7328908f04344c5976af3cda9d0f4ecb7cfc73199f4aad760955a1fa0fc` |
|  `2.448` `2` `latest`             | March 8th     | `sha256:db062dce11c12f72f1a7826264054a7c68461b9092c1193ab644bd282913fd6e` |
|  `2.447-dev`                      | March 2nd     | `sha256:9c1b659d74e346c9c17d2b9f8704e56e000126c93db80484d5b66567b8095c33` |
|  `2.447`                          | March 1st     | `sha256:615f25734272a8e39ebccdd8fd2e0746910e663caf400efee2bf2e6dd784a600` |
|  `2.446-dev`                      | February 26th | `sha256:fcfd00741ca3b778ca32691658c202278f84a24235902ab8d3260949a81ddcb9` |
|  `2.446`                          | February 26th | `sha256:d51373f342abbaac8803644e9d984fbd09c77d16d63ef036a5601c8d6a508f82` |
|  `2.445-dev`                      | February 19th | `sha256:2133ba18450ad72b92ee801f0b69e30ea867c37c20d462c041d6bd9982bd9208` |
|  `2.445`                          | February 19th | `sha256:205df5a552c6c8e93ae2bc77cb0ab0ff74fc2f01a067535084592d567e0b6d6f` |
|  `2.444-dev`                      | February 13th | `sha256:63350c2466a881e40fb4b15d17c928f0dc35f8b9304bac75a1bef49749af7c88` |

