---
title: "nemo Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the nemo Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-01 00:36:20
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/nemo/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/nemo/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/nemo/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/nemo/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 28th    | `sha256:d6f813b1c55ad5de1a5c7210c0b362e5de588dfdbe5d58d3830d25199fa57220` |
|  `latest`     | June 28th    | `sha256:fd979fcaa58a5c893ab6f3454cfcee4a9ee249d2ac68e054bb4a5a997c025b72` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `1.23` `1` `1.23.0`                 | June 28th    | `sha256:c668edcff095fc65d67a39c5d0695809429221fc4de0e968261aba2afe2773cf` |
|  `latest-dev` `1.23.0-dev` `1-dev` `1.23-dev` | June 28th    | `sha256:10c5361d8e2593d7198759622d4ada71a15b433a2ef4cb5548b456b7817c9667` |

