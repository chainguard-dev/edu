---
title: "cfssl Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the cfssl Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-29 00:47:42
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/cfssl/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/cfssl/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/cfssl/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/cfssl/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | March 28th   | `sha256:248d72930e18828840b3fbf1592023c0ba34f8b527549df0336c702c9a36990c` |
|  `latest-dev` | March 28th   | `sha256:bb286bfbb53cfba8d36b2b37d26b2178deae53f3906c38175dc5365e6d483db7` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.6.5` `latest` `1` `1.6`                 | March 28th   | `sha256:9578210ac920e8b06c2e6ba45c56f2e4ddbf3945fae861ee9833aa9ba489b8da` |
|  `latest-dev` `1-dev` `1.6.5-dev` `1.6-dev` | March 28th   | `sha256:0bdad69e165aef5bab1d3fb690b6b0b912f0e4d9428db342d18a9a059f7b719b` |
|  `1.6.4-dev`                                | March 2nd    | `sha256:6bb1365ee7004869afbf8c48665e97c7106fcf69cafa58a6c65b2bcfc1523d66` |
|  `1.6.4`                                    | March 1st    | `sha256:0f22b930283055b703dae5fa37506924b8b083ee11e6012964f184072692f9c5` |

