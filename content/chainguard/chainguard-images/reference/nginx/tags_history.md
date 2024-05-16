---
title: "nginx Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the nginx Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-16 00:37:58
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
|  `latest-dev` | May 15th     | `sha256:18f23cd307085f111d51eeb5258d18eef2057a7c238c7711e1e225d69332d4b5` |
|  `latest`     | May 15th     | `sha256:3eb5df4340ae1781b7e5b1895766db80d12f15f6632c333c86047d1330994958` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.26-dev` `1.26.0-dev`                      | May 15th     | `sha256:9fc4008f2dd908b8287442135c4b306cf2dd9ef0b1fc4e19f98fd91d14b56b7b` |
|  `1.25` `latest` `1.25.5` `1` `mainline`      | May 15th     | `sha256:fb1cff25d1d4c6933faf0569c32da396cd7e875040ca5a745c9c9a44f0188078` |
|  `1.26` `1.26.0` `stable`                     | May 15th     | `sha256:a2e8a338c8d7a9ee5e9f8aa524f3f76d4c953cfc969a80cc3212f916b8d64c4c` |
|  `1.25.5-dev` `1.25-dev` `1-dev` `latest-dev` | May 15th     | `sha256:58d53b16cb1d5900337db84295d4925a7785e7052da61e345b21cb042ba96c50` |
|  `1.24` `1.24.0`                              | May 2nd      | `sha256:f9cd4ff7d76ff0ce095f42fea4c9b5820fb99dcb49df0f0e302d87883fab7967` |
|  `1.24-dev` `1.24.0-dev`                      | May 2nd      | `sha256:15ebd2e4311a62e1d77e55ff87e6f494c8d3a84ef8e861fdf6a7a85a92b3b4f3` |
|  `1.25.4`                                     | April 16th   | `sha256:677b3c605e597b50e973f0a8bc265756ae86bb8b294105defc9e97e02654ef57` |
|  `1.25.4-dev`                                 | April 16th   | `sha256:01447112852762699d88c95bc0e4c3f83f9b7a0ec7e416df9ab7e8fcbda9c5dd` |

