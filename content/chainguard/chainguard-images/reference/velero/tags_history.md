---
title: "velero Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the velero Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-30 00:52:22
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
|  `latest-dev` | April 29th   | `sha256:17c629792374bce59c80fd218b7bcc2c24f5198301f8de7eae97d9e09b8dfc6c` |
|  `latest`     | April 26th   | `sha256:ee7d85b5e191c5d680dc649235c549d8ba0ef1519ca2630af0ef3050d60f1f0e` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.13-dev` `1-dev` `1.13.2-dev` `latest-dev` | April 29th   | `sha256:ab84e24597dc241a71136d82f05faa69c0669e9a0935ab96d7fff437dfec631c` |
|  `1.13.2` `latest` `1` `1.13`                 | April 26th   | `sha256:4292c194d225e618e87d21b5d251b85e9c4a5e3e6b6e217e589eef28e4933810` |
|  `1.13.1`                                     | April 11th   | `sha256:ecaaa35afc398d0d51919ddc02d92a4468412db2167d45ff303b0a3192d01650` |
|  `1.13.1-dev`                                 | April 11th   | `sha256:3915071decc82caab74ed7639ce8e07d7eea7b46d4464f8bdebd37583fe40dcb` |

