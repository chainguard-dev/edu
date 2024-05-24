---
title: "nginx Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the nginx Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-24 00:45:45
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/nginx/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/nginx/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/nginx/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/nginx/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | May 23rd     | `sha256:719305b803ebd28cf6c7ddb458723cfb1362491e3e1d6a5ca2270d9b02dd6e2e` |
|  `latest-dev` | May 23rd     | `sha256:a74de58017ff3ad6d3f875e5a65574074ef75c726caf7426c2eadef6631ffd14` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.26.0-dev` `1.26-dev`                      | May 23rd     | `sha256:110a9ee2a31ceaea3241396fdefa359bbe517a4daf5103620868e59e757c89a4` |
|  `latest-dev` `1.25.5-dev` `1.25-dev` `1-dev` | May 23rd     | `sha256:9f99a912166e5c893e3ca12b906e9a518dfd767d4834acc18989adf0384b58c2` |
|  `1` `mainline` `1.25` `1.25.5` `latest`      | May 23rd     | `sha256:93b6adddb594df94c5e196ef44ab87d133b4be98c91362d2ea63b970b7857f81` |
|  `1.26.0` `stable` `1.26`                     | May 23rd     | `sha256:8afccc2410fc9146dc5d5ea2874f8eafe3c7e52ebef3225d7d3b223e00a9abfa` |
|  `1.24` `1.24.0`                              | May 2nd      | `sha256:f9cd4ff7d76ff0ce095f42fea4c9b5820fb99dcb49df0f0e302d87883fab7967` |
|  `1.24-dev` `1.24.0-dev`                      | May 2nd      | `sha256:15ebd2e4311a62e1d77e55ff87e6f494c8d3a84ef8e861fdf6a7a85a92b3b4f3` |

