---
title: "etcd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the etcd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-13 00:52:18
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
|  `latest-dev` | March 12th   | `sha256:ef67019a469ed855832624770bd2b802c0f15298a7105d03846992421dd59329` |
|  `latest`     | March 8th    | `sha256:e8e0c8fab426aa43cd8e511c17e4676e363c535c357fd7fea955291ade24fcdb` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                      | Last Changed | Digest                                                                    |
|----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `3.5.12-dev` `3.5-dev` `3-dev` | March 12th   | `sha256:5d87b6cf8e1d1f73faebaa61ca46633962b38ca0b9bb051e12d7dabfd0727857` |
|  `3.4-dev` `3.4.30-dev`                      | March 12th   | `sha256:f6f47092b2f232d16e69fc8f1072d54f1af282f01ce8dad10baa6245e618279c` |
|  `3.4.30` `3.4`                              | March 9th    | `sha256:16c1a816f2c56039db6de1faad2f0975a307aba1bad5e0d5e3d9579d82e4a43b` |
|  `latest` `3.5.12` `3` `3.5`                 | March 8th    | `sha256:5aa6ed2dfe0e71a5916aed2b9b806b950f0d4e0809e110e7b5712ea6b2bd3a36` |

