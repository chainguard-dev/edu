---
title: "clang Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the clang Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-29 00:47:42
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/clang/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/clang/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/clang/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/clang/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | March 28th   | `sha256:7f8eef1cce7638bc65bb33a17f7d911a19c20cb6f6459718eb6857b82dffa5e9` |
|  `latest-dev` | March 28th   | `sha256:0bca2269feb2415b63db30efa4e7b3d827ba394b0d1fa40d93c8fdc47d8ca0d6` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `15` `latest` `15.0` `15.0.7`                 | March 28th   | `sha256:93254bec1f1fe06610fc2017fdd5b350c0d3d4ea74b1fce8e40ce9749b76990d` |
|  `15-dev` `latest-dev` `15.0.7-dev` `15.0-dev` | March 28th   | `sha256:d9f95d1a217e9d4e9c175c9cc1792054d544426d262ba352003cc8e5549a8c61` |

