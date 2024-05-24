---
title: "consul Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the consul Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-24 00:45:45
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/consul/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/consul/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/consul/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/consul/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | May 23rd     | `sha256:961ad1bc3c331a753bd18c272f9e1504552c48ce690896d946b0c9a38f052ce1` |
|  `latest-dev` | May 23rd     | `sha256:595c191db9a0fc96e07428068c19f04303715aa9dce04185686039333f4d3aae` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.15` `1.15.11`                             | May 23rd     | `sha256:21289808d08838ee7617295c4953d0b32fa5322415e6972b1ff7add3e73606c8` |
|  `1.17` `latest` `1.17.4` `1`                 | May 23rd     | `sha256:bfa2bbe950072be43122b38a9a45875bb28c3b0bfdec8604c0fa2858f7ab5532` |
|  `1.17.4-dev` `1.17-dev` `1-dev` `latest-dev` | May 23rd     | `sha256:fbdab325676460d0f56582ab1a49b913144e1e00cf2163e19fd8a70b26525d20` |
|  `1.16` `1.16.7`                              | May 23rd     | `sha256:eecac0e1eeee7204195ca79a8d8216b8e46102a026e94d4ec9fa738e3a37974f` |
|  `1.15.11-dev` `1.15-dev`                     | May 23rd     | `sha256:a1b4911521ce81b6321023ff18c08eff720c0d2d827f50a0265c010c6a6b6100` |
|  `1.16.7-dev` `1.16-dev`                      | May 23rd     | `sha256:394b7aa46c3caacea212430c4f7512b96b5acd64b0d043d34549962b72a68377` |

