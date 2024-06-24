---
title: "jenkins Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jenkins Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-24 00:43:49
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
|  `latest-dev` | June 22nd    | `sha256:b3f521428b97f664f03b4db325a0f86ba4f87c27bf7b72f4cc420f8924e4277c` |
|  `latest`     | June 22nd    | `sha256:501265fae38cde42b623186df03cc427413e582f31c8cf60b623c1f2e18ba945` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                           | Last Changed | Digest                                                                    |
|-----------------------------------|--------------|---------------------------------------------------------------------------|
|  `2.463-dev` `2-dev` `latest-dev` | June 23rd    | `sha256:38cdaf7f96fd8f37cd8ce0375ebe16782327af8fda4d344885e750fa3d723a97` |
|  `2.463` `2` `latest`             | June 23rd    | `sha256:8a3aea0fed653cd14ecd1899351590fccbf4bf2a88fc4c09aeb71316d5c1e7e5` |
|  `2.462-dev`                      | June 19th    | `sha256:3923b2d716015552b02ae4765e153c1e2ee083f421b7bf7be47d807b1e6ce246` |
|  `2.462`                          | June 19th    | `sha256:84e6b9e31fb47e1004decb776f19dbf3f104703ce8e091821d5a4eddfca56614` |

