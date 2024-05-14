---
title: "minio Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the minio Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-14 00:46:23
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/minio/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/minio/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/minio/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/minio/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 13th     | `sha256:d8ac9841a99322fc6b86905e343836bd7b1191f60a8886466246a3f9cfeb342c` |
|  `latest`     | May 13th     | `sha256:3e47852d9ccffbd65387856d5c0cce7df612c26a1d3d76ca14f9b8c5c3322e12` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)               | Last Changed | Digest                                                                    |
|-----------------------|--------------|---------------------------------------------------------------------------|
|  `0-dev` `latest-dev` | May 13th     | `sha256:a5d10c4804621de6dda990b8066836ec843fba9fb20f99c2aea996b136151739` |
|  `0` `latest`         | May 13th     | `sha256:c8914ab8e699ba10b6846cdacbc8e56a510c241810da6fa70eaafdb80ab85668` |

