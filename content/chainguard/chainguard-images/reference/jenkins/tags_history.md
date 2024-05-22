---
title: "jenkins Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jenkins Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-22 00:47:17
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
|  `latest-dev` | May 21st     | `sha256:d9b17bc9a667356d3d5b15a4d0693b56d4300e8efd9d7ab7112f3cec8e82b6d4` |
|  `latest`     | May 21st     | `sha256:78a0a4e91c07657e4f0eb8f02289ce8cc53c63baa52b9c1b05c9a75114c7b792` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                           | Last Changed | Digest                                                                    |
|-----------------------------------|--------------|---------------------------------------------------------------------------|
|  `2-dev` `latest-dev` `2.459-dev` | May 21st     | `sha256:ac2cb394a9999a3706dc50f9560671680e04360efb5823801e9aac58f2431707` |
|  `2` `latest` `2.459`             | May 21st     | `sha256:787c360d47e39e1b6b0fb619397a1443b09b87d202f362ed5d0d84a0478363f8` |
|  `2.458-dev`                      | May 21st     | `sha256:16bfb312accf7bca8cc909b2eb3a912bea1f768531d468649ba58159287c1244` |
|  `2.458`                          | May 21st     | `sha256:f3b60257ccb43880ae7d4b69bcf119848ca8410ff5fbde0645300abeb93251cf` |
|  `2.456-dev`                      | May 14th     | `sha256:78d93481a2abc64cb0d85b70664998503253d03ed0284d1b2b6b702d63daea7d` |
|  `2.456`                          | May 13th     | `sha256:f09ede8c004bb845b34d7aec9e1a3f83daa9e231a1208627bf3f8c6f0ef95b2e` |
|  `2.455-dev`                      | April 30th   | `sha256:c6c70361a2cc0bf7f3b801ca93281127280a1c7559105f7959bd825706ae763d` |
|  `2.455`                          | April 30th   | `sha256:003a795dbe4a264d127bd667bd2fdfe0397e336c1125b76d927ee701f7c5c4ab` |

