---
title: "helm Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the helm Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-20 00:48:18
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/helm/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/helm/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/helm/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/helm/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 17th     | `sha256:b3f2c3d34f05398aed67c7e4bec9178ccc6c065a767434326d9932f5150e6227` |
|  `latest`     | May 17th     | `sha256:7792fa21bdf3fa3bed1cae6a8f4149a4a5e36a1c914fa8e7fc4dc41f997f6944` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `3.15-dev` `3-dev` `latest-dev` `3.15.0-dev` | May 19th     | `sha256:098c2d84cf608ff4cfbb7c660217a19c58536d710f9e4a304ab9a8d289c6c593` |
|  `3.15` `3.15.0` `3` `latest`                 | May 17th     | `sha256:0633a9323f4586173f9220136eed121084d78bd3ab740fc35b5bd37a6ab3ce76` |
|  `3.14.4` `3.14`                              | May 15th     | `sha256:0c177fb85d6a7f3fc6f3de13db8322905b5ddeb2fdea2113a68b5bf5ddcb8bdb` |
|  `3.14-dev` `3.14.4-dev`                      | May 15th     | `sha256:b719b4a6efbece5213320216dc6004777a23a3f73b4cb8b16fe88178525d096f` |
|  `3.11.3-dev` `3.11-dev`                      | May 13th     | `sha256:d19f95e05b32385f5bad1aabd0d3da598752a530f9b0bb9abed33ed96c17bbae` |
|  `3.11.3` `3.11`                              | May 13th     | `sha256:0ea603774d017c1a29e5664a95cfa1eab62906d8f13b2a508a55bf331254a248` |

