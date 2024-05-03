---
title: "postgres-operator Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the postgres-operator Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-03 00:45:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/postgres-operator/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/postgres-operator/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/postgres-operator/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/postgres-operator/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 2nd      | `sha256:5d4c689d65437edac8ee01cca2a111251f2e693c7dd0494b8c33e6dc33c82c73` |
|  `latest`     | May 2nd      | `sha256:0cc9a5d861f83065c0a79aaa8c1ae917ac385da788278b7954d0d737eb7186ff` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `1` `1.11.0` `1.11`                 | May 2nd      | `sha256:1b649660e9acdb9219028c27d5f0c21a18ed3d997c0e11ffcba13170951c66f9` |
|  `1.11-dev` `1.11.0-dev` `1-dev` `latest-dev` | May 2nd      | `sha256:98e8e68feaded45acad2cd51fc099c3ebb2c40c97fdb67a64bef6ab07e0b9585` |

