---
title: "jenkins Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jenkins Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-12 00:55:01
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
|  `latest-dev` | March 11th   | `sha256:f878f5b89a1c8434ed2e82c824fcaa193dd7fd231a69a4920dedf4d5acbf2a5f` |
|  `latest`     | March 11th   | `sha256:e16b8f267d1c5d10e3f392eff5c69643476d81055bfa0d5c97ccb8df1bffb992` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                           | Last Changed  | Digest                                                                    |
|-----------------------------------|---------------|---------------------------------------------------------------------------|
|  `2-dev` `latest-dev` `2.448-dev` | March 11th    | `sha256:a51d95c2582b77a2ef5009d0d7245361d16a972047401d6aefeb0d0f43a660b4` |
|  `2` `latest` `2.448`             | March 11th    | `sha256:6f30bf9ced7433db4e6e0d113ec44de4181aa94f710a3808a94bdcc2619699fb` |
|  `2.447-dev`                      | March 2nd     | `sha256:9c1b659d74e346c9c17d2b9f8704e56e000126c93db80484d5b66567b8095c33` |
|  `2.447`                          | March 1st     | `sha256:615f25734272a8e39ebccdd8fd2e0746910e663caf400efee2bf2e6dd784a600` |
|  `2.446-dev`                      | February 26th | `sha256:fcfd00741ca3b778ca32691658c202278f84a24235902ab8d3260949a81ddcb9` |
|  `2.446`                          | February 26th | `sha256:d51373f342abbaac8803644e9d984fbd09c77d16d63ef036a5601c8d6a508f82` |
|  `2.445-dev`                      | February 19th | `sha256:2133ba18450ad72b92ee801f0b69e30ea867c37c20d462c041d6bd9982bd9208` |
|  `2.445`                          | February 19th | `sha256:205df5a552c6c8e93ae2bc77cb0ab0ff74fc2f01a067535084592d567e0b6d6f` |
|  `2.444-dev`                      | February 13th | `sha256:63350c2466a881e40fb4b15d17c928f0dc35f8b9304bac75a1bef49749af7c88` |

