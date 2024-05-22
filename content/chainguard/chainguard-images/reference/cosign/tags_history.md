---
title: "cosign Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the cosign Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-22 00:47:17
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/cosign/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/cosign/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/cosign/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/cosign/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 20th     | `sha256:0d0d8be5c3520fa71503821460bb5978fe2ba2af6215dc092a1fbb15e09254db` |
|  `latest`     | May 17th     | `sha256:b5975777284835c03bf64081f516e40bba77eb352cbc3bc5c7f6d57a5e638274` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2-dev` `2.2.4-dev` `2.2-dev` `latest-dev` | May 21st     | `sha256:8bbe5fbc89df65803bc2da39277a0a624fd235c08726e5c81427f256339390ed` |
|  `2` `latest` `2.2` `2.2.4`                 | May 21st     | `sha256:f1bf5798390945ecb63b5be5c671179bf14143f72bbe808d6d69bad7c336776c` |
|  `2.0.1-dev`                                | April 25th   | `sha256:0f8ffca811eab50fbca70379a3316113075cc46b8a09e880f7d831bdb66f689e` |
|  `2.0.1`                                    | April 25th   | `sha256:1418e13c3479d1a8d068325a97a4a4fbf437d12cb6d5fbfb7160c2f40a239e0b` |

