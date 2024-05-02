---
title: "cadvisor Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the cadvisor Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-02 00:37:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/cadvisor/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/cadvisor/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/cadvisor/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/cadvisor/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | May 1st      | `sha256:2312c69e8536a43a7c76ec1e6223613b1288fe921090763d6dad9c1aa6ba5f4a` |
|  `latest-dev` | May 1st      | `sha256:6fc8f5a5ed4598cf123b6303a77fa80172eb4187b8e884e90b0a62e16d0a57ae` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0-dev` `0.49-dev` `latest-dev` `0.49.1-dev` | May 1st      | `sha256:4def7fd4d5f92fad79633b2226081a939a2d8c2560aaebdfdf63af4cb2347fea` |
|  `0.49` `0` `latest` `0.49.1`                 | May 1st      | `sha256:c5207b514cb16fb6188668dda397bf37f93b68215dfe37d6fd8908a85197abce` |

