---
title: "prometheus Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the prometheus Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-16 00:33:13
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/prometheus/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/prometheus/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/prometheus/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/prometheus/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | March 15th   | `sha256:81f05c39854ef1df3d5b5386e5cc1df0af3e06d833ebe3f42ae3e8add44cca2a` |
|  `latest`     | March 15th   | `sha256:d2c58a69cbe1f241ab863c3f6394ed9ab327752e572d8c0eed347b4dcdf10408` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed  | Digest                                                                    |
|-----------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `latest-dev` `2.50.1-dev` `2-dev` `2.50-dev` | March 14th    | `sha256:b008457af0b82171745b326dd80a7b914b8e01f5ee2d630dfd34426586da12e3` |
|  `2` `2.50.1` `latest` `2.50`                 | March 14th    | `sha256:3f6728c82f662e55d33dcf1a323547ef27dc88bbb0c924bfa5ce7beec2d79f4e` |
|  `2.50.0-dev`                                 | February 24th | `sha256:218f6f54f1abb6456e5eeac7676fe11a23f8c38e0875353ecb3ed53b9ac65338` |
|  `2.50.0`                                     | February 22nd | `sha256:81809f6ab9abfb88b381631af35826872b10604c0e53b58fdbe54393974d7f19` |
|  `2.49.1-dev` `2.49-dev`                      | February 22nd | `sha256:3ee3f945ed6ac6f624601f3c3a13ec0ea387cb83f697b1e0098ce2255091ac8b` |
|  `2.49` `2.49.1`                              | February 20th | `sha256:91ae010064b3c88a6a392205b9072f075081b9f65523db2713693660d30f8c9e` |

