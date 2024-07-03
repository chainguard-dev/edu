---
title: "node-lts Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the node-lts Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-01 00:36:20
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/node-lts/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/node-lts/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/node-lts/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/node-lts/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)                  | Last Changed | Digest                                                                    |
|--------------------------|--------------|---------------------------------------------------------------------------|
|  `next-dev` `latest-dev` | June 28th    | `sha256:ec88a69cbf4f4d227b69e7692e959b8412cc41e4033bad7076996f9f12a6e01b` |
|  `next`                  | June 28th    | `sha256:8683cb055a76b9fd4621721acef7e0e838feec5d35f26ebc5a0f5637ca850745` |
|  `latest`                | June 28th    | `sha256:437a945409c1f9ad96884d8373f3021631502ed379d25501f659ce8e929da2ac` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                     | Last Changed | Digest                                                                    |
|-------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `20.15.0-dev` `latest-dev` `next-dev` `20.15-dev` `20-dev` | June 28th    | `sha256:c11a63f209bb02820b80a1642bd1e4a93cdeed1dc8f2da67bf3ae103649543df` |
|  `20.15.0` `20` `20.15` `latest`                            | June 28th    | `sha256:c2953fba1b64856ecfc0645b746f5cccfc7baa2857532f604713775455f38978` |
|  `next`                                                     | June 28th    | `sha256:ab8a95c79d8b91203e8f5d06db79def96def1ce11810da81e9b5f346597e8f8a` |

