---
title: "harbor-registry Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the harbor-registry Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-21 00:38:36
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/harbor-registry/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/harbor-registry/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/harbor-registry/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/harbor-registry/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 20th     | `sha256:51d4bc5bd645d6be913098d0d2d0a21cbea850b63932daed0cb8d0bf20d72a14` |
|  `latest`     | May 17th     | `sha256:eff205ec2a1fb4530020e97aaef43b98c3c3da3d5aa5090a60ebef87a2c61aaa` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                            | Last Changed | Digest                                                                    |
|----------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `3.0.0_alpha1-dev` `3-dev` `latest-dev` `3.0-dev` | May 19th     | `sha256:6e7a4517441a3184dc3282e50f3b711dc48d3cb856c5dfe3a994937d11405236` |
|  `3.0.0_alpha1` `3.0` `3` `latest`                 | May 17th     | `sha256:0f9a607101cb258671d256a4eafecd81e33887f4d66b2c22df1c1dc0b64c3d4d` |

