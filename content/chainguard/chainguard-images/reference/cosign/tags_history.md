---
title: "cosign Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the cosign Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-11 12:38:02
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/cosign/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/cosign/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/cosign/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/cosign/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 9th    | `sha256:e61b49f0e524581cf6b17a669a1829349812d412c557a16b8be10ee1ada1b065` |
|  `latest`     | April 4th    | `sha256:7539eedf0114a56de6e041253207b2ddb70b77402c31c5826e8177688a8e2efc` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2.2-dev` `2.2.4-dev` `latest-dev` `2-dev` | April 11th   | `sha256:21d2609444ac92084534212706526cdb3800e7bf7eb5e5cbb9e8cf90f7773223` |
|  `latest` `2.2` `2` `2.2.4`                 | April 11th   | `sha256:ffb342633fb870fffe8306dbd21b4569c41fe66c9cd16fc1eed2110507ef096c` |
|  `2.2.3-dev`                                | April 9th    | `sha256:1da0d2dcea301b70e54b4962bb344ff54e275a8e6024e083c04b1cbd99367c07` |
|  `2.2.3`                                    | April 3rd    | `sha256:1e547bf52787126db0e5a5e73893dd24e2b98d97eabf9816f7545670bbdaac40` |

