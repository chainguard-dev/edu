---
title: "kubectl Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the kubectl Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-26 00:35:03
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
|  `latest-dev` | June 24th    | `sha256:1844665fa77283d26923b2afe225f0d6adec6e08f1beb4e667db4b39e6ae165e` |
|  `latest`     | June 19th    | `sha256:9949dc16b4e0ca2f18e9823917dbcb07a4c44b8a177c4b254abc379163e81bc5` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.27.15-dev` `1.27-dev`                     | June 25th    | `sha256:d5e870c6c68c05ab5273127247a3524af31af6cbaf0515d6b47aabc0fa9cb758` |
|  `latest-dev` `1.30.2-dev` `1.30-dev` `1-dev` | June 25th    | `sha256:d2dfb335ae963535e1f868fce7e8ee9f9571636605083b6a0d79d4414ce38920` |
|  `1.28-dev` `1.28.11-dev`                     | June 25th    | `sha256:99cc69000c52fb74b45e6c49b63a8897c564c88ca8968e31aef1cbb2d1b7f3b5` |
|  `1.29.5-dev` `1.29-dev`                      | June 25th    | `sha256:000db2a40f2d0ddfb167531eeede1eca44c6a88dc8982f808a8802a00b425159` |
|  `1.30` `1.30.2` `latest` `1`                 | June 20th    | `sha256:2365586adc4cb44586e005adb19c692b6eee44fcd90f2e5b03fba679e382329e` |
|  `1.29` `1.29.5`                              | June 20th    | `sha256:bdff2c79e417e79c1bc286c786424870e6e1d40b51a2777ebe5d27411733f77a` |
|  `1.27.15` `1.27`                             | June 20th    | `sha256:d721ea91333757802c50978e7f53b1476e6a3fef6581b8ed3323f0405a21686e` |
|  `1.28` `1.28.11`                             | June 20th    | `sha256:5c89f21dda54d91d0721990e5ae17b6bedb6ec52e3f5b0fe398366a5041aee7c` |

