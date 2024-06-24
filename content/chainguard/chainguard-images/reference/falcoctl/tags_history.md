---
title: "falcoctl Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the falcoctl Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-24 00:43:49
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/falcoctl/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/falcoctl/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/falcoctl/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/falcoctl/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 22nd    | `sha256:4222dbe62d7ec50895ed28fa3a55e5597b2c000cabb77ff7b0aed57342e98be0` |
|  `latest`     | June 20th    | `sha256:00f2fca7cfda650798a6a2d1422857dfade8fd2de30f4f0c426281546c755bd6` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0.8.0-dev` `0-dev` `0.8-dev` `latest-dev` | June 23rd    | `sha256:12adc21a7d7c6aadac6ed57319d6869ee22a7e12a88693ba98d43f367752e4e2` |
|  `0.8.0` `0` `latest` `0.8`                 | June 20th    | `sha256:ff7494ba331b596e6e69244b58f0467cf12b57a920d1ce61450529f040c34216` |

