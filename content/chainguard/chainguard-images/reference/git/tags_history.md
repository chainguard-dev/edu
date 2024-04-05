---
title: "git Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the git Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-05 00:47:12
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/git/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/git/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/git/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/git/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)                  | Last Changed | Digest                                                                    |
|--------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-root`           | April 4th    | `sha256:2f99eac5be0edab2842e2483bd6c1b1b4634fc49e9b86ad465845af879d2b5dd` |
|  `latest`                | April 4th    | `sha256:bf24c033af68f8a0a3477f0b5541f41cdea884311c721f25edf4d078c384e0a1` |
|  `latest-dev`            | April 4th    | `sha256:1b89042e504fac9d8b3802561a8b0d5f1915474899dda577940a4b41a7435b13` |
|  `latest-root-dev`       | April 4th    | `sha256:eae7a562e9db3e29e81d3fc33b510a8f21d9b196771b091d21144d2bff1646f5` |
|  `latest-glibc-root-dev` | April 4th    | `sha256:153c53ad36ce3d006cb986491fde2b30c107e5c6fdedfe14913f88b34e4d0f92` |
|  `latest-glibc`          | April 4th    | `sha256:63edd43a2d06016e5da7b0760413d8066b7a69b29165e3c3c0b0d1156df974da` |
|  `latest-glibc-dev`      | April 4th    | `sha256:e3c26717e68b41e51d654b177be41007927b8f1366f478dc56530c8f3894026b` |
|  `latest-glibc-root`     | April 4th    | `sha256:0f3db74b3b1cf5d97e92b19f92f3feb08e363ce74479e6e1271976ecfa0ca8dd` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                   | Last Changed | Digest                                                                    |
|-------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-glibc-root-dev` `glibc-root-2-dev` `glibc-root-2.44-dev` `glibc-root-2.44.0-dev` | April 4th    | `sha256:f86d5b6d487eaeaaba7c3011989afff95aa8590d2cc1aee9c5ae5d647c405aea` |
|  `latest-glibc-root` `glibc-root-2.44` `glibc-root-2` `glibc-root-2.44.0`                 | April 4th    | `sha256:e1f52601d3690bd8805b57feb88cbb9459f794db468334f43bf48d2ebfc5ca3d` |
|  `glibc-2.44.0-dev` `glibc-2.44-dev` `glibc-2-dev` `latest-glibc-dev`                     | April 4th    | `sha256:9bcb653ba6c508d89408bdfe7d2d68c14f5eed8998eb264b7476ae3637942953` |
|  `glibc-2.44` `glibc-2.44.0` `glibc-2` `latest-glibc`                                     | April 4th    | `sha256:b997fdd2d1b17174dd47bda5ea71f46d7492d1d087924302d383bce895fab9d5` |

