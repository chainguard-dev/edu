---
title: "nginx Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the nginx Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-30 00:47:59
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
|  `mainline` `1.25` `1.25.5` `latest` `1`      | May 29th     | `sha256:c7ae06bfdb2b6a21b3716212e2a119144c92435c991d67560d608ae76a93a245` |
|  `latest-dev` `1.25.5-dev` `1.25-dev` `1-dev` | May 29th     | `sha256:58a3dab32e40a955aa444e392fa6cc7124ef11c0ba3de7c69489be8db89be24d` |
|  `1.26` `stable` `1.26.1`                     | May 29th     | `sha256:c6cf309a952fc9b20b3df262281b7c80d0a8098e10c6976314aa50742c4148e4` |
|  `1.26.1-dev` `1.26-dev`                      | May 29th     | `sha256:c0f68a018ccf114e9f4b6004b7085238e1aaf2be8477eaf4edd2f48ef69c426b` |
|  `1.26.0`                                     | May 24th     | `sha256:15cd3071254ed0c3fa7005f4e3379e7d478a83c55ad431fe68c3dbbfe43208c8` |
|  `1.26.0-dev`                                 | May 24th     | `sha256:af588d26d0f532bc3f1e01fd4516b6bf89c200332dad22fc13da39b441d5c55f` |
|  `1.24` `1.24.0`                              | May 2nd      | `sha256:f9cd4ff7d76ff0ce095f42fea4c9b5820fb99dcb49df0f0e302d87883fab7967` |
|  `1.24-dev` `1.24.0-dev`                      | May 2nd      | `sha256:15ebd2e4311a62e1d77e55ff87e6f494c8d3a84ef8e861fdf6a7a85a92b3b4f3` |

