---
title: "jenkins Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jenkins Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-25 00:42:19
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
|  `latest`     | June 24th    | `sha256:b32313449994a71cfd5e1c6374752e71e1d566d8b4122f7f4eb100e34ac39670` |
|  `latest-dev` | June 24th    | `sha256:a1e7f05fead0db926764d435060107934c183438e56c105284fe6dde8bd1e079` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                           | Last Changed | Digest                                                                    |
|-----------------------------------|--------------|---------------------------------------------------------------------------|
|  `2.463-dev` `2-dev` `latest-dev` | June 23rd    | `sha256:38cdaf7f96fd8f37cd8ce0375ebe16782327af8fda4d344885e750fa3d723a97` |
|  `2.463` `2` `latest`             | June 23rd    | `sha256:8a3aea0fed653cd14ecd1899351590fccbf4bf2a88fc4c09aeb71316d5c1e7e5` |
|  `2.462-dev`                      | June 19th    | `sha256:3923b2d716015552b02ae4765e153c1e2ee083f421b7bf7be47d807b1e6ce246` |
|  `2.462`                          | June 19th    | `sha256:84e6b9e31fb47e1004decb776f19dbf3f104703ce8e091821d5a4eddfca56614` |

