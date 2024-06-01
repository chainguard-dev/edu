---
title: "az Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the az Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-01 00:50:07
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/az/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/az/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/az/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/az/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 31st     | `sha256:2042297e99143967aa24b3bf7a6e941858c1fbe6e7d166ca92b451f52c31b4f7` |
|  `latest`     | May 30th     | `sha256:74068e96658aeec9114a349c2870ab0620cbf2990c6ccc9f9e48b2b91c07db97` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                       | Last Changed | Digest                                                                    |
|-------------------------------|--------------|---------------------------------------------------------------------------|
|  `2.61.0-dev` `latest-dev`    | June 1st     | `sha256:d7b3b65e1dd79a25c9fee0048b0bacef21cf3d1bccd73508f2c7d46b60d0754a` |
|  `2` `2.61` `latest` `2.61.0` | May 30th     | `sha256:66367d56ae9510a31d57ca2a87c9632c226397a91392f562b9d2d0e7ed435607` |
|  `2-dev` `2.61-dev`           | May 30th     | `sha256:5b91f81671fe99c216854e9b0fd80daaf5f13da6eb827217b941e6e9a88b903a` |
|  `2.60.0-dev` `2.60-dev`      | May 19th     | `sha256:ebf4af5e8c9618e08a9d8d17cfcc446250833fd4b0fb8593179302879a9fd2b9` |
|  `2.60.0` `2.60`              | May 17th     | `sha256:15ef99e92cea2e3acfa4c18d8cfea77d74684109d3c2a41ef1899924a800ff2a` |

