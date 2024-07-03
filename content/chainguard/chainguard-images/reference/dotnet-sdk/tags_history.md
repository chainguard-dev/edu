---
title: "dotnet-sdk Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the dotnet-sdk Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-01 00:36:20
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/dotnet-sdk/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/dotnet-sdk/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/dotnet-sdk/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/dotnet-sdk/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 28th    | `sha256:f0e5c147da6a5a09f7fcb0a8a50be63d948b1fd85fbb80286add9f71c5fb1051` |
|  `latest`     | June 28th    | `sha256:a65520bcd5cf9dce68cbc2b96a53d0b2a2af084295d79b2a54e8c2843ac747e6` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `6-dev` `6.0-dev` `6.0.131-dev`            | June 28th    | `sha256:f1da2a56d021f020faa1dd06f94f80d2741cb97ea246d91882e5b2ac5b517e2e` |
|  `8-dev` `8.0-dev` `8.0.6-dev` `latest-dev` | June 28th    | `sha256:a214ea6727b3ccf28c3fdb637e719de55b821688b8b989c5216eb387dde99644` |
|  `6.0.131` `6` `6.0`                        | June 28th    | `sha256:b3d47aa76783ebc1e0a705dfd33eae06f3134c810519309bf6c8b4a75d5898d0` |
|  `8.0` `8` `8.0.6` `latest`                 | June 28th    | `sha256:2b792b210793cbafb636b2e455fab826eaeeb9ce6a48fd13b8d112901bfb29e8` |

