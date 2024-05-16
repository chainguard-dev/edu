---
title: "etcd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the etcd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-16 00:37:58
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/etcd/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/etcd/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/etcd/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/etcd/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | May 15th     | `sha256:434d1a675057bfe232d66c644c7e2632bae4ed6aa1b8d1fc9d0fc6b4b05cee32` |
|  `latest-dev` | May 15th     | `sha256:d6e3dfc8f86c26984398f1c8cd146e54164ad0d092f37da463706948b94e7c5a` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                      | Last Changed | Digest                                                                    |
|----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `3` `latest` `3.5.13` `3.5`                 | May 15th     | `sha256:9827219d386ca1f07a34783ed12b7d568eb0fc1b1296f28ac66e41bc22eededb` |
|  `3.4-dev` `3.4.32-dev`                      | May 15th     | `sha256:b16b748e88d11880f90e170eb192dcc76dfeee685dde2cd07d9cf3634a5b1188` |
|  `3-dev` `3.5-dev` `3.5.13-dev` `latest-dev` | May 15th     | `sha256:3dc87fad05c674b35073d0a92eb55f6c5649842f8c4f9e3d39ad84d5f0988923` |
|  `3.4` `3.4.32`                              | May 15th     | `sha256:069afffaf207bcccda1721ec4c5c32f340c56e51d3c65bd4628521c72e57fc1e` |
|  `3.4.31`                                    | April 21st   | `sha256:5d8abbcfb187978ef20eaca3d2b18382debc0f9e4095113a82136db41e34c04a` |
|  `3.4.31-dev`                                | April 21st   | `sha256:20d7842e9556329750de78172129f388f124a41b10aa679d691d01eec64eecd7` |
|  `3.5.8-dev`                                 | May 13th     | `sha256:5b821a307f18eab710c58a32e737f12670e35f9d433ca462be16b51aebab9eb9` |
|  `3.5.8`                                     | May 13th     | `sha256:ff1f804d0649f9cd97a9d0ff8de33d9b543a41bb4500c2af110e6c979d71c181` |

