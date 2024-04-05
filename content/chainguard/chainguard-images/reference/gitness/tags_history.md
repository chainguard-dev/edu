---
title: "gitness Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the gitness Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-05 00:47:12
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/gitness/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/gitness/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/gitness/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/gitness/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 4th    | `sha256:62fb9b762165215a2b176a937d88008e1bc85792ece741fc1202530c2a5f0fac` |
|  `latest`     | April 4th    | `sha256:87bd0375ff7994c31f260a6cf70365433b39a335f0f19c9c24e8f1e1ca620a49` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                           | Last Changed | Digest                                                                    |
|---------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `3.0.0_beta6` `3.0` `latest` `3`                 | April 4th    | `sha256:e19fd80ca1ed89d5268d060f83f44f9ce5d04e250952bd5c6e4e91be1f6769c2` |
|  `3.0.0_beta6-dev` `latest-dev` `3.0-dev` `3-dev` | April 4th    | `sha256:57da99aae9931e77f1dea5e48a06e032b13c35824b92d11a54a547db0ce8e0e8` |
|  `3.0.0_beta5-dev`                                | March 28th   | `sha256:f2b14f3832e3d9d519de797e9e1b6118c984640ab152da2a5eedf71cf1fda830` |
|  `3.0.0_beta5`                                    | March 28th   | `sha256:9e45a6ef0329e840054375cd4c136a5d00b1809e4dfa5782c70b1dba53c43c2f` |

