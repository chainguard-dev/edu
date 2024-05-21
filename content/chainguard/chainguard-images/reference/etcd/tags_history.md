---
title: "etcd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the etcd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-21 00:38:36
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
|  `latest-dev` | May 20th     | `sha256:873d02990e33ed91ab72c64fd2910db8dbfe5abc9c4519e26dbb741cb32c78f3` |
|  `latest`     | May 17th     | `sha256:301d8edf90c9f49c9c591bda6a26eb516136695699f66ac5027b118f46847fe4` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                      | Last Changed | Digest                                                                    |
|----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `3.5.13-dev` `3-dev` `3.5-dev` `latest-dev` | May 19th     | `sha256:a1739033010c55d77a47e1e167fcc41deb002778c2dc9f047aef32558ead4fa1` |
|  `3.4.32-dev` `3.4-dev`                      | May 19th     | `sha256:79a82bdedd87ddd7fb7bdbae26cd2da28e9085c7be9f4fc78ed39cc969e8e0e2` |
|  `3.4` `3.4.32`                              | May 17th     | `sha256:4dbd93ea20d5e7b91d0b018ecfe4cb2acc5959632aeaa1556867fa32d2fe927e` |
|  `3.5.13` `3` `latest` `3.5`                 | May 17th     | `sha256:82ee740e6264b862b63fc0591a387595ab18541f2d518f87224953a2300394ba` |
|  `3.4.31`                                    | April 21st   | `sha256:5d8abbcfb187978ef20eaca3d2b18382debc0f9e4095113a82136db41e34c04a` |
|  `3.4.31-dev`                                | April 21st   | `sha256:20d7842e9556329750de78172129f388f124a41b10aa679d691d01eec64eecd7` |
|  `3.5.8-dev`                                 | May 13th     | `sha256:5b821a307f18eab710c58a32e737f12670e35f9d433ca462be16b51aebab9eb9` |
|  `3.5.8`                                     | May 13th     | `sha256:ff1f804d0649f9cd97a9d0ff8de33d9b543a41bb4500c2af110e6c979d71c181` |

