---
title: "etcd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the etcd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-09 00:39:12
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
|  `latest`     | July 8th     | `sha256:6cc7012362634aab28c7a76a5a3792e3886997e11115526ddabcdde6a03a4a1f` |
|  `latest-dev` | July 8th     | `sha256:59a3ef8e511d237374e4f301cc0c8991127c9bccfcb0358810988732fd089e3b` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                      | Last Changed | Digest                                                                    |
|----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `3.5.14` `3.5` `3`                 | July 8th     | `sha256:1a1999fbd8435746fdfaca91f0efe0ccae2c832af6eb94c2bebab849662034b2` |
|  `3-dev` `3.5-dev` `3.5.14-dev` `latest-dev` | July 8th     | `sha256:8e9ec43750dd2c9ce1ece42382e1c385469c042a9c02bbde340430fcb1b7fa5f` |
|  `3.4.33` `3.4`                              | July 8th     | `sha256:59ec476b66d562bfebb46e163e6b1a4d3a7ce390d7fef6d4ba73f8061ec47568` |
|  `3.4-dev` `3.4.33-dev`                      | July 8th     | `sha256:40dbf6798807b0590fdc8cc521e960aefb7c1185d499558655ee240a0fed54e2` |

