---
title: "argocd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the argocd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-05 00:42:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/argocd/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/argocd/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/argocd/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/argocd/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | July 3rd     | `sha256:1b756dd3cb39399eb0b67422e17d72b0f31f30d9af98cc9cde899da2005e0130` |
|  `latest`     | July 3rd     | `sha256:b3bae39afaad29c0341b3d5f573c06e79e6c4398b51dd02af1688d8d1dc2e651` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2.9-dev` `2.9.18-dev`                       | July 3rd     | `sha256:edeab89f1ef341d3a2fbce850c0b81ad357dd0fc6213a2674d729135f6d13d72` |
|  `2.11-dev` `2.11.4-dev` `2-dev` `latest-dev` | July 3rd     | `sha256:83c0ac81efe0ee398998c8fc7c1bfed5dfc5e7cd70a3a447b61c510db05a0d06` |
|  `2.8.18-dev` `2.8-dev`                       | July 3rd     | `sha256:3c29973bd953813b8111442882fe018e036ddf97c673eca85b95f414c39b699a` |
|  `2.10-dev` `2.10.13-dev`                     | July 3rd     | `sha256:b17433585cf7aa6ecc17be5547868349b067d2226a222f5d6213c9e9c94674fa` |
|  `2.10` `2.10.13`                             | July 3rd     | `sha256:93e69162868931a90237beab7c6a6523cb1f3f9ff50d5cf4d3c3a7885838c627` |
|  `2.9` `2.9.18`                               | July 3rd     | `sha256:6a05da638a2d7b1be0975b329d0c9d0edbb780d860b258ba9081085dea49ee74` |
|  `latest` `2.11` `2.11.4` `2`                 | July 3rd     | `sha256:39013c18012536e2454342645b9655c562aeb1ec1d8ab5053d23494a158e8b12` |
|  `2.11.3-dev`                                 | June 28th    | `sha256:b77312d2805a7790ad5131303ee2cc93cbeea594f289b3ef694e77d2908cdeb2` |
|  `2.9.17-dev`                                 | June 28th    | `sha256:48d89fdacd021509a34fe58036513b36227b355e3fb8f5d7c45d9602e3183a5c` |
|  `2.10.12-dev`                                | June 28th    | `sha256:1da1e47c1d2ebafa94b21d6f63fb153403bb2022e4835365e8cbf83ad92e0211` |

