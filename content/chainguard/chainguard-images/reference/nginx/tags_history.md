---
title: "nginx Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the nginx Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-21 00:38:36
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/nginx/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/nginx/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/nginx/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/nginx/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 20th     | `sha256:a43c733aa66a216836c5aba42dc42a94e0b1c89985292ae0e946a02abfaea9fc` |
|  `latest`     | May 17th     | `sha256:76a280e5e5da0e07ada2f12a25c27fa7a188bed0fd2f8f991069e043d2c40b48` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.26-dev` `1.26.0-dev`                      | May 19th     | `sha256:11620bbc0515dbf30ea87517f30b7892c9a900a96953f1576876560cbe4cc6c3` |
|  `1-dev` `1.25.5-dev` `1.25-dev` `latest-dev` | May 19th     | `sha256:42194e8d34b57e1394d880c4682d00b4bb4ea384c889a2bb1917e47da6269d93` |
|  `1.25` `mainline` `1.25.5` `latest` `1`      | May 17th     | `sha256:ce9839a185dd6af81046bbd6be13ce246e10b3552922575e97f38645467e9de3` |
|  `stable` `1.26` `1.26.0`                     | May 17th     | `sha256:d0a9164f59e2d64b3542fb335900c7fab18133a95dab6a32be25671e8dff5baa` |
|  `1.24` `1.24.0`                              | May 2nd      | `sha256:f9cd4ff7d76ff0ce095f42fea4c9b5820fb99dcb49df0f0e302d87883fab7967` |
|  `1.24-dev` `1.24.0-dev`                      | May 2nd      | `sha256:15ebd2e4311a62e1d77e55ff87e6f494c8d3a84ef8e861fdf6a7a85a92b3b4f3` |

