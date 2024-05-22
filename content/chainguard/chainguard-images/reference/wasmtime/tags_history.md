---
title: "wasmtime Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the wasmtime Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-22 00:47:17
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/wasmtime/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/wasmtime/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/wasmtime/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/wasmtime/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | May 21st     | `sha256:abb33b7ffa58c0e59d219f111eedfe4ca8da84ed2675355b1063ad3106dc4b84` |
|  `latest-dev` | May 21st     | `sha256:64e12297d5bc8ba0418e7abfba9ac44097c29526bc1c67418b1b3ff717413370` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `21` `21.0.0` `21.0`                 | May 21st     | `sha256:ac80c557e4363bf88ee9559c2751a593a2a1e06f8840161fa324938d328a68fd` |
|  `21-dev` `latest-dev` `21.0-dev` `21.0.0-dev` | May 21st     | `sha256:b47bdff7ac4c811f087fe5e2230de4f35580b9260a5df8c037f310eeea4410d2` |
|  `20-dev` `20.0.2-dev` `20.0-dev`              | May 19th     | `sha256:e3fde756c36d48b8a840fd769fc6da0183eab2f6f2740a36be8908f95a7fb8af` |
|  `20.0.2` `20.0` `20`                          | May 17th     | `sha256:4b32b618516d7e1d11ea9dbb7e3e6b20a20df621e0cc4d3774167a58feb76347` |
|  `20.0.1-dev`                                  | May 3rd      | `sha256:e3d7e58146bff895c099fc105024c68c0f62cd6ff613ede2144a5d064d3c885e` |
|  `20.0.1`                                      | May 3rd      | `sha256:f3df8bc879113c52903b1fc1469d2e9ae67adea1bb622d968121449c5349cd0c` |
|  `20.0.0`                                      | May 3rd      | `sha256:13947da773e5d7ddf1026db8580d993ae9c6f1b85edda5d509bbc0e65e000b87` |
|  `20.0.0-dev`                                  | May 3rd      | `sha256:6c8bc49247dd32c55ce0324fdb38fbe04035eb005fee188eb3491f973907e611` |

