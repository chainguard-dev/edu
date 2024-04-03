---
title: "flux Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the flux Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-03 00:49:16
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/flux/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/flux/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/flux/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/flux/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 2nd    | `sha256:b678baca52a34e7a89af2810dce58ccc6d73ba3647f8f1ccf0079b803a41c0fe` |
|  `latest`     | April 1st    | `sha256:ff47a87924c99fb103e4e491d8f849508cbaf9235e79d279ae404cabc7fe8c3d` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2-dev` `latest-dev` `2.2-dev` `2.2.3-dev` | April 2nd    | `sha256:bbf2c89fe993f81a506eb3cc967008422ac262d585ee0bbc6c8f89aa6e1b0208` |
|  `2` `latest` `2.2.3` `2.2`                 | April 1st    | `sha256:d0b39c7e0146c0056caf7cb11ba8f344d13c80624c36e7955d0dafe2cd26ef12` |
|  `2.0.1-dev` `2.0-dev`                      | March 18th   | `sha256:450718cfc4046e79d088812a0f0f41c843a0f2f2bc81bca9338248f0d698acdc` |
|  `2.0.1` `2.0`                              | March 18th   | `sha256:d61ee022c0891cc78882e60aa2cb1a2ed1ce6e42aff5a5d6df3502904faa27e3` |

