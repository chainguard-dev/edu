---
title: "cedar Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the cedar Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-28 00:50:32
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/cedar/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/cedar/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/cedar/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/cedar/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | March 18th   | `sha256:603303ec091e879bfe2e2b2de526bfe426f26e2bec54b4cde078077297b90d08` |
|  `latest`     | March 18th   | `sha256:20742ca7047e20bfacdf82fbdf8710e52e8121a3e6e7046a45d1b9718182be00` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `3.1.1-dev` `latest-dev` `3-dev` `3.1-dev` | March 27th   | `sha256:91c6b1e3aa8590e206cbe98c2afec28b141e28a0e987cb3e03aa145c2480bd00` |
|  `3` `latest` `3.1` `3.1.1`                 | March 27th   | `sha256:70a4ee4a84311e953d10b9bf27f5d16eadbe43cd514be9fe6596758f8005afae` |
|  `3.1.0`                                    | March 14th   | `sha256:8fc3c1355bb7f4f67450e4059bd2362215c23c085a67d9064685280c4dc0e38f` |
|  `3.1.0-dev`                                | March 14th   | `sha256:f221d3cbd9ee7beb5099e58d2d48ab17da7b4855e3528673593b4e8c9dfd8ef1` |
|  `3.0-dev` `3.0.1-dev`                      | March 8th    | `sha256:c6e01f06c064c4113639003fafefddb4a4fab50f0d924aa6988be90dc5e75ae6` |
|  `3.0` `3.0.1`                              | March 8th    | `sha256:4d86d482eecc0cb5c2c2ade17e5b13db5925b60d24f59540c84f2a29c769caef` |

