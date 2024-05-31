---
title: "nginx Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the nginx Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-31 00:48:45
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
|  `latest`     | May 30th     | `sha256:1a01e891696587501b097645d4feead0e0c512f7919481a10115d01bc1e94d27` |
|  `latest-dev` | May 23rd     | `sha256:a74de58017ff3ad6d3f875e5a65574074ef75c726caf7426c2eadef6631ffd14` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `mainline` `1.25` `latest` `1.25.5` `1`      | May 30th     | `sha256:4f8f7cadfcc4cb7bc591aaabc4d4a2ce33c7ddb45fed40725f166073d3d3aa34` |
|  `stable` `1.26` `1.26.1`                     | May 30th     | `sha256:c05ecaed537e08cf11e06de73cac84c68d9139e96e8a6b2e6e9e67bcab486405` |
|  `1.25.5-dev` `1.25-dev` `1-dev` `latest-dev` | May 30th     | `sha256:a37f81e431c6bc88755c7071ab379f35e687bde7767baa2c8e3fbbfbcb29b7e2` |
|  `1.26.1-dev` `1.26-dev`                      | May 30th     | `sha256:1c4cb29160a42ffc949edaf747eda6f4b1dc8be24f02dc3b3bb19447e46317ac` |
|  `1.26.0`                                     | May 24th     | `sha256:15cd3071254ed0c3fa7005f4e3379e7d478a83c55ad431fe68c3dbbfe43208c8` |
|  `1.26.0-dev`                                 | May 24th     | `sha256:af588d26d0f532bc3f1e01fd4516b6bf89c200332dad22fc13da39b441d5c55f` |
|  `1.24` `1.24.0`                              | May 2nd      | `sha256:f9cd4ff7d76ff0ce095f42fea4c9b5820fb99dcb49df0f0e302d87883fab7967` |
|  `1.24-dev` `1.24.0-dev`                      | May 2nd      | `sha256:15ebd2e4311a62e1d77e55ff87e6f494c8d3a84ef8e861fdf6a7a85a92b3b4f3` |

