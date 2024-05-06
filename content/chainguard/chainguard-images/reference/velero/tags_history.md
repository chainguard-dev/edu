---
title: "velero Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the velero Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-06 00:43:57
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/velero/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/velero/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/velero/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/velero/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | May 2nd      | `sha256:8795871034f606942d2476363d285118fddf7f3e17e4afb87648eb8f0759a7a2` |
|  `latest-dev` | May 2nd      | `sha256:8120ac553caccaa132c465996ff271995c9b2ea09722b0231c6860e14235989d` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `1` `1.13.2` `1.13`                 | May 3rd      | `sha256:cb37055bfbadd5249b11da84f1679bd756149e419676f904458cae04aa20bc66` |
|  `1-dev` `latest-dev` `1.13.2-dev` `1.13-dev` | May 3rd      | `sha256:fe850d1b2b7fbf2cf21f83b40188fce36f90ad4c88f4a3ecef28e5dc4f2a8f25` |
|  `1.13.1`                                     | April 11th   | `sha256:ecaaa35afc398d0d51919ddc02d92a4468412db2167d45ff303b0a3192d01650` |
|  `1.13.1-dev`                                 | April 11th   | `sha256:3915071decc82caab74ed7639ce8e07d7eea7b46d4464f8bdebd37583fe40dcb` |

