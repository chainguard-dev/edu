---
title: "k3s Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the k3s Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-17 00:44:46
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
|  `latest-dev` | May 16th     | `sha256:eaaa7d4208a39bdf6070bb1a2f6585c0e10e70a1673a199bfa9c2ccbd74333e1` |
|  `latest`     | May 15th     | `sha256:03a31d4b07451bb1b37d34751d8fe766ff090d61ba634332b27d0551a7fb9715` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.30.0` `1` `1.30` `latest`                 | May 16th     | `sha256:93bdc2e8eb1522ddb1cae7cd77f46aa92e871eaf20e5b6f9d0a6a93b07914787` |
|  `1.30.0-dev` `1-dev` `latest-dev` `1.30-dev` | May 16th     | `sha256:7b7051769cc3e1f99679f15bd16a583b77c9265c6eebe4ff51a497b2c3e1d533` |
|  `1.29-dev` `1.29.4-dev`                      | May 10th     | `sha256:4c379598438191e888381509da4a3224e38a191c05933a9770f2392ed01019cc` |
|  `1.29` `1.29.4`                              | May 10th     | `sha256:8861a492fbaa9b7cfc5585b7ae4528f8872bf96f527c3abb10db83e6d700998a` |
|  `1.29.3-dev`                                 | May 2nd      | `sha256:e88dc01fc63356ccb3f1f1059325151039ef335aa1169786c264464cdd147bce` |
|  `1.29.3`                                     | May 2nd      | `sha256:dfb73d2715eb177c64d492ba42a4509c2943dc6c36075fa83401467515152466` |

