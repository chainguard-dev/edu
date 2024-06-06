---
title: "etcd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the etcd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-06 00:48:16
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/etcd/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/etcd/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/etcd/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/etcd/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 5th     | `sha256:a81920e92094086fd5ab00953e490c13d2abae1d66ccb5317730900324af8aec` |
|  `latest`     | June 5th     | `sha256:4fdb9aa42c627105c95220b9b684e7c48119ae3c277ad57769bdc444417dfb3d` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                      | Last Changed | Digest                                                                    |
|----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `3.4` `3.4.32`                              | June 5th     | `sha256:a26aa0f531889f81d4d37dec83f6577629bcb35992818a2abcf523d942ca5fde` |
|  `3.4-dev` `3.4.32-dev`                      | June 5th     | `sha256:fe539857cfddf6b57dff194cc3c2f033b47900907e6a27558e1e2b5472e3cbb0` |
|  `latest-dev` `3-dev` `3.5-dev` `3.5.14-dev` | June 5th     | `sha256:7d6a50dbf261ec50d1309476e2b8d7f90a50eee4d75cba0b52e526a55666914b` |
|  `latest` `3.5` `3.5.14` `3`                 | June 5th     | `sha256:77855d3ad07f3e0418dc32fe0bca1bbfc7603f2f9f9d591c120c1e87ac078b5a` |

