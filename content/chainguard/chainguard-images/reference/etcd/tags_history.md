---
title: "etcd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the etcd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-23 00:45:07
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
|  `latest-dev` | May 22nd     | `sha256:678ae497a891995cab96cd51152130657af52c07d46bc2eacbc9a4ccbae6d931` |
|  `latest`     | May 21st     | `sha256:8e97c98dd857de18f7033ca489ca5552ebfc33c4562a6235017c747472a4b8ff` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                      | Last Changed | Digest                                                                    |
|----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `3.5-dev` `3-dev` `3.5.13-dev` | May 22nd     | `sha256:19991ba7e7ba7c90c68d26134a26f3f2d199c3972b26bd5dfafe4b4026b28bd2` |
|  `3.4.32-dev` `3.4-dev`                      | May 22nd     | `sha256:1d2426ef48935529f0d528d882491d3daab8027265929907690a59589ea05eaa` |
|  `3.4` `3.4.32`                              | May 21st     | `sha256:10e0add6a23b2da837b12803791412b41801412be314e72879b835648736b7af` |
|  `3` `latest` `3.5` `3.5.13`                 | May 21st     | `sha256:b19640e768aabaf6f07ee68a2ce3530e07325317e905033c49672bfe8c9535dd` |
|  `3.5.8-dev`                                 | May 13th     | `sha256:5b821a307f18eab710c58a32e737f12670e35f9d433ca462be16b51aebab9eb9` |
|  `3.5.8`                                     | May 13th     | `sha256:ff1f804d0649f9cd97a9d0ff8de33d9b543a41bb4500c2af110e6c979d71c181` |

