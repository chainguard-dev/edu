---
title: "wazero Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the wazero Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-22 00:47:17
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/wazero/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/wazero/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/wazero/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/wazero/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | May 21st     | `sha256:17d548a9ccc39c5fdea42b0cbd14dd2e57a19018201bf7230b67be244830d852` |
|  `latest-dev` | May 21st     | `sha256:c9cd934b1872bf1ca3c2e46446659e6f1c8fb05cbaea4c906072d7634dfb4176` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1` `latest` `1.7.2` `1.7`                 | May 21st     | `sha256:2c6f25b727ffb135db37a6d3d44c479921d00b6f02275fa9cf78bd382277e249` |
|  `latest-dev` `1.7-dev` `1-dev` `1.7.2-dev` | May 21st     | `sha256:baf3277232f1ba79e82c52d19076694d48d5d3a6394e05756bfd44f5aab3955d` |
|  `1.7.1-dev`                                | May 8th      | `sha256:ef3d5afc152ec35d30a95380e03eb0612675081c5e1146200d5a4ed9010b89e6` |
|  `1.7.1`                                    | May 8th      | `sha256:f24499e05fe5f466f1c3760f9e24101c083042c9a91af401022ba6d200398022` |

