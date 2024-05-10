---
title: "etcd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the etcd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-10 00:43:45
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
|  `latest`     | May 8th      | `sha256:e0e20b61d65921831c1d47889724b27509df747c854960fd5e7d71b2c5a9bc7a` |
|  `latest-dev` | May 8th      | `sha256:9a29ac843c4f37e6f1ec6886bd6f6d3f13fa77c66d1dfd818fe5ea6caaad041a` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                      | Last Changed | Digest                                                                    |
|----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `3.5-dev` `latest-dev` `3.5.13-dev` `3-dev` | May 9th      | `sha256:bdebc894b3a96dd8a1ca7de26fff6d746557b5c8bcc7dcc74076be7e56e2d483` |
|  `latest` `3.5.13` `3` `3.5`                 | May 9th      | `sha256:43b93f50ab25e41b7ccb34683ee340d4c98e1b7ac9506e630ea383c3d20ab879` |
|  `3.4-dev` `3.4.32-dev`                      | May 2nd      | `sha256:9639288e7c5342fb37f6db85059d1d6a6f3839f216910d8fa33f067bd0bd02d4` |
|  `3.4` `3.4.32`                              | May 2nd      | `sha256:4a64a05939cfe56cfa3907d67d387c1f8f25931e11b242398fca36b200ff22dd` |
|  `3.4.31`                                    | April 21st   | `sha256:5d8abbcfb187978ef20eaca3d2b18382debc0f9e4095113a82136db41e34c04a` |
|  `3.4.31-dev`                                | April 21st   | `sha256:20d7842e9556329750de78172129f388f124a41b10aa679d691d01eec64eecd7` |

