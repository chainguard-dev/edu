---
title: "bazel Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the bazel Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-27 00:41:27
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
|  `latest-dev` | June 26th    | `sha256:ce43a3a7ace4990025401389593815c99ce6e97c96ccd5198591df36a0df597b` |
|  `latest`     | June 26th    | `sha256:d1c264fcbe91b83dafc773a11d73578563bad0bb0c27c1292d9da287aaed44d8` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `6-dev` `6.5.0-dev` `6.5-dev`              | June 26th    | `sha256:8948e7d8db7a4f737e3c0153c590b598a6ac2193a965b305332811deb6344488` |
|  `6` `6.5` `6.5.0`                          | June 26th    | `sha256:88cede848225447ca7e7b53db0375e6dae58ae870c4c8c577a7218dd5c92a625` |
|  `5.4` `5` `5.4.1`                          | June 26th    | `sha256:1a1dce61b5868e30a8cc6281403cc4a71102ef7f7adf91b0ab80eb577d4f767d` |
|  `latest-dev` `7.2.1-dev` `7.2-dev` `7-dev` | June 26th    | `sha256:ea6d92cae562ee2cdfc8d1423637a06742228a54579d878cae698cf5d22fd718` |
|  `7.2.1` `7` `7.2` `latest`                 | June 26th    | `sha256:7e6c3a82a444a63d9fe21113422ff55ec84bdf9918465956f88c6979ebc576e5` |
|  `5-dev` `5.4.1-dev` `5.4-dev`              | June 26th    | `sha256:19d6e4a5593bec7d340a8b171b4c015729d851e7403eb1f34dfd0b12884530d0` |
|  `7.2.0`                                    | June 24th    | `sha256:f0608a7e45f91e7391a83575a0f8143a0da10e80aa8cccc1dcd385bc70410dac` |
|  `7.2.0-dev`                                | June 24th    | `sha256:4a2ccc4f894f2c6d7b3bb3556969292b1ea26a0d57efbe7ad2fe65057e49b965` |

