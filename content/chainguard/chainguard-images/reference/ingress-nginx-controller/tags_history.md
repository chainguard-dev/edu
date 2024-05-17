---
title: "ingress-nginx-controller Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the ingress-nginx-controller Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-17 00:44:46
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/ingress-nginx-controller/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/ingress-nginx-controller/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/ingress-nginx-controller/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/ingress-nginx-controller/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | May 16th     | `sha256:e9cff6c5026a32b6f845b4e58e7c35518c8d32bb30b3e8b223f612f53a79b2af` |
|  `latest-dev` | May 16th     | `sha256:6058a46d8202129132ce9a7f427b1627545b60aeda4e5a2da003c39bea6a38e2` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.10.1` `1.10` `1` `latest`                 | May 16th     | `sha256:1842cb4b2e7f6785003dcb6b227521b06f97e38b3d4d595c8b701232f0585095` |
|  `1.9` `1.9.6`                                | May 16th     | `sha256:21b4ebc6628b216dc6d8137f2884c15b49694128e9e093c615d015bffde5c161` |
|  `1.9-dev` `1.9.6-dev`                        | May 16th     | `sha256:003be2fe1142bccafaba1fd59c3480f95d5872d95b1fb75bc93e9df52be0baf2` |
|  `latest-dev` `1-dev` `1.10-dev` `1.10.1-dev` | May 16th     | `sha256:6500c2d7bc68d58504cb98d4c71268ee7d33403ce7d8c71763712705638e80ae` |
|  `1.10.0-dev`                                 | April 20th   | `sha256:27f7a69e168ba4b48506041601641dafb87118758ef4b408eb01c0e6867d5553` |
|  `1.10.0`                                     | April 20th   | `sha256:2a323e07711fb6b5f9f201d89610035cebaf5be7ef2466d92efc8a8031dcfb71` |

