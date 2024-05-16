---
title: "helm Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the helm Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-16 00:37:58
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/helm/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/helm/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/helm/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/helm/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 15th     | `sha256:6f2a9fd83614d27dde15bb28dc712c9882ef550791f910ff3bfe92fd13806c6f` |
|  `latest`     | May 15th     | `sha256:5e0ae59804027d926209960ef8a0543e2e00ef94055162c228408b130d5518c3` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `3.15.0-dev` `3.15-dev` `latest-dev` `3-dev` | May 16th     | `sha256:8681ba4107ac5f3aa33e8c40440670e8639cbd1b6227d31277fb32371b8453eb` |
|  `3` `latest` `3.15.0` `3.15`                 | May 16th     | `sha256:b876a9cb7c2bf219508003a6a422808c2820cf311af067f4a71dadf7a254dbdd` |
|  `3.14.4` `3.14`                              | May 15th     | `sha256:0c177fb85d6a7f3fc6f3de13db8322905b5ddeb2fdea2113a68b5bf5ddcb8bdb` |
|  `3.14-dev` `3.14.4-dev`                      | May 15th     | `sha256:b719b4a6efbece5213320216dc6004777a23a3f73b4cb8b16fe88178525d096f` |
|  `3.11.3-dev` `3.11-dev`                      | May 13th     | `sha256:d19f95e05b32385f5bad1aabd0d3da598752a530f9b0bb9abed33ed96c17bbae` |
|  `3.11.3` `3.11`                              | May 13th     | `sha256:0ea603774d017c1a29e5664a95cfa1eab62906d8f13b2a508a55bf331254a248` |

