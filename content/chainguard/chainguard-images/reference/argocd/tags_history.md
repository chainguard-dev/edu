---
title: "argocd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the argocd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-27 00:41:27
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/argocd/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/argocd/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/argocd/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/argocd/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 26th    | `sha256:d2db4becd4f8b69a02a8cda484ea389c53cc7f379eab47feda79e336eccf8d85` |
|  `latest`     | June 20th    | `sha256:2419508878d181620f1b8d4e5ff07b35b5c1592146815900624ec5f6fa3e1cf1` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2-dev` `2.11-dev` `latest-dev` `2.11.3-dev` | June 26th    | `sha256:c36850ae9c06de4c32d72d05ff2fa5edcbeb9e055c5e0734257081ab1df7e23e` |
|  `2.11` `latest` `2` `2.11.3`                 | June 26th    | `sha256:501273df14751c7345c9a760c72f53c9a7211442448c01766514838c14eea1f9` |
|  `2.8.18-dev` `2.8-dev`                       | June 26th    | `sha256:49364b8b400a597ace8e654c03b2d7cc4021662656dec6dc46db6f89dc5138f6` |
|  `2.10-dev` `2.10.12-dev`                     | June 26th    | `sha256:6bd8bd35e2aa9b38c9887a6cc140c6303c339bc848ee4df1cbfd8053c184d20b` |
|  `2.9-dev` `2.9.17-dev`                       | June 26th    | `sha256:feb904fb7ae42c0726c1e3438e01f6787b36ef6d61cd32e751b01a4a8f97288d` |
|  `2.9.17` `2.9`                               | June 25th    | `sha256:c2392385594b66ae53b55316cf3bc52c26c7f8067f8ec1421b15f750c8b84eae` |
|  `2.10.12` `2.10`                             | June 25th    | `sha256:7e21bca4fda50d60acf3e3f51be5223623aa611da1a41e7406b3eaeefbc3ab04` |
|  `2.8.18` `2.8`                               | June 20th    | `sha256:83cf4f6a04c977dea2cb1026560ffd6609c38015ab2318957481c1af0ecee724` |

