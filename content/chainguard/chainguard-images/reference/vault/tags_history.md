---
title: "vault Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the vault Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-27 00:43:34
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/vault/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/vault/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/vault/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/vault/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 23rd     | `sha256:9766fae06730a4cab5a60260350c8fc492418ef1b180abef476a6e1e364639d6` |
|  `latest`     | May 23rd     | `sha256:4dabb4da4d1ed6c907a66a3a36bfbc9e55a6e5ff083a3d7447f2fbd18a369f88` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.14.12-dev` `1.14-dev`                     | May 24th     | `sha256:5422efd6c2cb7e1d9b8423e215b34e59d6346a86de3e6a3302fbe10715b816f1` |
|  `latest-dev` `1-dev` `1.16-dev` `1.16.2-dev` | May 24th     | `sha256:71309af8d600e08b10e8dfa013fd0924b2911b29fe38b6faa8731aa2eaae06e9` |
|  `latest` `1.16.2` `1.16` `1`                 | May 24th     | `sha256:4dcb9e16d87bd56c9d01d2b1014c998bac476a263c5ec8e7f4e79055bd4cbae1` |
|  `1.15` `1.15.8`                              | May 24th     | `sha256:b905fd40ddbfa212d70bafb7d6b79e3ec890f674907d47ac1dca84910c9a33ed` |
|  `1.15-dev` `1.15.8-dev`                      | May 24th     | `sha256:15ced5a729ffb55d1cf15499c92f23915641e81bec88c120e1dda63be14b01a7` |
|  `1.14.12` `1.14`                             | May 24th     | `sha256:c57ea2ac3e68ec244e864b090a1fbfb5e7da5ba6af728ce5edb72a2788f328ea` |
|  `1.13-dev` `1.13.13-dev`                     | May 14th     | `sha256:f07262ce87225366516a80bb5ed890a173a8f2c0ee1ec69e613b4071d88280e3` |
|  `1.13.13` `1.13`                             | May 13th     | `sha256:35383fc342a68b25575442fb9e682f569a1eddcf0d8af31fade9d22c17e6b317` |

