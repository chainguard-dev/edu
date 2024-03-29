---
title: "fluentd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the fluentd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-28 00:50:32
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/fluentd/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/fluentd/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/fluentd/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/fluentd/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)              | Last Changed | Digest                                                                    |
|----------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev`        | March 22nd   | `sha256:701139ed98eaeafeacbda6b7f0fffdc43cf01906ea989c5c8cf1cd1e2f785062` |
|  `latest`            | March 22nd   | `sha256:4778f2c3fbaa36b75a7312620b808e33e39a86681d3687fd4bebb840e1d767d0` |
|  `latest-splunk-dev` | March 22nd   | `sha256:63f62c3e1aacfe79994026bc7c3ff0560f24648c3771e96009e45e5fb72e2e99` |
|  `latest-splunk`     | March 22nd   | `sha256:22ef20f9513dbcdef64b7ba6c1f1632241042ccc5ad82b8dcfcc12a02246e1b0` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                      | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1` `1.16.5` `1.16` `latest`                                                | March 27th   | `sha256:7668d146bdb97a05000242f169d2329e056ec55ce27d86709b83976f5c083e9a` |
|  `1-dev` `latest-dev` `1.16-dev` `1.16.5-dev`                                | March 27th   | `sha256:60328753b6d03de0f1d89e0b93b166330b15f6d253610213e136a81cf64db755` |
|  `1-splunk-dev` `1.16-splunk-dev` `1.16.5-r0-splunk-dev` `1.16.5-splunk-dev` | March 27th   | `sha256:b06ea625a7f44a056dcdb235ac44bc28ee1fcd0e018fd924519368cec4fc95cd` |
|  `1-splunk` `1.16.5-r0-splunk` `1.16-splunk` `1.16.5-splunk`                 | March 27th   | `sha256:2f3d26c021dd41d0ca74a73ed665cd8ec9e9cf4b68e8e3e1c1b6ec91355e85df` |
|  `1.16.4-splunk-dev` `1.16.4-r0-splunk-dev`                                  | March 27th   | `sha256:3b27787033b3648c3de96fcd0654098ce79a13f43b2ad6d7dc4f80f2d2db32ba` |
|  `1.16.4-dev`                                                                | March 27th   | `sha256:11600998fec349115f2dce10d0676de2604ee2cfe9e5d9af79d99dd0d19a1a1a` |
|  `1.16.4-splunk` `1.16.4-r0-splunk`                                          | March 22nd   | `sha256:c18d359ef44a76b99ed6695ce4b231bc621b56f19d8659c49ae9f46218fb18ad` |
|  `1.16.4`                                                                    | March 22nd   | `sha256:1eb2f9c7c9b9a0fc95f8e2eb516614490790b30dbb8c1b5fc78699386cb7851a` |
|  `1.16.3-r1-splunk-dev` `1.16.3-splunk-dev`                                  | March 14th   | `sha256:0fef6f7c2cd7b2050db62430cfcbda1321040a445611bd45912694c722feb2ba` |
|  `1.16.3-r1-splunk` `1.16.3-splunk`                                          | March 14th   | `sha256:7c8e444a1bd10fe1b2ff2420375ac5a307d06b9063555dc20522cc6725758e6c` |
|  `1.16.3`                                                                    | March 14th   | `sha256:a73b93df29394adca0c321d669efec4d21b1d50ab3e4f19728196a8023b66e2b` |
|  `1.16.3-dev`                                                                | March 14th   | `sha256:12cb8789fef98f45bd4be9de57f7e2974dd2109ae39dbbfe0fe00c7a2a8d447a` |

