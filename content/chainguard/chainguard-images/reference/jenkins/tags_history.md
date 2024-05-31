---
title: "jenkins Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jenkins Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-31 00:48:45
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/jenkins/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/jenkins/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/jenkins/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/jenkins/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | May 30th     | `sha256:6abe6044c9223bccf92f67792bd0d5121405974a723b2eb8ac0ad9d46d2dd9bc` |
|  `latest-dev` | May 30th     | `sha256:7579366c38dfd8d96e0d68696d93a4ccb4a672e023db9d5f93ef23cf7952f7f7` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                           | Last Changed | Digest                                                                    |
|-----------------------------------|--------------|---------------------------------------------------------------------------|
|  `2.459-dev` `2-dev` `latest-dev` | May 30th     | `sha256:26e375b5d6fd31ba75d1e9c302144e75b4a3e1df7f4421b6785eae2f8d11c575` |
|  `2.459` `2` `latest`             | May 30th     | `sha256:fd907ad1e0fa7a863df75528aeca2c648fb234b3412265c8d0af7c06b08816e2` |
|  `2.458-dev`                      | May 21st     | `sha256:16bfb312accf7bca8cc909b2eb3a912bea1f768531d468649ba58159287c1244` |
|  `2.458`                          | May 21st     | `sha256:f3b60257ccb43880ae7d4b69bcf119848ca8410ff5fbde0645300abeb93251cf` |
|  `2.456-dev`                      | May 14th     | `sha256:78d93481a2abc64cb0d85b70664998503253d03ed0284d1b2b6b702d63daea7d` |
|  `2.456`                          | May 13th     | `sha256:f09ede8c004bb845b34d7aec9e1a3f83daa9e231a1208627bf3f8c6f0ef95b2e` |

