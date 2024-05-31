---
title: "k3s Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the k3s Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-31 00:48:45
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
|  `latest`     | May 30th     | `sha256:c34a5c9930d92e6aa815b213432fbc12bdc2e5f1edfb8edb1aa7b2dc919a7fe1` |
|  `latest-dev` | May 30th     | `sha256:f4f5d2c4cb3a5e06cabc9716f2d10138c0fd275a10d70cfdd7e014163ec5a49e` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.30` `1` `latest` `1.30.1`                 | May 30th     | `sha256:3f23458e3ca33ff4f0cd9ca66a6fbc7902e78fae140fb17eec971e0a25534036` |
|  `1.30.1-dev` `1-dev` `1.30-dev` `latest-dev` | May 30th     | `sha256:bfefb1b2ecbde094b6458e602b3dfa583276094726d2375d39b2f0b42e48088a` |
|  `1.30.0`                                     | May 24th     | `sha256:073ebc9c0283a713e2b6a14abe5f409218c6f56bd9c47e3ce9372de8cca144e3` |
|  `1.30.0-dev`                                 | May 24th     | `sha256:07c993cd151f4e37d2a746b5220b13f211cf8b250e978451e1dbf114b4616e7c` |
|  `1.29-dev` `1.29.4-dev`                      | May 10th     | `sha256:4c379598438191e888381509da4a3224e38a191c05933a9770f2392ed01019cc` |
|  `1.29` `1.29.4`                              | May 10th     | `sha256:8861a492fbaa9b7cfc5585b7ae4528f8872bf96f527c3abb10db83e6d700998a` |
|  `1.29.3-dev`                                 | May 2nd      | `sha256:e88dc01fc63356ccb3f1f1059325151039ef335aa1169786c264464cdd147bce` |
|  `1.29.3`                                     | May 2nd      | `sha256:dfb73d2715eb177c64d492ba42a4509c2943dc6c36075fa83401467515152466` |

