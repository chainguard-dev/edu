---
title: "aws-cli Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the aws-cli Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-28 00:45:11
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/aws-cli/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/aws-cli/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/aws-cli/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/aws-cli/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | May 24th     | `sha256:4d45c8b3d660afdd38b6657ddf315acaf6650c7269806ca24b9e7a1c33b50370` |
|  `latest-dev` | May 23rd     | `sha256:e68e1a24030321d57fdba2cf5af534eeee5daff90c1736ea8d0785ad3217b28a` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.32-dev` `1-dev` `latest-dev` `1.32.71-dev` | May 25th     | `sha256:e00e94c6f1aa81d69887ab0b8d65226e9aef51c85a223d302392ecb6212d4baa` |
|  `1.32` `1.32.71` `latest` `1`                 | May 25th     | `sha256:c39a71318d2da9f8f7a9ef7d8d251268ec4b350406069a5e04259c003e7f81a1` |
|  `1.27.141`                                    | May 27th     | `sha256:d3c4f2fee754bfbad6ae4c37e727b61d68ad10ee6805b01d3be30063b1782ce1` |
|  `1.27.141-dev`                                | May 27th     | `sha256:550277232ed15c810bf4222a3be50607d2a19b176b695735448347242cda66b2` |
|  `1.27.139-dev`                                | May 25th     | `sha256:fe2900f5c9472c61e531c57927496669e360c5768c3c756a7502772bf7949db7` |
|  `1.27.139`                                    | May 25th     | `sha256:dc18eb32b24af3909b893aa444f591ab5fa42db7123c2e58e19fc996f636430c` |
|  `1.27.138-dev`                                | May 24th     | `sha256:3fad1f9717ae9652e32e2bb2ad505f47e3e1b7e91618781d88dfaeca62bdb69b` |
|  `1.27.138`                                    | May 24th     | `sha256:ca753ceb33de695e109dde17476ff0a04184ba967a45c6e1020426e116a242f0` |

