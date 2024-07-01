---
title: "loki Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the loki Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-01 00:36:20
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/loki/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/loki/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/loki/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/loki/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 28th    | `sha256:6fc65a41d7c792a4ebb254ad8ade8fb3104e26c9d1bc0c08bd074f5fa9de84ba` |
|  `latest`     | June 25th    | `sha256:5f8fcac1cc7fb2fe7b3b73f85d3da3d8be505b806e9e15959ee4783ad4a8cdf0` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2-dev` `2.9.8-dev` `2.9-dev`              | June 28th    | `sha256:4bf732d42793abfdcd55dee1e0657a03ac2d4685eaf06527a46e6eebffa894a7` |
|  `3.0-dev` `3.0.0-dev` `3-dev` `latest-dev` | June 28th    | `sha256:aa1f74d80e4f023a3b6333a06c3b10b52d7a0121ce0e0adc1161ef385cc3fc09` |
|  `2.9.8` `2` `2.9`                          | June 25th    | `sha256:4868bfeb27e12dd8323fbe5f026a4151be555076a2342c2be24e61125694dce1` |
|  `latest` `3.0.0` `3.0` `3`                 | June 25th    | `sha256:2d587b57338c94f9957e11e3c805dc8e78b4a5894ab7aaac02df6efd6a5c11a5` |

