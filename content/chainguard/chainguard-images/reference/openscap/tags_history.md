---
title: "openscap Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the openscap Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-02 00:32:13
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/openscap/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/openscap/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/openscap/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/openscap/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | July 1st     | `sha256:a10debc95ef873e5fc6ff4e46cb80bbc87f55a611ed03481a8491dc01181ca8a` |
|  `latest`     | July 1st     | `sha256:db5401d7c82f6790dfa8749303c072caca7f2be013629108c1a78ab85812f787` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                      | Last Changed | Digest                                                                    |
|----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.3.10` `1.3` `1` `latest`                 | July 1st     | `sha256:477d54690943b722e09e41bea22089cc1c29d9c2e82f370d2db1b6736dbe4c27` |
|  `1-dev` `latest-dev` `1.3.10-dev` `1.3-dev` | July 1st     | `sha256:c4cb79759132cf1b8d95b8ff047c22a7c882d2dc93f50095f5dbff66f80d47b1` |

