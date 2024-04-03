---
title: "gatekeeper Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the gatekeeper Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-03 00:49:16
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/gatekeeper/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/gatekeeper/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/gatekeeper/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/gatekeeper/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 2nd    | `sha256:36efbaac6b58323ba845c2fa1bedf174c4156800e1e1a38f0b74c8a572271bdb` |
|  `latest`     | March 18th   | `sha256:5771bc5fb2f7cfa3d0a71970267460ce0af9061e49c5e5419ce48f92245c254f` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `3-dev` `3.14-dev` `3.14.1-dev` `latest-dev` | April 2nd    | `sha256:f344d3c7aea0e8155637fc2630800580b06bab71a5fccc57a5ae1aa4a0cee45c` |
|  `3.12.0-dev` `3.12-dev`                      | April 2nd    | `sha256:6064f1439cd27a6fe86496deb1d438104b2b956e31346b5fefe6d55fff463def` |
|  `3.13-dev` `3.13.4-dev`                      | April 2nd    | `sha256:be134997d690e771912926124afc1f81797b789f2880d412202d01d8c8bae623` |
|  `3.12.0` `3.12`                              | March 28th   | `sha256:af9b04e5d7af2813e171c951cd3998651dd8bf3ce1359e731c98e9e64d3c9884` |
|  `3.14.1` `3` `latest` `3.14`                 | March 28th   | `sha256:93ee8aac2b0ffcf66dfae1ff6b31b25e668924035883747b4ba804367a647f37` |
|  `3.13` `3.13.4`                              | March 28th   | `sha256:55fb1ba8d5860f4915d9465365169e2ad42b0ccb48373139ecf38018ebb9fdc5` |
|  `3.14.0-dev`                                 | March 12th   | `sha256:b4b3ef5c89c9f443b9f12a2199c3c4dffb1260770cb5c30f8d0f8dd33eca2eb1` |
|  `3.14.0`                                     | March 8th    | `sha256:60eb7d52e5c4c4d8c92191863c96dbd49b2da96da1b685bc3909cb518456e85c` |

