---
title: "step-cli Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the step-cli Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-15 00:39:35
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/step-cli/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/step-cli/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/step-cli/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/step-cli/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 14th     | `sha256:cb9d1a5d2223926bb8b01ca916f71716d33137c62be7664c93d99a37c8d7f255` |
|  `latest`     | May 10th     | `sha256:d89b60fa2cdf21b6dbda531870719183940350ad9ef84830800d8d3c7bd8c8c1` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0.26-dev` `latest-dev` `0.26.1-dev` `0-dev` | May 14th     | `sha256:c339bd2077b2b5c8ea32d8f5ad3f88c9fcf43229ca690376d2fd5302e022efda` |
|  `0` `0.26` `0.26.1` `latest`                 | May 10th     | `sha256:d3b7c03a390ccb5b9022612fe2f1cd39240a15607942e1f1426010d32fa837f2` |
|  `0.26.0-dev`                                 | April 21st   | `sha256:c58861a16bbf5286470f8608892591da684289394dbebd736841a0cbc9f1dcfa` |
|  `0.26.0`                                     | April 21st   | `sha256:5f8d80635bbc72c9eae0d69c4cbdd7b0d515cad0980eaa77c466136cc70434d8` |

