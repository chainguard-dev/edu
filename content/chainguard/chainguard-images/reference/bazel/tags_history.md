---
title: "bazel Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the bazel Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-23 00:45:07
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/bazel/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/bazel/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/bazel/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/bazel/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | May 22nd     | `sha256:2f7bea6d4a365a2365e738f51feaa839e5531e6e20f34188afd544e4c1835065` |
|  `latest-dev` | May 22nd     | `sha256:67c331cf505f7aad0f4c473418b592bdd12894d9aee3bcb094036b4f8a447c5b` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `5.4` `5.4.1` `5`                          | May 22nd     | `sha256:d539482a698c94089ee1501e220ac9c65d698d9c79736bebd253dee505ff9c90` |
|  `6.5` `6` `6.5.0`                          | May 22nd     | `sha256:3e62fd530e6b31494471d0ddc3cfc9853fe7c0a417076dac0013759a8116f703` |
|  `latest-dev` `7-dev` `7.1.2-dev` `7.1-dev` | May 22nd     | `sha256:12cc907fb6357337f6400af8b405235422d08f341957303e73bced7e997f6c56` |
|  `6.5.0-dev` `6.5-dev` `6-dev`              | May 22nd     | `sha256:838294982afdb3695736207e316f765074452f8ac67d174d9778994d3b62467d` |
|  `5.4.1-dev` `5.4-dev` `5-dev`              | May 22nd     | `sha256:f275719898c9bd7127242724c3d2fdb31729ce1531b11f4fa58d57c384a1c609` |
|  `7` `latest` `7.1.2` `7.1`                 | May 22nd     | `sha256:f4e82a521873a444745267a78239ebb3d587af5ba68d8b1e2562c77de7088748` |
|  `7.1.1`                                    | May 9th      | `sha256:14417579783d4513144a3ed611a6b3dbb2c5cc51453ad7c11cf3cdb595d737b2` |
|  `7.1.1-dev`                                | May 9th      | `sha256:cdd252e8dac5c1ceccfa2b49bb2279867f4c5686a559e40122327b9b37a114f7` |
|  `6.1.2` `6.1`                              | May 22nd     | `sha256:eed2d4f320442b1498ee44dc54efd331844d9e2c7ec1a2ff0458bd2762172d0c` |
|  `6.1.1`                                    | April 28th   | `sha256:e779a5ec7dfce8190755a7c683f3f8fed331ac6909ec52270d35362fba8df214` |

