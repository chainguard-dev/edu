---
title: "bazel Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the bazel Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-25 00:42:19
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/bazel/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/bazel/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/bazel/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/bazel/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 24th    | `sha256:c05b1e18e44d45f6f92d8c5dc7879f58d76bfaa140a53ae335fed00e777df4c0` |
|  `latest`     | June 24th    | `sha256:b3000300fd10f2dc529115f0b796dfeb5653d30a97395932a34e4d85bf6210cf` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `5-dev` `5.4.1-dev` `5.4-dev`              | June 24th    | `sha256:bf4ea70a64b6fb361223445885e43d05df99e673df8e40d1a5b51abe15dc41f1` |
|  `5.4` `5.4.1` `5`                          | June 24th    | `sha256:f03b06c8b922d843f92510568851bcef3230baf78b2f500234fc1dff36905148` |
|  `6.5.0-dev` `6-dev` `6.5-dev`              | June 24th    | `sha256:2eccb1ec7dd186c551ea484fdfbdae7f8987348f1a11114242aeea4ea24db7dd` |
|  `latest-dev` `7-dev` `7.2-dev` `7.2.0-dev` | June 24th    | `sha256:4a2ccc4f894f2c6d7b3bb3556969292b1ea26a0d57efbe7ad2fe65057e49b965` |
|  `latest` `7.2.0` `7` `7.2`                 | June 24th    | `sha256:f0608a7e45f91e7391a83575a0f8143a0da10e80aa8cccc1dcd385bc70410dac` |
|  `6.5` `6.5.0` `6`                          | June 24th    | `sha256:0cc40a64efab791dde2777aa84a16b5f563b7daaa865f0a67f3fadf6e8c90b87` |

