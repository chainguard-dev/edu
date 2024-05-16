---
title: "octo-sts Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the octo-sts Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-16 00:37:58
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/octo-sts/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/octo-sts/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/octo-sts/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/octo-sts/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 15th     | `sha256:14b6bd3b7bff0b14c8a15853f83a2969d7f83dc4bef4ca16f5136b92385ec0d1` |
|  `latest`     | May 13th     | `sha256:33b0eac71e3a7828da6828a68029a01d30096429b410cc24abe8b79ed0f843cc` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `0` `0.1.0` `0.1`                 | May 15th     | `sha256:d211dadfc2981092d626b8000b673630a2ade55deb357872155c963572d57394` |
|  `0-dev` `latest-dev` `0.1-dev` `0.1.0-dev` | May 15th     | `sha256:1d902c32da48648ba91f0c5b8ff888322a2e0997daf80e55c33d718162c78239` |

