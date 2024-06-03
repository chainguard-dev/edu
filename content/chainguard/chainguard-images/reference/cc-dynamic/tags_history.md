---
title: "cc-dynamic Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the cc-dynamic Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-03 00:46:08
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/cc-dynamic/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/cc-dynamic/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/cc-dynamic/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/cc-dynamic/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 1st     | `sha256:3377cfcd915e80f34cfdeb4f143249ce520d3fd90218006c190d9ce39dd21289` |
|  `latest`     | May 23rd     | `sha256:8274e806c70e6b0a5a8905be6d86539b1ab5843a080cdabbe40517faf8c4215e` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `13-dev` `13.2-dev` `latest-dev` `13.2.0-dev` | June 1st     | `sha256:ef53bd41c539614a7c767e7f79d6d1ef6feda677d7474f7f151057e7c9e9e227` |
|  `latest` `13` `13.2` `13.2.0`                 | May 23rd     | `sha256:420d11593ff7d9e1d297bfc223ca9b656b6474e243f3545089c7c66969cf6438` |

