---
title: "kubectl Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the kubectl Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-10 00:50:47
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/kubectl/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/kubectl/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/kubectl/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kubectl/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 9th     | `sha256:84a8ea46b33c167ce37f1c022b42675372c03ef5c0dfc768a427a745a9d88602` |
|  `latest`     | June 5th     | `sha256:a9ad484dac0e52b6a59996565dbdb35d5ef084a2df7dd3782d09be722cb8396a` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.29.5-dev` `1.29-dev`                      | June 8th     | `sha256:1734168049cd9b52d5fcf1f928eaa961fd8fc50d34e9e88d6f99239144965566` |
|  `1.30-dev` `latest-dev` `1-dev` `1.30.1-dev` | June 8th     | `sha256:3f062ed6a0cc477f75e7ea629991772266b77f5a24ae69ff2ba5aaa1f16c9f74` |
|  `1.28.10-dev` `1.28-dev`                     | June 8th     | `sha256:8dd74b202f91ee987b725038b087956560cc5160ab1a84a5d2d8ea8d7d34951d` |
|  `1.27-dev` `1.27.14-dev`                     | June 8th     | `sha256:27fd9bab92cc127a8f40bf71d805da8c439ff65ea9e349a515a84373a3932f55` |
|  `1.28` `1.28.10`                             | June 5th     | `sha256:d7a7a9d3b17e5cff5941bd2b68731c3188a54f2b06f293916140e77443ebf179` |
|  `1.27` `1.27.14`                             | June 5th     | `sha256:f7605e34b52564a2492774a527d4aca7e096fe87116449ff6cb2df552d61f228` |
|  `1.29` `1.29.5`                              | June 5th     | `sha256:8078e5fb80b1240aa6db1048f771851dfc8eadf1f118fad452405b83d61015fc` |
|  `1.30.1` `latest` `1.30` `1`                 | June 5th     | `sha256:a9035436de99e77c1c9aeb6d5140a17034ce2f194b0378252252e233d72316a5` |

