---
title: "jenkins Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jenkins Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-30 00:47:59
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
|  `2-dev` `latest-dev` `2.459-dev` | May 29th     | `sha256:10fb40435b7a3a233bf6158b36a7b8641c3107e1830acd4e419f1fd17b878542` |
|  `2` `latest` `2.459`             | May 29th     | `sha256:96052b641ff789e5aad8bd519c329a852deb25e41d91d5df8130c6eed6365fd9` |
|  `2.458-dev`                      | May 21st     | `sha256:16bfb312accf7bca8cc909b2eb3a912bea1f768531d468649ba58159287c1244` |
|  `2.458`                          | May 21st     | `sha256:f3b60257ccb43880ae7d4b69bcf119848ca8410ff5fbde0645300abeb93251cf` |
|  `2.456-dev`                      | May 14th     | `sha256:78d93481a2abc64cb0d85b70664998503253d03ed0284d1b2b6b702d63daea7d` |
|  `2.456`                          | May 13th     | `sha256:f09ede8c004bb845b34d7aec9e1a3f83daa9e231a1208627bf3f8c6f0ef95b2e` |

