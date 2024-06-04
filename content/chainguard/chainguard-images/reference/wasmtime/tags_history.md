---
title: "wasmtime Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the wasmtime Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-04 00:50:16
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
|  `latest-dev` | June 1st     | `sha256:aa22e36b6b3bc58f82920c1869a063fdda131946f2b5cb2ad52d91d7cfe6cc40` |
|  `latest`     | May 23rd     | `sha256:1a025829c48b1fb2d8c7b9292681bb42fe2385954ebadc80cd6c9c578f8d6270` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `21.0-dev` `21-dev` `21.0.1-dev` `latest-dev` | June 1st     | `sha256:2b0c90bb4b88103015744aecc704aad0cd2e11dba4c90425eae3642a5c84af23` |
|  `21` `21.0` `latest` `21.0.1`                 | May 23rd     | `sha256:832d1fffe22f09240224826d8677ae67be094db6848d63e3f7681473bce328b5` |
|  `21.0.0-dev`                                  | May 22nd     | `sha256:b4aba5a64fb7389b7b712c8329d6e520cb93f2db883ef9aa05d0af5d930dd6c6` |
|  `21.0.0`                                      | May 21st     | `sha256:ac80c557e4363bf88ee9559c2751a593a2a1e06f8840161fa324938d328a68fd` |
|  `20-dev` `20.0.2-dev` `20.0-dev`              | May 19th     | `sha256:e3fde756c36d48b8a840fd769fc6da0183eab2f6f2740a36be8908f95a7fb8af` |
|  `20.0.2` `20.0` `20`                          | May 17th     | `sha256:4b32b618516d7e1d11ea9dbb7e3e6b20a20df621e0cc4d3774167a58feb76347` |

