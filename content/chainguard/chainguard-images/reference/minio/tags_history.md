---
title: "minio Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the minio Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-23 00:43:06
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
|  `latest-dev` | June 22nd    | `sha256:8b46c273b6ffc9803763b06a6080c982ab852e5a480f509f9daad149a2992ae3` |
|  `latest`     | June 19th    | `sha256:9289658215a457707736aa40d797a2af1be70b1a4b9306569b1fd7ebdeff3768` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)               | Last Changed | Digest                                                                    |
|-----------------------|--------------|---------------------------------------------------------------------------|
|  `0-dev` `latest-dev` | June 22nd    | `sha256:ede31429e6c6d91f13ba5c51312363697ef0e9b05bccb4c93cd1f1f5f3c80867` |
|  `latest` `0`         | June 22nd    | `sha256:9827f4937fcb976d3da7629514561de7a1475e2360c18fc9f3e6a206e45c39c3` |

