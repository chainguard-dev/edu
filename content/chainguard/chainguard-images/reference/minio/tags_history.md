---
title: "minio Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the minio Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-19 00:54:00
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
|  `latest`     | March 18th   | `sha256:40b5639355d7680f19df7311b73174506500aedadf402b57f25d5361a2b51edd` |
|  `latest-dev` | March 18th   | `sha256:22aeb1d4759e1bb5e0a2f8fb464c93f5a5a444a9ab781d201064fb57033600db` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)               | Last Changed | Digest                                                                    |
|-----------------------|--------------|---------------------------------------------------------------------------|
|  `0` `latest`         | March 18th   | `sha256:53332952c42680baa9b26afbe821830ec03a03edd2366f5140946064d5e8a4d9` |
|  `latest-dev` `0-dev` | March 18th   | `sha256:c8b45391edad376d917530c66f0cd841c36104cb5f66275ef4723e261e3f5bbe` |

