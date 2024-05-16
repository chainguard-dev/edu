---
title: "yara Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the yara Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-16 00:37:58
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/yara/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/yara/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/yara/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/yara/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 15th     | `sha256:9ad16cd037da9aa81750f1d98bd5f0fe3bef07754f9ae1cca49c54a5a763eaf1` |
|  `latest`     | May 15th     | `sha256:955da502718f368c1138df6bda6d1318073ae30167a1c483757f257c37f4228c` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `4-dev` `4.5-dev` `4.5.0-dev` `latest-dev` | May 15th     | `sha256:434f2e2a5c5035270b12be870c381d2eca95f7fb0b0c1f79c5298a8d39c3e26d` |
|  `4.5` `latest` `4.5.0` `4`                 | May 15th     | `sha256:9b9debc84c6868de1e30aba0a046631bd6f901d45561a5efc6f107f653f139c5` |

