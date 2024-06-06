---
title: "fluent-bit Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the fluent-bit Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-06 00:48:16
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/fluent-bit/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/fluent-bit/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/fluent-bit/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/fluent-bit/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 5th     | `sha256:a343ca0d1968edab6fe153da8d31ea716ff673a11752dcfb6805782aaad4e19e` |
|  `latest`     | June 5th     | `sha256:dd69b2726a4b978771eb01bb79440a57d06ccd25f7995ea63081c3e4e21350e1` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `3.0.6-dev` `3-dev` `3.0-dev` | June 6th     | `sha256:59ef1cfb70913a7fab8e88d1eb0aaec7c4fc3a64606f688eebfd85c40cfe11f1` |
|  `2.2.3-dev` `2.2-dev` `2-dev`              | June 6th     | `sha256:9f3b3cf62c9fef18099a9dc7c6dae9fb47918ccd768bb503eabe3da3ef4c8d68` |
|  `3.0` `3` `3.0.6` `latest`                 | May 30th     | `sha256:1b8de36663467cc73021411d9c3fb224ffd05c7b16c16b473f64d796fff9437d` |
|  `2.2.3` `2.2` `2`                          | May 30th     | `sha256:b1a6b4b5c9b120f151120623e4ed4a9997d61e5f9bd286e5c1cf3c9ee1b29ecd` |

