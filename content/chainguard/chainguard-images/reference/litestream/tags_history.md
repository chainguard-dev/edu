---
title: "litestream Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the litestream Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-03 00:45:55
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
|  `latest`     | May 2nd      | `sha256:c1b0b2566c2d8c3c6d9486b876c3cf1595c09478f2c565b7f37693479fc77c41` |
|  `latest-dev` | May 2nd      | `sha256:c5c9cbbe62b6ff30f91797d66725444de5256f5e57b1bf07c14c2dbb3937f778` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                      | Last Changed | Digest                                                                    |
|----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0.3.13` `0.3` `latest` `0`                 | May 2nd      | `sha256:0c8e0b8b90c2698f00a128c571c9ccd0908b238e6f477b560363815a39013f8b` |
|  `0.3-dev` `latest-dev` `0.3.13-dev` `0-dev` | May 2nd      | `sha256:5fc4b4b7942ba7ef7f3972b45ba77ce1de40908633b6c8abdab7c7689d063981` |

