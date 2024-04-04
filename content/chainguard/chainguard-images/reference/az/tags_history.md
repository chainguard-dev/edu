---
title: "az Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the az Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-04 00:51:18
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/az/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/az/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/az/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/az/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | April 3rd    | `sha256:dda6e60213c831a990e79dd7b10d685139291e7c0c66666c6486535f54325aa0` |
|  `latest-dev` | April 3rd    | `sha256:5a9d6e94b687a22e04e2d82b8524d4578ff379388237826ddfb54dfcfb27c505` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2-dev` `2.59.0-dev` `latest-dev` `2.59-dev` | April 2nd    | `sha256:ed1cda23e371543af3f8c7f97dcba87731940e3adbc17c12d4847e7110040f6e` |
|  `2` `latest` `2.59` `2.59.0`                 | April 2nd    | `sha256:6d72f8bf5b56354d1c3f283d5ba31a8e38051622a4d018df1697999254473e8b` |
|  `2.58.0` `2.58`                              | March 29th   | `sha256:734813223228612022acbdaff720f02863b1d55b8fe5f711edfe5534d9496568` |
|  `2.58.0-dev` `2.58-dev`                      | March 29th   | `sha256:6c09869e1638043d06effba12ef736ade8f6c546f4ceaf794e4a0fd303a02350` |

