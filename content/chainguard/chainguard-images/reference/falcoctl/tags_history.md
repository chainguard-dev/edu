---
title: "falcoctl Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the falcoctl Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-16 00:37:58
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/falcoctl/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/falcoctl/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/falcoctl/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/falcoctl/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 15th     | `sha256:a8638c3fe00a0be3ec6b509c2b0725dd57b0e0719e39bc2b6a4041e3da34f53b` |
|  `latest`     | May 15th     | `sha256:ee4865bbfec7f38916fb3b5b3c4cab1d3a3a4791abc0024a124c9137a7072b07` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0.7.3` `0.7` `latest` `0`                 | May 15th     | `sha256:3c012bc9f4252bee0539c2442b648db84c315bd394dbd850eb91fcf4e962eefd` |
|  `latest-dev` `0-dev` `0.7.3-dev` `0.7-dev` | May 15th     | `sha256:8e4131f41f6d33a7c4bf47512086571889c699757842047c357bd8ca8b1b3ade` |

