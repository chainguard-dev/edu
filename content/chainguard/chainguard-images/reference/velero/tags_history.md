---
title: "velero Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the velero Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-02 00:36:12
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
|  `latest`     | April 1st    | `sha256:7c09e7371717163bba24106419416482fd810506a9474ae8d719ff4f6d051921` |
|  `latest-dev` | April 1st    | `sha256:4bf2c11e87e1783d4fcb010fc9beadbd84d05551467ef89769cde87d4dea409f` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.13` `1.13.1` `1` `latest`                 | April 1st    | `sha256:91872bcc2be75934411cc69ffd24db4ef3d87db6cca6df1f86ba31e4c9a1e03f` |
|  `1.13.1-dev` `1-dev` `1.13-dev` `latest-dev` | April 1st    | `sha256:13a02874c0b0513eb83edf18ff5279063e8403368d6ea96124a64c1c1079de41` |

