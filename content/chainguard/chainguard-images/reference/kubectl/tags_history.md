---
title: "kubectl Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the kubectl Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-09 00:39:12
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/kubectl/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/kubectl/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/kubectl/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kubectl/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | July 8th     | `sha256:0bdd434c07c1578d83277ad6eca86a11f8fc1c23fb49f278f8b9c4492a627118` |
|  `latest`     | July 8th     | `sha256:3b0c36a1df908b9d44820e218a536b08962801eff7705ad5c7b3f8b7e26fa63c` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.28.11-dev` `1.28-dev`                     | July 8th     | `sha256:1c66dfe4faaf9f2390ab273205ccadc0b6a978514f19b975f6afefb29d8e4f09` |
|  `1.30` `1.30.2` `1` `latest`                 | July 8th     | `sha256:b880d1f2fdabf4adfce9fbd8da05d8782776f6ea1ccd38125f7c596e567eb6af` |
|  `1.29` `1.29.6`                              | July 8th     | `sha256:25f74f314cfd8c916941f58c85db4e45e5c691d7f24d1786ff8949f55cf5c832` |
|  `1.28.11` `1.28`                             | July 8th     | `sha256:64024e379a96a8b4e918e1e6e7f574d2d1fe839dffd7e59df96a3bd0881560c0` |
|  `1.29-dev` `1.29.6-dev`                      | July 8th     | `sha256:3a45cdaf39a739b976deae60190b750e2337c88a721410db935f5e7fa937d9f1` |
|  `1.30-dev` `latest-dev` `1.30.2-dev` `1-dev` | July 8th     | `sha256:8ba4f0fed4b3236314c4d3086636d662c30413bafb35c8b1342b1d82c1c83ea3` |

