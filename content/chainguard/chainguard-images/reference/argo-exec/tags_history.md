---
title: "argo-exec Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the argo-exec Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-22 00:34:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/argo-exec/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/argo-exec/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/argo-exec/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/argo-exec/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | March 21st   | `sha256:8f45c850c2061725f0ab8de5eed96591d38a900c39c51547d0445e8f90e32add` |
|  `latest`     | March 21st   | `sha256:d4017c2de60425cb06a86db7150209545ef02de7f6175f787f5065bfcd493748` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed  | Digest                                                                    |
|---------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `latest-dev` `3.5-dev` `3-dev` `3.5.5-dev` | March 21st    | `sha256:3d4cd4daa4f8dfd49cc72f1d373664c6f25f5625f735eb77ab75c31c2985e4c8` |
|  `3` `latest` `3.5` `3.5.5`                 | March 21st    | `sha256:108a7ac3f3c5c8404c80c6170ae0a83bbd981ce73616670d03a9dd09a2d42e66` |
|  `3.5.4`                                    | February 26th | `sha256:4440013a8470d0eb317d39d1381bfd3af6e357a7ed8f1b473b3bc824068f9e81` |
|  `3.5.4-dev`                                | February 26th | `sha256:e87ec60f76dbf0093f0f9582d109a2c9214e54f27d432548f045dfbaac6d6ec7` |

