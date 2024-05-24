---
title: "jenkins Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jenkins Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-24 00:45:45
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
|  `latest`     | May 23rd     | `sha256:01d992ce05664ddcbabe07a21b0ee587b700896015b46e6c5a55eba47ca58cbd` |
|  `latest-dev` | May 23rd     | `sha256:cc8f3690102a3d308357bfdc71d6b277a27b69393761931a99084460b91a0850` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                           | Last Changed | Digest                                                                    |
|-----------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `2.459-dev` `2-dev` | May 24th     | `sha256:ab47c2affc15d56d719580eb7f5cae3e31939f25f20953973e42cf8dc2b203d6` |
|  `latest` `2.459` `2`             | May 24th     | `sha256:a68e04465660a084f07c050d1a2bcf62978e4a769ab697b92caf3cf9d79ebe00` |
|  `2.458-dev`                      | May 21st     | `sha256:16bfb312accf7bca8cc909b2eb3a912bea1f768531d468649ba58159287c1244` |
|  `2.458`                          | May 21st     | `sha256:f3b60257ccb43880ae7d4b69bcf119848ca8410ff5fbde0645300abeb93251cf` |
|  `2.456-dev`                      | May 14th     | `sha256:78d93481a2abc64cb0d85b70664998503253d03ed0284d1b2b6b702d63daea7d` |
|  `2.456`                          | May 13th     | `sha256:f09ede8c004bb845b34d7aec9e1a3f83daa9e231a1208627bf3f8c6f0ef95b2e` |
|  `2.455-dev`                      | April 30th   | `sha256:c6c70361a2cc0bf7f3b801ca93281127280a1c7559105f7959bd825706ae763d` |
|  `2.455`                          | April 30th   | `sha256:003a795dbe4a264d127bd667bd2fdfe0397e336c1125b76d927ee701f7c5c4ab` |

