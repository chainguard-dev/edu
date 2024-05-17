---
title: "grype Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the grype Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-17 00:44:46
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/grype/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/grype/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/grype/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/grype/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 16th     | `sha256:6cf2ab6f1d0b78028a5527fcf5dd1a6174707ac184c0d2d97bda8cd2732843a0` |
|  `latest`     | May 15th     | `sha256:9ba307ba02c0b267b79e47caffffe34cb5256dd93a1eb1197e4ee53a6bcfdb47` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0-dev` `latest-dev` `0.77.4-dev` `0.77-dev` | May 16th     | `sha256:92d41faad718e7c60269b63863d4f8cc1e1ee6e832da5088698193c034692a0e` |
|  `0.77` `latest` `0` `0.77.4`                 | May 15th     | `sha256:dae0fb1234b7e9782cf0ce64a80c8a6e7f5f9eb20355159b8f3b447f309068bd` |
|  `0.77.3-dev`                                 | May 10th     | `sha256:e1b42bc5ed7bef8e05a4d586278175e3f9da60a1c117aa6609273b339f1d3190` |
|  `0.77.3`                                     | May 10th     | `sha256:1983c77db21053d04fcd3ff46f40db5fbfaa3852b77f1932dab0873f909a18c8` |
|  `0.77.2`                                     | May 2nd      | `sha256:5110e7eb6eb7aad915a9e6f743e949d4ebef5d8d6e4d67862bd7021a5d0e30d7` |
|  `0.77.2-dev`                                 | May 2nd      | `sha256:bba1ddf52bae26bcae36d01809103548c4d7bb62ef2a76129b8f57a945c1f362` |
|  `0.77.1-dev`                                 | May 1st      | `sha256:0f9ee9c83dc3b8920cf49bc2a145ee9d09f8da647bf024583cbd5a5daf328a8e` |
|  `0.77.1`                                     | May 1st      | `sha256:d843569f324eee5bb52a1b20405444b0ebb4cd08fe36671c220ed59277a4680f` |
|  `0.77.0-dev`                                 | April 21st   | `sha256:341638335599028da312b6e765de204b84f39028fabe375fc5342f71b8a75ef0` |
|  `0.77.0`                                     | April 21st   | `sha256:0a1622f25939eb8b7218266f5372711ae7c171504538c7cc24cfbe0ce2a6e8fc` |

