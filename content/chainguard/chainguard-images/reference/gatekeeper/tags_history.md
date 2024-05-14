---
title: "gatekeeper Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the gatekeeper Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-14 00:46:23
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
|  `latest-dev` | April 29th   | `sha256:8fda4e163563d17db0f5633bfbc203024b348da4bb4c5ce34876bc91e02de90e` |
|  `latest`     | April 21st   | `sha256:991a66ae28c5cf2cf28d3ab1ae5443aa02e9cf23f83f4e49706236d8299682eb` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `3.15-dev` `latest-dev` `3-dev` `3.15.1-dev` | May 13th     | `sha256:bc2db512a223ebf734b2fa1b9673dd8f399d446a4832232d1af34f269f1f6dac` |
|  `3.12-dev` `3.12.0-dev`                      | May 13th     | `sha256:6721a22ffe9a2d7f0330b473351b324e2705bc6c98e4e38f81577c6031e60d5d` |
|  `3.14.1-dev` `3.14-dev`                      | May 13th     | `sha256:8462eacad8bc5fe2ae31732d06262483427110f34da23bd41b4ef79fdab17f41` |
|  `3.13-dev` `3.13.4-dev`                      | May 13th     | `sha256:d2ed8f707ed119f482790ab3786e4ac77c0d3f6dd107ed8c3cd7e8dc60ae9a79` |
|  `3.15` `latest` `3` `3.15.1`                 | May 10th     | `sha256:39723105addafde8dd7e6178d5c240e83045933165c2fcb1b111aa5c9f40f73d` |
|  `3.12.0` `3.12`                              | May 2nd      | `sha256:d4c50f9a2e52c131e30c06ad7fb4adf0543db21bc3ae2933d24b30c1fb4e92c3` |
|  `3.14` `3.14.1`                              | May 2nd      | `sha256:457fe967007a273dc4f8bbe98f318abddda4ee52c89dcb5f6a0490de5c740f5c` |
|  `3.13` `3.13.4`                              | May 2nd      | `sha256:16cdaf3476e3e3d09dea33c19682984bd8f33eef1d01f6f43c79bfe4f4b39567` |

