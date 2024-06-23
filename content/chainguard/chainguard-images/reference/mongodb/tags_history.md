---
title: "mongodb Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the mongodb Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-23 00:43:06
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/mongodb/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/mongodb/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/mongodb/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/mongodb/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 22nd    | `sha256:baffb96570799c9511e3c6937ac2dc7afa9b612f2e1b1f5ee9cb5c2d9a44bce2` |
|  `latest`     | June 22nd    | `sha256:7a6a133ca3ae8afd077decd9533ff975f017c70b6b8608b10e34d7a9bc880208` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                         | Last Changed | Digest                                                                    |
|---------------------------------|--------------|---------------------------------------------------------------------------|
|  `6.0.15` `6` `6.0`             | June 21st    | `sha256:5b14e39bd2ab73c6194f864cf9e7e9c05de9270c82f10c8aa377ed846bfa4a8a` |
|  `6-dev` `6.0.15-dev` `6.0-dev` | June 21st    | `sha256:ea14b3c04b8d5c51ca11902ca13a08672e130a4fca6395bd4b06fbeab54a2847` |
|  `5-dev` `5.0.27-dev` `5.0-dev` | June 21st    | `sha256:1d56bb7e7d48804494fbcb2c15e943cc126df5570e8a4acf0c0a76f1459f9b2c` |
|  `7.0-dev` `7-dev` `7.0.11-dev` | June 21st    | `sha256:257158131c8e34be3d048ac129aab65a5bc898947d43c570048d0920a3c4c389` |
|  `5` `5.0.27` `5.0`             | June 21st    | `sha256:95a7e0cd1f6ef0e36c7e92a6d8b47f080397bb9e8b5eed2cfb41c7c50088ccdd` |
|  `7.0` `7` `7.0.11`             | June 21st    | `sha256:0ebcafb57b481dc7aa94a8f6b0d7b320e8bccc009f38ff0c0a78dd4e36a27d10` |

