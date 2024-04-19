---
title: "hugo Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the hugo Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-19 00:39:27
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
|  `latest`     | April 18th   | `sha256:6f4c78e9c93a951adee59d23dbe0a996a3a3d2b37caf7562c601b2b0c1de10b3` |
|  `latest-dev` | April 18th   | `sha256:61188c22eabda3a9cc8b741ee23cf4e9b496b576ef152b15d6bfa63fad96bf30` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                         | Last Changed | Digest                                                                    |
|-------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0` `0.125.1` `0.125` `latest`                 | April 18th   | `sha256:cabdde6428abda55cc0c7debfe2f85883e05a9d797a4181c071d658ced8fcfac` |
|  `latest-dev` `0.125.1-dev` `0-dev` `0.125-dev` | April 18th   | `sha256:cff7178915196cbc3e12d046aeddb8e4657e16d975e9684f2b952eeafbc6b811` |
|  `0.125.0-dev`                                  | April 16th   | `sha256:aba3a70dcab303cf4eae2bbad97635cd96940c105e4cace7577c98064100ea2b` |
|  `0.125.0`                                      | April 16th   | `sha256:071f477e01798ecafe478fe523ddad99dcb2ac98f0876bbe89968dcbff4924e9` |
|  `0.124.1-dev` `0.124-dev`                      | April 11th   | `sha256:ea065264a10f92736dd66e7cf1c175e23f2cc1a0629a587f01cb13bc37a8415d` |
|  `0.124` `0.124.1`                              | April 4th    | `sha256:2d37286522291d59fbd0e1673d576f01d6f8d765b6a07ee7d7e186e8c87012ce` |

