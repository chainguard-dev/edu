---
title: "etcd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the etcd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-18 00:56:27
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/etcd/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/etcd/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/etcd/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/etcd/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | March 15th   | `sha256:cd0822750c32e20d0a22e22c80b28c91f50bd1471026fa40a2e54e36797be125` |
|  `latest`     | March 15th   | `sha256:f9d3b351d8c434f73abf7bb08041ec1b1c0c142304ed0c3c966852f797a9bf13` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                      | Last Changed | Digest                                                                    |
|----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `3.4-dev` `3.4.30-dev`                      | March 16th   | `sha256:cb5bf86b5050e3573d9e75cae68b6d02741f68ce12a0157938390923a6b7707a` |
|  `3.4.30` `3.4`                              | March 16th   | `sha256:66c9de672664e218eb952f7016ab48437ea27e7086e88ece00f406189e788bde` |
|  `3.5.12-dev` `3.5-dev` `latest-dev` `3-dev` | March 14th   | `sha256:c34c5b12c3a2d53ead81bb2034cda246bedad2059bcbc3e94c8e0affac20860c` |
|  `latest` `3.5.12` `3.5` `3`                 | March 14th   | `sha256:dd9cf1ee2283ce171c89cc27204063ea56b6ea03f6d073d49dfb44c9e58a4c35` |

