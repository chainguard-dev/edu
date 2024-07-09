---
title: "octo-sts Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the octo-sts Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-09 00:39:12
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
|  `latest-dev` | July 8th     | `sha256:e5357a134613cbe6e507102dba87aa894c8325863b93cfd8b6683d3ba97dca81` |
|  `latest`     | July 8th     | `sha256:cd27a815ff79e0d2793feb6555c51782631bac831b11bcac1bb95113afbf1fc6` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `0.2` `0.2.0` `0`                 | July 8th     | `sha256:fb2b6f94afc5e77069398ef59e38d95dc39ffd3803548ec50a6a6c896d34648b` |
|  `0.2-dev` `0-dev` `0.2.0-dev` `latest-dev` | July 8th     | `sha256:e4a2c47da942c466a087247a4ad12b68a5ee70ffd73a6167af73a61a558cc0e0` |

