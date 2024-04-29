---
title: "cosign Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the cosign Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-29 00:53:42
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/cosign/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/cosign/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/cosign/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/cosign/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | April 26th   | `sha256:4045ba01e1b261048856d2fe5a84338b4e4dbfe2df68ea6b66fde1cd9e0aaa37` |
|  `latest-dev` | April 26th   | `sha256:ceed44af67c37b86f9eb9bf2ae6d649286f0dbf44e7295532b8dd89624b963c7` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2.2-dev` `2-dev` `2.2.4-dev` `latest-dev` | April 26th   | `sha256:44f5a1618e11004b5c0ffd92e2a62d53dd3c82a747797ad1755451e342277486` |
|  `2` `2.2.4` `latest` `2.2`                 | April 26th   | `sha256:54cb093348aaeb602ac459f081ef4c998873bc6eaa6204acd64edac3222b09e2` |
|  `2.2.3-dev`                                | April 9th    | `sha256:1da0d2dcea301b70e54b4962bb344ff54e275a8e6024e083c04b1cbd99367c07` |
|  `2.2.3`                                    | April 3rd    | `sha256:1e547bf52787126db0e5a5e73893dd24e2b98d97eabf9816f7545670bbdaac40` |
|  `2.0.1-dev`                                | April 25th   | `sha256:0f8ffca811eab50fbca70379a3316113075cc46b8a09e880f7d831bdb66f689e` |
|  `2.0.1`                                    | April 25th   | `sha256:1418e13c3479d1a8d068325a97a4a4fbf437d12cb6d5fbfb7160c2f40a239e0b` |

