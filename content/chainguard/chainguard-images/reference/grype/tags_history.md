---
title: "grype Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the grype Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-24 00:43:49
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/grype/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/grype/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/grype/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/grype/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 22nd    | `sha256:5324b666c7fa296fe9aae5fac732f209f61158e042e4f2962ac2a0bb468b0dfa` |
|  `latest`     | June 19th    | `sha256:bd7413c543cf5553ea0dde655cc94e51d20f392af917a483c6b173979da6f900` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0.79-dev` `latest-dev` `0.79.1-dev` `0-dev` | June 23rd    | `sha256:ea21fb0aa3d8c2e4b0534d3bf678bdf86734d800e6d4659550076e9c390a6ed2` |
|  `0` `0.79.1` `0.79` `latest`                 | June 20th    | `sha256:22971ee8467c0b26339bba7918ee7a578095a4236f335b4c4bd44d1f07cebd6c` |

