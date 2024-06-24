---
title: "opentelemetry-collector Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the opentelemetry-collector Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-24 00:43:49
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/opentelemetry-collector/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/opentelemetry-collector/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/opentelemetry-collector/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/opentelemetry-collector/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 22nd    | `sha256:c884912f3c56bf4d9ecb2c82b0929f657c0513e437b71fa833f5b1a7270ef190` |
|  `latest`     | June 19th    | `sha256:9609f2a0fcb2a59ff4de3f2e93f739b953b100ffa489391f01c6e62ab9fd3933` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                         | Last Changed | Digest                                                                    |
|-------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0.103-dev` `latest-dev` `0.103.0-dev` `0-dev` | June 23rd    | `sha256:ffc5a588400bb0183c64a04d8c6d5811dd3a8f326762b809969e206a0c78eb50` |
|  `0.103.0` `0` `0.103` `latest`                 | June 20th    | `sha256:0e553ce2c0f4d5c9058b34ea2727ef3cdd556037ab27f8d4ebcb9aca543d4d70` |
|  `0.102-dev` `0.102.1-dev`                      | June 18th    | `sha256:7b622776a3188cdd061ffe7135549673908c52f2f4b775eac1e21cfe60a961e6` |
|  `0.102.1` `0.102`                              | June 18th    | `sha256:7dce56fbc3caa7d4861dcc73f9953ec95781f896a46e176f84cc11d310a9250c` |

