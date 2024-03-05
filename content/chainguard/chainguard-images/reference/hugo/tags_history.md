---
title: "hugo Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the hugo Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-05 17:06:05
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/hugo/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/hugo/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/hugo/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/hugo/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | March 1st    | `sha256:8e7b48e9cb2a9b913760322c1fae302490c6bdb2a52b6fb92cd70605b7bf2aa9` |
|  `latest`     | March 1st    | `sha256:7d09cc46c1fd1fa9f1b72d1bf909eaec17f6767e106f5fc5072d3a85a7877561` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                         | Last Changed  | Digest                                                                    |
|-------------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `0.123.7-dev` `0-dev` `latest-dev` `0.123-dev` | March 2nd     | `sha256:c024426674794c1ebf8d51765b071f5d40d75123673619c27be82d06705dc7de` |
|  `0.123.7` `0` `0.123` `latest`                 | March 1st     | `sha256:0502d6d9515cdf4365c678e840321f1282ae2e29a27a9ffd8de9d0ea40cd4f9d` |
|  `0.123.6-dev`                                  | March 1st     | `sha256:ba09bbd048aaa8fe9fde7d7bf83d71c31d9b7d8a34c2f02532a0fe12319cbe01` |
|  `0.123.6`                                      | February 29th | `sha256:16689601a29ec6edc8b435d0099cdb8095fa774342f50f5d0dc7a4ed9000f0d7` |

