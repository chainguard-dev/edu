---
title: "kubectl Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the kubectl Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-23 00:43:06
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/kubectl/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/kubectl/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/kubectl/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kubectl/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 22nd    | `sha256:5a0e20bbf00670e7007ef0ff362b6ff84907ba291af61b3131e76bdac982d399` |
|  `latest`     | June 19th    | `sha256:9949dc16b4e0ca2f18e9823917dbcb07a4c44b8a177c4b254abc379163e81bc5` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `1.30.2-dev` `1-dev` `1.30-dev` | June 21st    | `sha256:e3961939648324eace1499c8f0e3b9a51ab8d2c0c53a123db1aea691d1d04e61` |
|  `1.28.11-dev` `1.28-dev`                     | June 21st    | `sha256:355c31ae956f787d4a769b34a1be04c31a19e415268c2e84cd9484996aa2cb02` |
|  `1.29.5-dev` `1.29-dev`                      | June 21st    | `sha256:18ccc875303679d32f2fac0d8fcc7bd8fbbd0e0d827d43fe1e50c5e47bacc725` |
|  `1.27-dev` `1.27.15-dev`                     | June 21st    | `sha256:eb17686a4da80e1f4677d9c1220d267bba99fbef0319993d90348009a5dacebe` |
|  `1.30` `1.30.2` `latest` `1`                 | June 20th    | `sha256:2365586adc4cb44586e005adb19c692b6eee44fcd90f2e5b03fba679e382329e` |
|  `1.29` `1.29.5`                              | June 20th    | `sha256:bdff2c79e417e79c1bc286c786424870e6e1d40b51a2777ebe5d27411733f77a` |
|  `1.27.15` `1.27`                             | June 20th    | `sha256:d721ea91333757802c50978e7f53b1476e6a3fef6581b8ed3323f0405a21686e` |
|  `1.28` `1.28.11`                             | June 20th    | `sha256:5c89f21dda54d91d0721990e5ae17b6bedb6ec52e3f5b0fe398366a5041aee7c` |

