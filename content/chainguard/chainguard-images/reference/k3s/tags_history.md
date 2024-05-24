---
title: "k3s Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the k3s Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-24 00:45:45
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
|  `latest`     | May 23rd     | `sha256:6e58143addb99310c9cae4dffc86ce0caeed34a735ff553102cad3fd3a2e9c6b` |
|  `latest-dev` | May 23rd     | `sha256:f34c0b1fd691e8b51bd403d6392f79675db6bf527481543e8706e3ac2035ae0a` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `1.30.0` `1` `1.30`                 | May 23rd     | `sha256:2b474b1959d71154ea39040a61496e3453681338c7718923269a63a8f31e06c8` |
|  `1.30-dev` `latest-dev` `1.30.0-dev` `1-dev` | May 23rd     | `sha256:43e748be3f4261bf6badbb65286b9e7fd497d4b85846c536b336478591424239` |
|  `1.29-dev` `1.29.4-dev`                      | May 10th     | `sha256:4c379598438191e888381509da4a3224e38a191c05933a9770f2392ed01019cc` |
|  `1.29` `1.29.4`                              | May 10th     | `sha256:8861a492fbaa9b7cfc5585b7ae4528f8872bf96f527c3abb10db83e6d700998a` |
|  `1.29.3-dev`                                 | May 2nd      | `sha256:e88dc01fc63356ccb3f1f1059325151039ef335aa1169786c264464cdd147bce` |
|  `1.29.3`                                     | May 2nd      | `sha256:dfb73d2715eb177c64d492ba42a4509c2943dc6c36075fa83401467515152466` |

