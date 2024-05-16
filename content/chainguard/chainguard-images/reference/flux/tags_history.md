---
title: "flux Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the flux Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-16 00:37:58
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/flux/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/flux/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/flux/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/flux/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | May 15th     | `sha256:c9dc12154cee09f0da2912f0cfa0967efcc03e327dc8edb74dca75198aa7e348` |
|  `latest-dev` | May 15th     | `sha256:556d5317750a32cc687af1e60be15d481c9e66fc37ae0e93b68e55b6d997b92d` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2.3` `latest` `2` `2.3.0`                 | May 15th     | `sha256:6deb3ef9dd256323957ccb8733a55005c5014a97a8987bb3f78f35d597b62f78` |
|  `latest-dev` `2-dev` `2.3.0-dev` `2.3-dev` | May 15th     | `sha256:8bc02cef37b13ab1cfb3d00eb3bba8c4750716b8bac6c6e95254b4db18881982` |
|  `2.2.3` `2.2`                              | May 2nd      | `sha256:8cfe941351304bf758f74f25831dd5def0ee2616fe89f1f42d8326edb8180352` |
|  `2.2.3-dev` `2.2-dev`                      | May 2nd      | `sha256:fb040a1798a4c30e8c3abe5905f62da9f2721931d9505e4ceef40f53165488e3` |

