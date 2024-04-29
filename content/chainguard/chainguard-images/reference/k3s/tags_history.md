---
title: "k3s Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the k3s Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-29 00:53:42
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/k3s/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/k3s/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/k3s/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/k3s/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 26th   | `sha256:16e3fb2a29194fab66de4e0793d09995ff8dcd162a3fa66f2eb2e70d740d3d38` |
|  `latest`     | April 26th   | `sha256:1dd18987ffa4b383cf969c20c534d4fcb667e6a0801d41917c99a2c34c192557` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.29` `1` `latest` `1.29.3`                 | April 26th   | `sha256:7d77d497ef31e57d802a52636fb315a1e948eaa049d04edee04caf1977d85ab8` |
|  `latest-dev` `1.29.3-dev` `1-dev` `1.29-dev` | April 26th   | `sha256:0c2f4edbd0c65bae2c7a3116cfc153b24b4f8983dcde184a2519d3c0d978f70f` |

