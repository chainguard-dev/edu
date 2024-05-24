---
title: "etcd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the etcd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-24 00:45:45
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
|  `latest-dev` | May 23rd     | `sha256:43d132346be9141e3d0b731f8f2dca0aae59e84d3c6c798bbd238911c12b8526` |
|  `latest`     | May 23rd     | `sha256:fe3eefcb973de7af67b1f8a26b9d31d65e4d46b8a3fa66fd3c88ea8ac1057249` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                      | Last Changed | Digest                                                                    |
|----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `3.5.13-dev` `3-dev` `3.5-dev` `latest-dev` | May 23rd     | `sha256:2d2929713ab21afa681f92b2fceabf54891e54ed84bf8b619e9926ab0777e80d` |
|  `3.4.32-dev` `3.4-dev`                      | May 23rd     | `sha256:814c63a2f5d779bde91ca1d4e3c6ef9955d636458b94941418140bd0612bc970` |
|  `3.4` `3.4.32`                              | May 23rd     | `sha256:ee3de210f4c4233692bf7d383e45713d63c5b06c57fe78b2ece91f51b683c440` |
|  `3` `3.5` `latest` `3.5.13`                 | May 23rd     | `sha256:12b285e9204b41f1d65b690bb9225d469784a57f893d166b7aeb4dd53016a4f0` |
|  `3.5.8-dev`                                 | May 13th     | `sha256:5b821a307f18eab710c58a32e737f12670e35f9d433ca462be16b51aebab9eb9` |
|  `3.5.8`                                     | May 13th     | `sha256:ff1f804d0649f9cd97a9d0ff8de33d9b543a41bb4500c2af110e6c979d71c181` |

