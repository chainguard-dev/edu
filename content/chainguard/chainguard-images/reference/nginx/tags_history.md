---
title: "nginx Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the nginx Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-03 00:45:55
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
|  `latest`     | May 2nd      | `sha256:2c6b352134c1083d81a4b17d9703f6229cea5ca57ad4bd2a50c46f09fb3653a8` |
|  `latest-dev` | May 2nd      | `sha256:f49292877c1644e7d0932d95557e3b0890cbfcb20a28bbfac7e2c6bbad825437` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `mainline` `1.25` `1.25.5` `latest` `1`      | May 2nd      | `sha256:2fee9e353ae68f210aaee02585ac04beef32cc71b02d0614700b5715c9aa153b` |
|  `1.24` `stable` `1.24.0`                     | May 2nd      | `sha256:f9cd4ff7d76ff0ce095f42fea4c9b5820fb99dcb49df0f0e302d87883fab7967` |
|  `1.25-dev` `1-dev` `latest-dev` `1.25.5-dev` | May 2nd      | `sha256:b401a494e33718b612a0beaf7168efa4bc3900e84a3ba543334d4024b2057023` |
|  `1.24-dev` `1.24.0-dev`                      | May 2nd      | `sha256:15ebd2e4311a62e1d77e55ff87e6f494c8d3a84ef8e861fdf6a7a85a92b3b4f3` |
|  `1.25.4`                                     | April 16th   | `sha256:677b3c605e597b50e973f0a8bc265756ae86bb8b294105defc9e97e02654ef57` |
|  `1.25.4-dev`                                 | April 16th   | `sha256:01447112852762699d88c95bc0e4c3f83f9b7a0ec7e416df9ab7e8fcbda9c5dd` |

