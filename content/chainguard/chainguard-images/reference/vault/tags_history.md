---
title: "vault Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the vault Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-24 00:45:45
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
|  `1.14-dev` `1.14.12-dev`                     | May 23rd     | `sha256:4a762d38899e93fe084434a55345c2e68dd84fdb634926a4ec41d2d447480e94` |
|  `1.16-dev` `1-dev` `latest-dev` `1.16.2-dev` | May 23rd     | `sha256:ed74f79b288b14fe7cfffa526f6823fda920555f35593c07a4c4351c8731f61f` |
|  `1.15.8-dev` `1.15-dev`                      | May 23rd     | `sha256:886afda19e8d472af1f2fb9551d11efec30a6a4349ca481c37420d62757bf93e` |
|  `latest` `1` `1.16` `1.16.2`                 | May 23rd     | `sha256:1ca4293d420049a755acaa0efe293ae51b9cb5a0f334d935cde31d5856e4ea46` |
|  `1.15` `1.15.8`                              | May 23rd     | `sha256:bb393f3837d4d32f715951105b54551526e28b10727666c8e3f0bc0feefd88f7` |
|  `1.14` `1.14.12`                             | May 23rd     | `sha256:8f634f980f0d30859ec673dea4cc7efaf65763f51ce49f9cb0eb7591c48cc6f9` |
|  `1.13-dev` `1.13.13-dev`                     | May 14th     | `sha256:f07262ce87225366516a80bb5ed890a173a8f2c0ee1ec69e613b4071d88280e3` |
|  `1.13.13` `1.13`                             | May 13th     | `sha256:35383fc342a68b25575442fb9e682f569a1eddcf0d8af31fade9d22c17e6b317` |
|  `1.14.11`                                    | April 26th   | `sha256:baa430d699817105639b081708b5bf3326f161308f97e5089e11851ec37c9dc9` |
|  `1.14.11-dev`                                | April 26th   | `sha256:44281a4b321973f4480aa4be95bb23a048b8386caa19056b0786b9c180f5e0c7` |
|  `1.13.1`                                     | April 25th   | `sha256:4fa1f7cd2a3553f8f19748120b51c9ceea5f2735e67d9ee88bfd16b65513f275` |
|  `1.13.1-dev`                                 | April 25th   | `sha256:8b7f0986cd7d2835c2d3362b1d68e5e9d9837aff3ffeb3a308c3c1d379eb6ef7` |

