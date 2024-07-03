---
title: "gradle Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the gradle Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-03 00:33:11
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/gradle/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/gradle/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/gradle/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/gradle/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)   | Last Changed | Digest                                                                    |
|-----------|--------------|---------------------------------------------------------------------------|
|  `latest` | June 28th    | `sha256:98a5ec3ca6231342f096554e71b3f72660c06b442275dcb0465684b575a8c4ab` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-21-8-dev` `latest-dev` `openjdk-21-dev` `openjdk-21-8.8.0-dev` `openjdk-21-8.8-dev` | July 2nd     | `sha256:d94a3c68b177fa22b14c7df7659115c4223fb4c268b2e3c9b6d249ec0913327c` |
|  `openjdk-21-8` `openjdk-21` `openjdk-21-8.8` `openjdk-21-8.8.0` `latest`                     | July 2nd     | `sha256:2e6d5777e2cf88447c73518c0d8e67bce495e68b3e79a9fb066ebc52cdd7c5ea` |
|  `openjdk-17-8-dev` `openjdk-17-8.8.0-dev` `openjdk-17-dev` `openjdk-17-8.8-dev`              | July 2nd     | `sha256:35fafddc0118af445caa7ba135e85b7476727176df8392730facb271d5b0c168` |
|  `openjdk-17-8` `openjdk-17` `openjdk-17-8.8` `openjdk-17-8.8.0`                              | July 2nd     | `sha256:f9bfbbd51c19178f65753cc48e0823b6dffcc2f101a8b69f5a052b036f0c04b4` |

