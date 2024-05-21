---
title: "k3s Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the k3s Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-21 00:38:36
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
|  `latest-dev` | May 20th     | `sha256:99f7b9eee714287cf080c2b8e6b6edf1648e2f4360a38a4aff447b227ee9bc8f` |
|  `latest`     | May 17th     | `sha256:43276dcfa00a08e50eebbfb8a7d2882e1236aa622f9f39c3c87bac46420cfb2d` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `1.30.0-dev` `1.30-dev` `1-dev` | May 19th     | `sha256:eead371331258af94141147448f02118588b0d32f6e75ccfc488fd668cec7219` |
|  `1` `latest` `1.30.0` `1.30`                 | May 17th     | `sha256:e959afb3aa4ac95265b7dada13ba34db4b753cb7c66ff2ca8ef080ccb56d351d` |
|  `1.29-dev` `1.29.4-dev`                      | May 10th     | `sha256:4c379598438191e888381509da4a3224e38a191c05933a9770f2392ed01019cc` |
|  `1.29` `1.29.4`                              | May 10th     | `sha256:8861a492fbaa9b7cfc5585b7ae4528f8872bf96f527c3abb10db83e6d700998a` |
|  `1.29.3-dev`                                 | May 2nd      | `sha256:e88dc01fc63356ccb3f1f1059325151039ef335aa1169786c264464cdd147bce` |
|  `1.29.3`                                     | May 2nd      | `sha256:dfb73d2715eb177c64d492ba42a4509c2943dc6c36075fa83401467515152466` |

