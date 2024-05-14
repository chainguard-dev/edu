---
title: "wasmtime Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the wasmtime Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-14 00:46:23
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
|  `latest-dev` | May 13th     | `sha256:d856dc133540c817487c52548d152528f20aa3dbe4b8850db44093c2a4296f20` |
|  `latest`     | May 8th      | `sha256:8833f08266cd7f5e27e976467488857debf5548acd2db9c681558a1919422b59` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `20-dev` `latest-dev` `20.0.2-dev` `20.0-dev` | May 13th     | `sha256:3810e869b63b423df8682aa1d679aa2d837d286d389875f17f5a39444234349c` |
|  `latest` `20.0.2` `20` `20.0`                 | May 7th      | `sha256:297f25c60bd9707f6d64b38e4ca75c4591dec65327f2793635b31b328c799f37` |
|  `20.0.1-dev`                                  | May 3rd      | `sha256:e3d7e58146bff895c099fc105024c68c0f62cd6ff613ede2144a5d064d3c885e` |
|  `20.0.1`                                      | May 3rd      | `sha256:f3df8bc879113c52903b1fc1469d2e9ae67adea1bb622d968121449c5349cd0c` |
|  `20.0.0`                                      | May 3rd      | `sha256:13947da773e5d7ddf1026db8580d993ae9c6f1b85edda5d509bbc0e65e000b87` |
|  `20.0.0-dev`                                  | May 3rd      | `sha256:6c8bc49247dd32c55ce0324fdb38fbe04035eb005fee188eb3491f973907e611` |
|  `19-dev` `19.0.2-dev` `19.0-dev`              | April 21st   | `sha256:6c541973f81c55a8dfe5368d0e40415ff474bd5ee103a96d12ddff8aa8e65559` |
|  `19.0` `19.0.2` `19`                          | April 21st   | `sha256:19084f45e28fdbc883f253e842eadd6df8ce3e5926ac38e096de824a3ff09ac7` |

