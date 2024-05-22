---
title: "kubectl Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the kubectl Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-22 00:47:17
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
|  `latest-dev` | May 21st     | `sha256:03853d9de651683d93e3972c68a466e5752ec3f47923fc2586bae1925b7245fc` |
|  `latest`     | May 21st     | `sha256:35d756fd3b5722257f666e5bc8377977bb87cea297f5d95fb56f62a06b710550` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `1-dev` `1.30.1-dev` `1.30-dev` | May 21st     | `sha256:c33c881ba5b473489970d078c9abe69ffba096de25e1bbe0058857bceb17f18b` |
|  `1.29.5-dev` `1.29-dev`                      | May 21st     | `sha256:fb5521f20044fef2a948fd1533daec9052eaeb0dc57d128ddfc9f9e05a47be57` |
|  `1.27` `1.27.14`                             | May 21st     | `sha256:934a289ece53ce645aed1c49efbc46eb3e83731082c04520104582ce56f84629` |
|  `1` `1.30` `1.30.1` `latest`                 | May 21st     | `sha256:0792b408fff6c23a1d34836638d7e8f9654534c0b21b1fd221b63ccd1b856df3` |
|  `1.29.5` `1.29`                              | May 21st     | `sha256:46e91eae1260cab007a7ce88315abc111a698b962888bc75cfdbc9fafd85e3c0` |
|  `1.27.14-dev` `1.27-dev`                     | May 21st     | `sha256:3fdc1dbec463934f9246ec123383bcd7412950c92d80209635deb98817faec15` |
|  `1.28.10` `1.28`                             | May 21st     | `sha256:f030c6675e0bbf334c85c060e094930b83b1cfe03e1ab1de8430578b9bfbb663` |
|  `1.28-dev` `1.28.10-dev`                     | May 21st     | `sha256:52e7a8a854f72116e98e555d04edc91eb5b3b62be4043bc1f167a95b06e6d64b` |
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

