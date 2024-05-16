---
title: "nemo Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the nemo Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-16 00:37:58
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/nemo/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/nemo/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/nemo/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/nemo/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 15th     | `sha256:314f0a821a6ac10b28bf336957f64999f5d41c79a1cad59886fa6911c53ae19d` |
|  `latest`     | May 15th     | `sha256:234c471d64d12972fe990d76f372c1c5a7cd5d28f89c50ba3947907bf3146e68` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.23` `1` `1.23.0` `latest`                 | May 15th     | `sha256:cf3b59aa2046511556056c066983b646b5a1d68ef897dc1eace91cca24b2975f` |
|  `1-dev` `1.23.0-dev` `1.23-dev` `latest-dev` | May 15th     | `sha256:8c7cb043dd4cb5ac645a1cb6c11bc190b60fe171f7b53637422f59c0f5b25101` |

