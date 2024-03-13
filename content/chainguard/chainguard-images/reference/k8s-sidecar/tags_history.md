---
title: "k8s-sidecar Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the k8s-sidecar Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-13 00:52:18
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/k8s-sidecar/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/k8s-sidecar/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/k8s-sidecar/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/k8s-sidecar/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | March 12th   | `sha256:28c06f6a6bad1080405bac8dff6d3c83fee8f47965ff134cea6210953cc52932` |
|  `latest`     | March 12th   | `sha256:5ae2f9528147c580c2c4b689b0e77cd427d423a31b195076ac076bfb83501372` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed  | Digest                                                                    |
|-----------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `1-dev` `1.26.1-dev` `1.26-dev` `latest-dev` | March 13th    | `sha256:ba87794a8b68600d823784590866381cc834fb8a000364d2654e30d3187690ee` |
|  `1.26.1` `1` `1.26` `latest`                 | March 13th    | `sha256:dbb41ddf912d4b586afc45188807a53ef41b5110794d36a6c846ca2898e0de1a` |
|  `1.26.0-dev`                                 | March 2nd     | `sha256:fbfacc2f5ca90fbc0933e95b1354a7e397d83b81938181261f498a453c72672d` |
|  `1.26.0`                                     | March 1st     | `sha256:fa244bba955ff2419b401e83fb062f6d2d0e4db5f2955126a71dd866a6847852` |
|  `1.25.6` `1.25`                              | February 26th | `sha256:5122e92c38b77df2933f06cded201ccbeac376adf2e49e3aae8d9d78c289912c` |
|  `1.25-dev` `1.25.6-dev`                      | February 26th | `sha256:44af9bfeecd1695c69475a71a860e7c399f2b65170dd962a2e6d67f0b4f31ce5` |
|  `1.25.4-dev`                                 | February 24th | `sha256:fc502b83eb2a58e1b6c259ced16bcd97fdd68b1964695d01bece450e5996626e` |
|  `1.25.4`                                     | February 24th | `sha256:9cce6c67c785997a2dd1842c08271b93bd0711281b7c91eab8876b5874f5061d` |

