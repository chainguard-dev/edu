---
title: "conda Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the conda Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-03 00:49:16
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/conda/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/conda/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/conda/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/conda/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 1st    | `sha256:6c2521135ae31e23d49c4fb77ccf38f216fa2345a58dc8ff3e8bb8b5f7308bd6` |
|  `latest`     | April 1st    | `sha256:b6ce7965568022eb493e33b892af3e6de50fb9f2306b94192a8d054c6b3192c1` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `24.3-dev` `24-dev` `24.3.0-dev` | April 2nd    | `sha256:1ce5ec95cbfbf41f149f3deba7ef43ebb8a5720aaca6d96217d4fbab33446975` |
|  `latest` `24.3` `24.3.0` `24`                 | April 1st    | `sha256:71ce9a840883d3886b26ec67e400957547bee36165bf5449d8791558a245c350` |
|  `24.1.2` `24.1`                               | March 18th   | `sha256:c4ded39d1296d285dd0292b96eda8becb5fec3ed63c071709d7c8de448e4a59d` |
|  `24.1-dev` `24.1.2-dev`                       | March 18th   | `sha256:170c94f39165c6e06538e2a326bf9f888c06d00f95747e3662d28bf51f9ceec0` |

