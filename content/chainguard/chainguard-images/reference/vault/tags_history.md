---
title: "vault Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the vault Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-14 00:46:23
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
|  `latest-dev` | May 13th     | `sha256:d87ee59c9255fda80d26b72a78640e6581d1ec90b465f65b38104f9bf42f38ff` |
|  `latest`     | May 13th     | `sha256:bf45f1d7fabc6d1ecbe9d1a6378b5a7399827fca33233b685f22247b6a615532` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.14.12` `latest` `1.14` `1`                 | May 13th     | `sha256:3406d62dde3f20fc0d122e4fd7940f06f641c0f4381c51883ff452de6c829f03` |
|  `latest-dev` `1.14.12-dev` `1-dev` `1.14-dev` | May 13th     | `sha256:719d120a5bb45c8b5f89636e77b545a3328eae49368244cc7ff84f366089e9f6` |
|  `1.13.13` `1.13`                              | May 13th     | `sha256:35383fc342a68b25575442fb9e682f569a1eddcf0d8af31fade9d22c17e6b317` |
|  `1.13.13-dev` `1.13-dev`                      | May 13th     | `sha256:b4a6b04fd233119ad1e4790d6fc0bdf76498fdd33fade071bcbab7fb9b4d57f4` |
|  `1.14.11`                                     | April 26th   | `sha256:baa430d699817105639b081708b5bf3326f161308f97e5089e11851ec37c9dc9` |
|  `1.14.11-dev`                                 | April 26th   | `sha256:44281a4b321973f4480aa4be95bb23a048b8386caa19056b0786b9c180f5e0c7` |
|  `1.13.1`                                      | April 25th   | `sha256:4fa1f7cd2a3553f8f19748120b51c9ceea5f2735e67d9ee88bfd16b65513f275` |
|  `1.13.1-dev`                                  | April 25th   | `sha256:8b7f0986cd7d2835c2d3362b1d68e5e9d9837aff3ffeb3a308c3c1d379eb6ef7` |

