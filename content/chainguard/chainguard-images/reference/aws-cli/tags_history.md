---
title: "aws-cli Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the aws-cli Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-03 00:46:08
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
|  `latest-dev` | June 1st     | `sha256:3a9c419f36b257a972ee3b7e5ab150a1bab294b1cfa36886f1d43481acc17d8a` |
|  `latest`     | June 1st     | `sha256:e6190a241e2515ccdccbb69241f9c80dd6dcd9d222f7d49674655ccde3f2a32a` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1` `1.32.71` `latest` `1.32`                 | June 1st     | `sha256:7aa401f6c15ffaa246800ff2ec61551d4ec9c8562d198146ab3426e38c2247a9` |
|  `1.32-dev` `1-dev` `1.32.71-dev` `latest-dev` | June 1st     | `sha256:bc2a30c48c3f03b633b4dd2881fdb95539890c6d9b77573b6264b582bd152e32` |
|  `1.27.145-dev`                                | June 2nd     | `sha256:11ee37829afb9f0d8dd30e3f985ee5ed0380bef51b3bb9c420ab11ef672037bf` |
|  `1.27.145`                                    | June 2nd     | `sha256:4c5b29e30855d61c93cb44c9da32139f9a75eb3b349fd9777596f8830a20d147` |
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

