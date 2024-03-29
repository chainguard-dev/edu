---
title: "cedar Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the cedar Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-29 00:47:42
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
|  `latest`     | March 28th   | `sha256:3c678b3f612f0d8b7c35fb5327c24f6deb7cbdade2b9221cb6a7046078f6b39e` |
|  `latest-dev` | March 28th   | `sha256:ffef461476e85f2f1ae5825e9e4ddf71a267904ca1b44bf905437691e18b5a6c` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `3.1` `3.1.1` `3`                 | March 28th   | `sha256:17302921c55438624c57e173f92b5fa363ebcc582248dfa5756406e22d696203` |
|  `3.1.1-dev` `3-dev` `latest-dev` `3.1-dev` | March 28th   | `sha256:ae46720556f3bf1e7fc2aa46d417c6f4ecdea00d5a50f5e970623369e1119d76` |
|  `3.1.0`                                    | March 14th   | `sha256:8fc3c1355bb7f4f67450e4059bd2362215c23c085a67d9064685280c4dc0e38f` |
|  `3.1.0-dev`                                | March 14th   | `sha256:f221d3cbd9ee7beb5099e58d2d48ab17da7b4855e3528673593b4e8c9dfd8ef1` |
|  `3.0-dev` `3.0.1-dev`                      | March 8th    | `sha256:c6e01f06c064c4113639003fafefddb4a4fab50f0d924aa6988be90dc5e75ae6` |
|  `3.0` `3.0.1`                              | March 8th    | `sha256:4d86d482eecc0cb5c2c2ade17e5b13db5925b60d24f59540c84f2a29c769caef` |

