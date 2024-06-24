---
title: "bazel Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the bazel Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-24 00:43:49
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/bazel/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/bazel/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/bazel/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/bazel/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | June 23rd    | `sha256:d45e7b1d8fedbc29d0a8139d66e5dc6ea2db33d99424703d6470ddcd3c65b781` |
|  `latest-dev` | June 23rd    | `sha256:2958ceec75c09f1ac086105dc1965ef31f5f708c8a7462d7c3804599e5936926` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `7.2` `7.2.0` `7` `latest`                 | June 23rd    | `sha256:279fd140c56b2d27e563745a28780cd692ba5d8e37b5bd3abebf83a91b5e3dc7` |
|  `5.4.1` `5.4` `5`                          | June 23rd    | `sha256:298ce086c9233f25fa958c2b17e533773e5a7f3fe0d8d0139284613e92012a0f` |
|  `7.2-dev` `7-dev` `7.2.0-dev` `latest-dev` | June 23rd    | `sha256:f512c825c49d2d8fdb21dbcfae72c75827fc9e90cc3d41fa41b764d81f68188a` |
|  `6.5-dev` `6-dev` `6.5.0-dev`              | June 23rd    | `sha256:6b866cb9e03d2abbdc7e6d06565263dff701cacac28622ad66987cdcb00e3a9a` |
|  `5.4.1-dev` `5-dev` `5.4-dev`              | June 23rd    | `sha256:3c2540757dcae74d85bca48de1b8b886c8b54359ac335e40dc6cb69c2b567331` |
|  `6.5.0` `6` `6.5`                          | June 23rd    | `sha256:31d435fc74a3359beeaf388848ef12a35f11bfe396b4325ed9112bb2cd45d2dc` |

