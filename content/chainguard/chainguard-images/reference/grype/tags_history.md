---
title: "grype Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the grype Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-23 00:45:07
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
|  `latest-dev` | May 22nd     | `sha256:646d2ce0c951e0449c55420cfd0ec5fb692e4ce797cd0f34bc6b3c7bf12ba429` |
|  `latest`     | May 21st     | `sha256:ba2a343d7a8ed8dacd461e6a6e0aa7842b2b7f9b39ea0d8f1512841df3c9670d` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0.77.4-dev` `latest-dev` `0-dev` `0.77-dev` | May 22nd     | `sha256:39c6b5683b34e9bf24948de54f56f165eba89581d517df378293b050c7e250ac` |
|  `0.77.4` `0` `latest` `0.77`                 | May 21st     | `sha256:8320c8906d9d2fc4e8599d87362085548b4a282a47b42e6de0ce05b432dce9ae` |
|  `0.77.3-dev`                                 | May 10th     | `sha256:e1b42bc5ed7bef8e05a4d586278175e3f9da60a1c117aa6609273b339f1d3190` |
|  `0.77.3`                                     | May 10th     | `sha256:1983c77db21053d04fcd3ff46f40db5fbfaa3852b77f1932dab0873f909a18c8` |
|  `0.77.2`                                     | May 2nd      | `sha256:5110e7eb6eb7aad915a9e6f743e949d4ebef5d8d6e4d67862bd7021a5d0e30d7` |
|  `0.77.2-dev`                                 | May 2nd      | `sha256:bba1ddf52bae26bcae36d01809103548c4d7bb62ef2a76129b8f57a945c1f362` |
|  `0.77.1-dev`                                 | May 1st      | `sha256:0f9ee9c83dc3b8920cf49bc2a145ee9d09f8da647bf024583cbd5a5daf328a8e` |
|  `0.77.1`                                     | May 1st      | `sha256:d843569f324eee5bb52a1b20405444b0ebb4cd08fe36671c220ed59277a4680f` |

