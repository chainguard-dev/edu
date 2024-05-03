---
title: "etcd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the etcd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-03 00:45:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/etcd/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/etcd/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/etcd/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/etcd/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | May 2nd      | `sha256:d18ec3b57ad3b5e28fb803e9095a560cdd80348f9d29027edd2640dfbd34e5e3` |
|  `latest-dev` | May 2nd      | `sha256:eeebd8ea5215ade00cd9714c4a77155c06e0ebce6d3eeaa135ebf60d4f54954d` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                      | Last Changed | Digest                                                                    |
|----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `3.5-dev` `3-dev` `latest-dev` `3.5.13-dev` | May 2nd      | `sha256:d4c39b35a71c00f9f722d8bd11915ea59daaf2282a41d037362a1b9b29a6ed09` |
|  `3` `latest` `3.5` `3.5.13`                 | May 2nd      | `sha256:f64b8d014af72c05863ff8abe5ab1e5f223f96d8fc41f6403e677aeb9e733184` |
|  `3.4-dev` `3.4.32-dev`                      | May 2nd      | `sha256:9639288e7c5342fb37f6db85059d1d6a6f3839f216910d8fa33f067bd0bd02d4` |
|  `3.4` `3.4.32`                              | May 2nd      | `sha256:4a64a05939cfe56cfa3907d67d387c1f8f25931e11b242398fca36b200ff22dd` |
|  `3.4.31`                                    | April 21st   | `sha256:5d8abbcfb187978ef20eaca3d2b18382debc0f9e4095113a82136db41e34c04a` |
|  `3.4.31-dev`                                | April 21st   | `sha256:20d7842e9556329750de78172129f388f124a41b10aa679d691d01eec64eecd7` |

