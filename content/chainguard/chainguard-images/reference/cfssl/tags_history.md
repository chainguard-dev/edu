---
title: "cfssl Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the cfssl Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-19 00:54:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/cfssl/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/cfssl/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/cfssl/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/cfssl/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | March 18th   | `sha256:e6d96ca3f87fce59edaa385a4d37a85a49d51fdd982e025c899ea0567500a48c` |
|  `latest`     | March 18th   | `sha256:61ddd7b41f220c969f8ba57c5b48f133b5d9d09fe4fa47f9db4802e09df52e41` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.6` `latest` `1` `1.6.5`                 | March 18th   | `sha256:49ac2e9ea02b68bc3eafcff944419a965e922bf4ba0cc3552fddc8fa8f2f8255` |
|  `1.6-dev` `1.6.5-dev` `1-dev` `latest-dev` | March 18th   | `sha256:0f30536632ed6ee351e743284109d399601c3995d363b6adc07cfedf3fe4af20` |
|  `1.6.4-dev`                                | March 2nd    | `sha256:6bb1365ee7004869afbf8c48665e97c7106fcf69cafa58a6c65b2bcfc1523d66` |
|  `1.6.4`                                    | March 1st    | `sha256:0f22b930283055b703dae5fa37506924b8b083ee11e6012964f184072692f9c5` |

