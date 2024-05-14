---
title: "etcd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the etcd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-14 00:46:23
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
|  `latest-dev` | May 13th     | `sha256:1316353f2e6806295677e0dfa566eaba203b69fb7afdc0dfbdd3ecb87ccecf3e` |
|  `latest`     | May 10th     | `sha256:798054fd77e1a0f65824ee5600ac9389f4caadc001be8f427d94d6d4502cb606` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                      | Last Changed | Digest                                                                    |
|----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `3.4.32-dev` `3.4-dev`                      | May 13th     | `sha256:438ce9f5b002822563ab7531db95cffe1aaa75400a4be7b19aac8227baf1a6ad` |
|  `3.5-dev` `3-dev` `3.5.13-dev` `latest-dev` | May 13th     | `sha256:3d866f3c01e0d536a07db5fec6edc75dd5ba869bbddd27b452389e0fac6b5979` |
|  `3.4` `3.4.32`                              | May 10th     | `sha256:bb5a0f4ddfc43599d3e6b5ae2d3bb10143b2e55954acdadea4c4c5904c9a4ae4` |
|  `latest` `3.5.13` `3` `3.5`                 | May 9th      | `sha256:43b93f50ab25e41b7ccb34683ee340d4c98e1b7ac9506e630ea383c3d20ab879` |
|  `3.4.31`                                    | April 21st   | `sha256:5d8abbcfb187978ef20eaca3d2b18382debc0f9e4095113a82136db41e34c04a` |
|  `3.4.31-dev`                                | April 21st   | `sha256:20d7842e9556329750de78172129f388f124a41b10aa679d691d01eec64eecd7` |
|  `3.5.8-dev`                                 | May 13th     | `sha256:5b821a307f18eab710c58a32e737f12670e35f9d433ca462be16b51aebab9eb9` |
|  `3.5.8`                                     | May 13th     | `sha256:ff1f804d0649f9cd97a9d0ff8de33d9b543a41bb4500c2af110e6c979d71c181` |

