---
title: "gradle Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the gradle Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-09 00:39:12
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/gradle/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/gradle/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/gradle/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/gradle/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)   | Last Changed | Digest                                                                    |
|-----------|--------------|---------------------------------------------------------------------------|
|  `latest` | July 3rd     | `sha256:2668ae75a25d5014443a8441126961852f1f80b40b8e5a13400b3529bff3c5c2` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-17-8` `openjdk-17-8.8.0` `openjdk-17` `openjdk-17-8.8`                              | July 8th     | `sha256:d520658e9e1ae5be345e4aee0cfcce21bcee67d2b1cbe6027858fdf4888efee7` |
|  `openjdk-21-8.8.0-dev` `openjdk-21-dev` `openjdk-21-8-dev` `openjdk-21-8.8-dev` `latest-dev` | July 8th     | `sha256:c4575ded33e9c0cf22bb5b9e19c12ebb10a366047a83d57d714f10eef1dc8fef` |
|  `openjdk-17-8.8-dev` `openjdk-17-8.8.0-dev` `openjdk-17-8-dev` `openjdk-17-dev`              | July 8th     | `sha256:10e1d560f907bc68d7fa5c3c30d203d86ed0a103f5289c67cf566ce5d91bd8e7` |
|  `openjdk-21-8.8` `openjdk-21` `openjdk-21-8` `openjdk-21-8.8.0` `latest`                     | July 8th     | `sha256:fd5697854da53c45bf73c9b084f14a3ffe1aa5df5db28e12f5a6873f1596f8b1` |

