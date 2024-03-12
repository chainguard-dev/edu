---
title: "buildkit Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the buildkit Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-12 00:55:01
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/buildkit/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/buildkit/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/buildkit/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/buildkit/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)            | Last Changed | Digest                                                                    |
|--------------------|--------------|---------------------------------------------------------------------------|
|  `latest-root-dev` | March 11th   | `sha256:292948e8a49626c4de0ffa38455da9ef3d13ab703ddf63fdf082509e062845f2` |
|  `latest-root`     | March 8th    | `sha256:c9c27fa201cd2d3db6b2ce7484f2b124acf5d884a37a4ddd9004a9d88ca462ac` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed  | Digest                                                                    |
|-----------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `0.13.0-dev` `0.13-dev` `latest-dev` `0-dev` | March 10th    | `sha256:cda0fac4cb765648f0079f74e2f21c153ae957d03bf82d287dd6b0dc513ec1ae` |
|  `latest` `0` `0.13` `0.13.0`                 | March 8th     | `sha256:994cc3f25ea043affd8a9bec006912b2f831ae28ece1fa48eaa83b15989e6432` |
|  `0.12-dev` `0.12.5-dev`                      | March 7th     | `sha256:eb2452151ab5c3adf7ee6f6d1f4dfd4a968e70234b83d642522e66703d244d2a` |
|  `0.12.5` `0.12`                              | March 7th     | `sha256:e132b011e8b5ac50ba5d5f602001286e59f82c4cb8348a83db7e5aff1f8a06f4` |
|  `latest-root-dev`                            | February 15th | `sha256:fbdaabead056fc1bff769880be0f207ec52f27a465cf8f22ecc8f39af6651241` |

