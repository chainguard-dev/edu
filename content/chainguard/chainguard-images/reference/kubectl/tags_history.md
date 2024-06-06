---
title: "kubectl Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the kubectl Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-06 00:48:16
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
|  `latest-dev` | June 5th     | `sha256:90baeba1b84c098ad2f5ff157363f46cd0996656e0989bc10aa12614e24fb493` |
|  `latest`     | June 5th     | `sha256:a9ad484dac0e52b6a59996565dbdb35d5ef084a2df7dd3782d09be722cb8396a` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.29.5-dev` `1.29-dev`                      | June 5th     | `sha256:9238edd9ed76be71dcc746edf01d6a58da04044bc6744a5223be6f20b80bbbe0` |
|  `1.28` `1.28.10`                             | June 5th     | `sha256:d7a7a9d3b17e5cff5941bd2b68731c3188a54f2b06f293916140e77443ebf179` |
|  `1.27` `1.27.14`                             | June 5th     | `sha256:f7605e34b52564a2492774a527d4aca7e096fe87116449ff6cb2df552d61f228` |
|  `1.27.14-dev` `1.27-dev`                     | June 5th     | `sha256:23badd925f37e22f32dc917865d22e0f8cf61ced365c05b27da5447f695936b8` |
|  `1.29` `1.29.5`                              | June 5th     | `sha256:8078e5fb80b1240aa6db1048f771851dfc8eadf1f118fad452405b83d61015fc` |
|  `1.28-dev` `1.28.10-dev`                     | June 5th     | `sha256:c64c72ce28a67dba73430947abdc4d64ff1e09bb636bfcc2add48c9196dc6002` |
|  `latest-dev` `1-dev` `1.30.1-dev` `1.30-dev` | June 5th     | `sha256:ec522912d1347933d263333a8ee41e622cd3838c3d50115a4722bbc4fd56b98c` |
|  `1.30.1` `latest` `1.30` `1`                 | June 5th     | `sha256:a9035436de99e77c1c9aeb6d5140a17034ce2f194b0378252252e233d72316a5` |

