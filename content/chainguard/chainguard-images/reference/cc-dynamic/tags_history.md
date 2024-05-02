---
title: "cc-dynamic Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the cc-dynamic Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-02 00:37:55
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
|  `latest-dev` | May 1st      | `sha256:5b17896fdb870e5273001ad893f56106397d211530eadd8e18aa03130a085ee1` |
|  `latest`     | May 1st      | `sha256:5ec8356f509caf4abb8b1012b231fd4a31d1e470be0cb7b80097f7d0127d1483` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `13-dev` `13.2-dev` `latest-dev` `13.2.0-dev` | May 1st      | `sha256:33db291606141dc3d2002ceb14b6d0997730633bac58ba336bdab416d5fa4949` |
|  `latest` `13.2.0` `13.2` `13`                 | May 1st      | `sha256:3161293e2a4466dc70c27def55898061527ceb62249d17b3a56556982671c9e9` |

