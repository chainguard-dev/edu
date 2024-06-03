---
title: "ingress-nginx-controller Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the ingress-nginx-controller Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-03 00:46:08
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
|  `latest-dev` | June 1st     | `sha256:77f731b38da84fcfd5e8343b123f2fe462e41b2703ffb53029fc3b9d2e083973` |
|  `latest`     | May 30th     | `sha256:271494380b5cb14cb1c95a856aa9137ba28581551dfebce68a8469bbb2185d6e` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.9-dev` `1.9.6-dev`                        | June 1st     | `sha256:6aa082d1cbc65b0314ab7e7862705520923b196180d27095d219d0e47a6835f9` |
|  `1.10.1-dev` `1-dev` `1.10-dev` `latest-dev` | June 1st     | `sha256:0eddf0cb22666d310e7993c156dd33c5a697db18596f012f6eabcd1bf9b91a11` |
|  `1.9.6` `1.9`                                | May 30th     | `sha256:892ad6bb14e57c87a8627d5c051c73d7fde0c7ae11f923548ce6ebf1dddc5af9` |
|  `1` `latest` `1.10` `1.10.1`                 | May 30th     | `sha256:bf2ea4c680c523dc29961d79c48232b912b5036d79718f890d4f68c6712677de` |

