---
title: "cfssl Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the cfssl Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-06 00:47:02
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
|  `latest`     | March 5th    | `sha256:57e7a5454f48f76915d1c399968ffd38070cf0059535c96631ca08fe2887319b` |
|  `latest-dev` | March 5th    | `sha256:07975abaa3817e793b500d22685fb3f36b7f6843e2d6379d8cf3089b22aaa1f6` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `1.6.5` `1` `1.6`                 | March 5th    | `sha256:146434f01b0a6be07f3d93eb2c7876b7c0df8b879694f2b0474cbad139bd9823` |
|  `1.6-dev` `latest-dev` `1.6.5-dev` `1-dev` | March 5th    | `sha256:59267e9c6978b5fb0ffc6e07a5b1581adcf2df22b5c21f7d34930470d0525745` |
|  `1.6.4-dev`                                | March 2nd    | `sha256:6bb1365ee7004869afbf8c48665e97c7106fcf69cafa58a6c65b2bcfc1523d66` |
|  `1.6.4`                                    | March 1st    | `sha256:0f22b930283055b703dae5fa37506924b8b083ee11e6012964f184072692f9c5` |

