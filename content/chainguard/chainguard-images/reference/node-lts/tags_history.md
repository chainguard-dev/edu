---
title: "node-lts Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the node-lts Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-13 00:45:28
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/node-lts/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/node-lts/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/node-lts/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/node-lts/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)                  | Last Changed | Digest                                                                    |
|--------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `next-dev` | May 9th      | `sha256:56c6bbd1fdbf513e376e677624563b68c9fb699162d1db7e4480c36d4b357aff` |
|  `next`                  | May 9th      | `sha256:edb467cff1faa0fa881fb7dd14696486815eab4eccb372bd987dc8328877bf1f` |
|  `latest`                | May 9th      | `sha256:fe26db9e7e82bfbce3c5a1d931d5938660a4524c4879f0fd76f72f1f85cf681d` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                     | Last Changed | Digest                                                                    |
|-------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `20-dev` `next-dev` `20.13.1-dev` `20.13-dev` `latest-dev` | May 10th     | `sha256:4e91c696651dd829998836a70493a960d257f006c14ecb3d4925916c24a565cc` |
|  `20.13.1` `latest` `20.13` `20`                            | May 9th      | `sha256:2e71ebf445bcc38058d086ca31c882bd70b0a8ceeeee2ed04aea7e5a327d00d2` |
|  `next`                                                     | May 9th      | `sha256:f71f94f84402c514a28da1937a623fcaa1ec46cf8c32576ce63ba76556685846` |
|  `20.13.0-dev`                                              | May 8th      | `sha256:2360a32e40e19b859f6d47a78ff722b6e3533260547e961a24aae47ad2603aa1` |
|  `20.13.0`                                                  | May 7th      | `sha256:9e605246896ec5e57b3ca2c840df46d2736a52d8093823a237437374d1c1c788` |
|  `20.12-dev` `20.12.2-dev`                                  | May 2nd      | `sha256:e8836f7cb1c3a413655996eb25cda5e87fe8950b6af44ff77a39f0ca39b32bd0` |
|  `20.12` `20.12.2`                                          | May 2nd      | `sha256:a55a71363129778395bcc88cc8c2fe6a0f26affb1d7ee94862bef5c6e1f1c873` |

