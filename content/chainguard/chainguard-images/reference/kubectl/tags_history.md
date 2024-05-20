---
title: "kubectl Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the kubectl Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-20 00:48:18
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
|  `latest-dev` | May 17th     | `sha256:cab96ec0c0b4d4eaad44ca62e5469f3e9db30de6ce27e3512eec983d509a226b` |
|  `latest`     | May 17th     | `sha256:0a897f9869e621df64efe3cbd597aa7d1d45ceab3ed0fd6469b526c7040101b8` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.27-dev` `1.27.14-dev`                     | May 19th     | `sha256:0571af385e5b947587f2c7e6dcf879ac950941042380cb588be092d907601661` |
|  `1.28.10-dev` `1.28-dev`                     | May 19th     | `sha256:5b3485b076de3adb20134ac262957b4dd56a176ded914e3625a35e85889e4387` |
|  `1-dev` `latest-dev` `1.30.1-dev` `1.30-dev` | May 19th     | `sha256:4392c9f49ee8e3dba91c8936fd6f3ef7f7947eed6430e9e66aad5a6c1ffa931c` |
|  `1.29.5-dev` `1.29-dev`                      | May 19th     | `sha256:519abeeea0a98b287d3745fc931dbaa98f2b181182c9af8d840fe86c53b77c9b` |
|  `1.29.5` `1.29`                              | May 17th     | `sha256:14eb9dc17fae6485ae58824bb74745d6265eeee43dbb219d46ed1b9386e69938` |
|  `1.27.14` `1.27`                             | May 17th     | `sha256:c8db5e977b71eb525a26ddb1f74ef710fb47ca496f0e7ddea52da4b404d58f71` |
|  `1.30` `latest` `1` `1.30.1`                 | May 17th     | `sha256:fff73f1a08f82408ec48baf67e2c1e886906aa9d501cf4e11aa49bc63329ecc0` |
|  `1.28` `1.28.10`                             | May 17th     | `sha256:ef6dd69c67791763c9fae7f3ea4c214fafdf5d84165583580d0d38a199555fbd` |
|  `1.29.4`                                     | May 15th     | `sha256:ed3a78b7598f7bbc30b7f7409e3c908440c5cc9d85ac9aa286c33099cc3ef840` |
|  `1.30.0-dev`                                 | May 15th     | `sha256:1d3df70b95a12c53735c6fdd1d97c99a5dbfcee1862fcc4714f7f737f56ca650` |
|  `1.30.0`                                     | May 15th     | `sha256:b9cc3719a088d386d3ad87a831d7fc04dcf7416b8d04cee64926acc6707b0d13` |
|  `1.27.13`                                    | May 15th     | `sha256:8f75c099125fea0773715aded35592ff7fd8d8db59395ab3d3bb66d4f9aea275` |
|  `1.29.4-dev`                                 | May 15th     | `sha256:66ef3edc9137a991ea2a60aa8d5de8fe0ff1131dea2a0db8c7d7e61fff46c4f5` |
|  `1.27.13-dev`                                | May 15th     | `sha256:d37490676d071751b105967f6615d33f34aa27176e5b049e7112d59c2f1c3108` |
|  `1.28.9`                                     | May 15th     | `sha256:1731b37f5f760b29f540f0e013a97446baab1e12e832c7410ccfc1703517905c` |
|  `1.28.9-dev`                                 | May 15th     | `sha256:8e01bcda0bbefff414e5ea8888a9e8425704ddd00c5e14ec3cf4df1b6543147a` |
|  `1.26-dev` `1.26.15-dev`                     | May 13th     | `sha256:1e011aa667c8cc7a41eedaf1f38220b03a0f0d4277f3c0393c5ed47b24ad53a0` |
|  `1.25-dev` `1.25.16-dev`                     | May 13th     | `sha256:9ec0ad21540014026dacbef923fb5aeb9ed0b1636a505fad0522fe061df8a57c` |
|  `1.26` `1.26.15`                             | May 2nd      | `sha256:93a765a0c47c74985b04b152b7d573fd43252dc4e9f4f451ed62f5fffd5bd6b8` |
|  `1.25` `1.25.16`                             | May 2nd      | `sha256:51c66711b8efb6cb3ce2c2d9d8f5af35899e25636c3a98a82da98a102184b183` |
|  `1.28.8`                                     | April 24th   | `sha256:7fc7e22977b775a076be8989d68693b23780c5550ba13287f09cf31e628a86ba` |
|  `1.28.8-dev`                                 | April 24th   | `sha256:69f787fdf7ed164ec1a90071023b8efc952cd0e470b3188207c97ca7b52e02a7` |
|  `1.27.1`                                     | May 18th     | `sha256:cb0c5c3863e0a4c8b3a45e1248fc2e8761d241beac8b7b49abdc3822005bdc23` |

