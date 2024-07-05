---
title: "litestream Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the litestream Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-05 00:42:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/litestream/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/litestream/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/litestream/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/litestream/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | July 3rd     | `sha256:36bd20ec05fa02d993fefcbc7e9f5f7d36860e5fe7f5558a8cf8058435fb58d5` |
|  `latest-dev` | July 3rd     | `sha256:1955d45bb3ac46e6316115142621293ca8ab3d862828bcb510d35a39118c3d90` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                      | Last Changed | Digest                                                                    |
|----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0-dev` `latest-dev` `0.3-dev` `0.3.13-dev` | July 3rd     | `sha256:5e8849c893b3d649e1c711c9283b86dccbe3c63ff6ecaa4f111babc351f4ad62` |
|  `0.3.13` `latest` `0.3` `0`                 | July 3rd     | `sha256:05dbbca655e0fc58f73a0a89bfa96b88a49ec8ca8c9e4f0406f5b88c264bc8c7` |

