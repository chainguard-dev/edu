---
title: "cosign Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the cosign Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-01 12:14:22
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/cosign/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/cosign/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/cosign/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/cosign/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed  | Digest                                                                    |
|---------------|---------------|---------------------------------------------------------------------------|
|  `latest-dev` | February 27th | `sha256:f6cb952ea25eb0ca1fc80ec3d146475dee14af705d4f513e894039c3d4b6a1cc` |
|  `latest`     | February 27th | `sha256:c9afd56fcad447ff35ba7859ad9015ff7ff22738169028ea78b74c0ca3b2555c` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed  | Digest                                                                    |
|---------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `latest` `2` `2.2.3` `2.2`                 | February 26th | `sha256:e9c1e96dbc7d07aec090c112467a7b31e3cbabde087c721a4efcd6d4641ed56f` |
|  `latest-dev` `2.2-dev` `2-dev` `2.2.3-dev` | February 26th | `sha256:7383dde7d4f8afb0c66a8c4f11d30d0dec1a877c00a24c19805ab21774b8c8f4` |

