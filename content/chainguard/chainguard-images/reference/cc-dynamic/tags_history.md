---
title: "cc-dynamic Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the cc-dynamic Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-15 00:39:35
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
|  `latest-dev` | May 14th     | `sha256:4412c903c284d24277b65b2146e108da2522ce48d7e15b6a3a46412c103c5038` |
|  `latest`     | May 2nd      | `sha256:5eaef0efce22c37d1c24ac122e2e68f64278f4ab38cda5fb237acd35287e62d3` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `13.2-dev` `latest-dev` `13-dev` `13.2.0-dev` | May 14th     | `sha256:e7032873aabe80ce94ca03a2853f9683605e97bef7ffe18d57171fb87333aad2` |
|  `13` `latest` `13.2.0` `13.2`                 | May 2nd      | `sha256:1acc3789052ef300f465f892b4f75a48275ffeee2a25e9fac0844664da57fb5e` |

