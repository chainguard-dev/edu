---
title: "node-lts Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the node-lts Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-19 00:39:27
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/node-lts/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/node-lts/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/node-lts/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/node-lts/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 11th   | `sha256:9fcfa8026f6df20579bd23a215cfbc990a09c02a098a62cbc35c2cc1068abee5` |
|  `latest`     | April 11th   | `sha256:acc28399a7605bebe75d5a74b5391e1e5391ac206dd2eb034ab2208a84a5a62d` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                          | Last Changed | Digest                                                                    |
|--------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `20.12-dev` `latest-dev` `20-dev` `20.12.2-dev` | April 11th   | `sha256:100ece7fe2c9939432ab408573111ea238647b2e358f6fedbb7f4761ecf1fb4e` |
|  `latest` `20.12` `20.12.2` `20`                 | April 11th   | `sha256:e4b0eafd4b9e9c4039ce907814f5760e5ba844702af9f1e7de255e1d83a0a3d3` |
|  `20.12.1-dev`                                   | April 9th    | `sha256:d289a7c7a304ddbed4b56ad9d455d5927e43fdb587c451e75bd652ee876feed2` |
|  `20.12.1`                                       | April 9th    | `sha256:7d95ea2daa4623b270d640e2a7e9f7aeb353993313b277bd44f29a67bce1655f` |
|  `20.12.0-dev`                                   | April 3rd    | `sha256:83afbbb59e0c66fe10e503df0da53673df4724b013dcf10bdc996d6898a8608c` |
|  `20.12.0`                                       | April 3rd    | `sha256:0f9217ed827198cbb8c09503e28fb93acbe24a2f1af31c45e5cdcb31fe0f5347` |

