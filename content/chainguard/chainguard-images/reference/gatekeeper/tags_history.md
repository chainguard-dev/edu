---
title: "gatekeeper Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the gatekeeper Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-06 00:47:02
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

| Tag (s)       | Last Changed  | Digest                                                                    |
|---------------|---------------|---------------------------------------------------------------------------|
|  `latest-dev` | March 1st     | `sha256:02d6ed37dd1b5d3a35906570bde3732ac6542fd0f41d609dea544d0cec66ace6` |
|  `latest`     | February 27th | `sha256:8a3b1f68fd30b2952a9dbcbc7ec8c9fdc760706cc6ebaef290d91e04f2e3ada7` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed  | Digest                                                                    |
|-----------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `3.12-dev` `3.12.0-dev`                      | March 5th     | `sha256:9e054bca14928ae79f7f8d66fd0dabfdb44451e87ff9c32476fbea20696709f4` |
|  `3.12` `3.12.0`                              | March 5th     | `sha256:f7e51dd5e386a33ac1c401c5b17c8ac979f7e9e3a36df63f2178f37f0dde7d42` |
|  `3.13.4-dev` `3.13-dev`                      | March 2nd     | `sha256:c51cee65689777b0d854448b2fa6488168cd7bb66f712f4221d834dc815502c0` |
|  `3.14-dev` `3-dev` `3.14.0-dev` `latest-dev` | March 2nd     | `sha256:b7f41ebf64a9932f3c93ba05c952433322bd4edb24ae0b77a728c95cbf4de34b` |
|  `3.14` `3.14.0` `latest` `3`                 | February 26th | `sha256:31338ae4eba8284f6561d72f26b4dc316ba2de806b69e10045087edd912ab50a` |
|  `3.13.4` `3.13`                              | February 26th | `sha256:94b7391bbc9dc29a3797788b6ac41a7091c4775fc16ba645b9d2e964803bc6db` |

