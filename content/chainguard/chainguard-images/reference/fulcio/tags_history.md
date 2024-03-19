---
title: "fulcio Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the fulcio Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-19 00:54:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/fulcio/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/fulcio/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/fulcio/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/fulcio/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | March 18th   | `sha256:d4a19bf965d7acb1565c9498440873a63732c46e1402af8b5266bca0db9771be` |
|  `latest`     | March 18th   | `sha256:46cf0941b9f93a37558b2b21dc4c0d45e9bb8b8b052fb9c45994d4898afef497` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed  | Digest                                                                    |
|---------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `1-dev` `latest-dev` `1.4-dev` `1.4.4-dev` | March 18th    | `sha256:0dbf7e46397ae0b6b50004ca3377e6a09698ed707906200ef6357170e0df94c2` |
|  `1.4.4` `1` `latest` `1.4`                 | March 18th    | `sha256:8b246443c8f5e39cf73ca3769976a7ee95abbce822976867b03a15111fbf8807` |
|  `1.4.3`                                    | February 26th | `sha256:d680112957f409a24d72fa539bbc1a4c8af7246ddb9f6f2462b86b97dfb684b5` |
|  `1.4.3-dev`                                | February 26th | `sha256:38b5ccc586bf4eab9c6df844bc8e7063c9da3751a48c496a17d0c2372d979cc3` |

