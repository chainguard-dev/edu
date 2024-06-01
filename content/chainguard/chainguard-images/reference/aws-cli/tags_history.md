---
title: "aws-cli Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the aws-cli Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-01 00:50:07
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
|  `latest-dev` | May 31st     | `sha256:3913c78500719db52c45936aa506656a2e97c89a9a77beab84e4de57c16712be` |
|  `latest`     | May 31st     | `sha256:8950dbdb5ad9494b881428250c04fd8498376aa8a6a57026751f8e2582756291` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1-dev` `latest-dev` `1.32.71-dev` `1.32-dev` | May 31st     | `sha256:2c79fcee7b43d68a550441e7f3f24d09a611d7f2bd38fd7926ccd556fd5a5d38` |
|  `1` `1.32.71` `latest` `1.32`                 | May 31st     | `sha256:2b9cf9fff53e40fae6ff1fefa205d7a07317ead9e324026c2f5438cb130fa463` |
|  `1.27.144-dev`                                | May 31st     | `sha256:d0064090043a2e1910b0f10be2843cbd55f8a106cac7813ff62e608915160f98` |
|  `1.27.144`                                    | May 31st     | `sha256:4911b3b61b98a0d331475f196f44567fe8fda823a87935139426e643d38533a9` |
|  `1.27.143`                                    | May 31st     | `sha256:db26ac6ead4a3ba6c7c527e46630906b4d6daede075fec92221a3df86d51e042` |
|  `1.27.142-dev`                                | May 29th     | `sha256:026a52de69ec66041411fa726bf3afe0d5037eaba8e266e0d29b02e16e3ec22b` |
|  `1.27.142`                                    | May 29th     | `sha256:f777aad92c935d6db47296527057079cee8245a5495f1d5d1dead59d64a05624` |
|  `1.27.141`                                    | May 27th     | `sha256:d3c4f2fee754bfbad6ae4c37e727b61d68ad10ee6805b01d3be30063b1782ce1` |
|  `1.27.141-dev`                                | May 27th     | `sha256:550277232ed15c810bf4222a3be50607d2a19b176b695735448347242cda66b2` |
|  `1.27.139-dev`                                | May 25th     | `sha256:fe2900f5c9472c61e531c57927496669e360c5768c3c756a7502772bf7949db7` |
|  `1.27.139`                                    | May 25th     | `sha256:dc18eb32b24af3909b893aa444f591ab5fa42db7123c2e58e19fc996f636430c` |
|  `1.27.138-dev`                                | May 24th     | `sha256:3fad1f9717ae9652e32e2bb2ad505f47e3e1b7e91618781d88dfaeca62bdb69b` |
|  `1.27.138`                                    | May 24th     | `sha256:ca753ceb33de695e109dde17476ff0a04184ba967a45c6e1020426e116a242f0` |

