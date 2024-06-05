---
title: "nginx Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the nginx Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-05 00:36:13
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
|  `latest-dev` | June 1st     | `sha256:66edc7d99308cf3e8acc211397fcabe4919d802d2d587a0821ccbe6bdbdade64` |
|  `latest`     | May 30th     | `sha256:1a01e891696587501b097645d4feead0e0c512f7919481a10115d01bc1e94d27` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.25.5-dev` `1.25-dev` `1-dev` `latest-dev` | June 1st     | `sha256:c4c336a3dd640019f5fc60f4efa21df86d2c86a7c09a9bd943ff82cc2f4dd5c2` |
|  `1.26-dev` `1.26.1-dev`                      | June 1st     | `sha256:1d2e9de48d03f62bccf291837d88b4102ef5b7f03561a6cb21cdb5555f0c010e` |
|  `mainline` `1.25` `latest` `1.25.5` `1`      | May 30th     | `sha256:4f8f7cadfcc4cb7bc591aaabc4d4a2ce33c7ddb45fed40725f166073d3d3aa34` |
|  `stable` `1.26` `1.26.1`                     | May 30th     | `sha256:c05ecaed537e08cf11e06de73cac84c68d9139e96e8a6b2e6e9e67bcab486405` |

