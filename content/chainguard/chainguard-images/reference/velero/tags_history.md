---
title: "velero Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the velero Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-30 00:47:59
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/velero/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/velero/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/velero/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/velero/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | May 23rd     | `sha256:3c42456aac98487bace64630b9b377048b9eb4eca255bf7c8e15e06b32f63b18` |
|  `latest-dev` | May 23rd     | `sha256:2d454817ea8a55729fa3fea40e9917232059caf48a132cb98474e491c1d5d6a3` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.13.2-dev` `1-dev` `latest-dev` `1.13-dev` | May 29th     | `sha256:11977ef537ea1335540b1bf191fd66552541bedd0cc7fae20b6d5880ff373bb0` |
|  `1` `latest` `1.13` `1.13.2`                 | May 29th     | `sha256:0a5a0779652942fc276f6b36d9f4d55151b586803f3f9047b34ce60c699c2568` |

