---
title: "nginx Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the nginx Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-06 00:48:16
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
|  `latest`     | June 5th     | `sha256:f4683b8e1b6976fd4ba0e5bbfacdb0d2a81c355e00901b6197adf5c722bac93e` |
|  `latest-dev` | June 5th     | `sha256:b7781cae61fb9aacb903e72c0d620490d8e7552e1a5b59df90b36389eeedc7a4` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `1.27.0-dev` `1-dev` `1.27-dev` | June 5th     | `sha256:581c0d6b47872faed9fa36278b4773204c72233165a66757b8d772c45b9b4a6f` |
|  `1.27` `latest` `mainline` `1` `1.27.0`      | June 5th     | `sha256:b904aa95b3624202baafde213675b4c9d8e78340d52feeac3c2d14deef85c130` |
|  `1.25` `1.25.5`                              | June 5th     | `sha256:4f8f7cadfcc4cb7bc591aaabc4d4a2ce33c7ddb45fed40725f166073d3d3aa34` |
|  `1.26.1-dev` `1.26-dev`                      | June 5th     | `sha256:1d2e9de48d03f62bccf291837d88b4102ef5b7f03561a6cb21cdb5555f0c010e` |
|  `1.25.5-dev` `1.25-dev`                      | June 5th     | `sha256:c4c336a3dd640019f5fc60f4efa21df86d2c86a7c09a9bd943ff82cc2f4dd5c2` |
|  `stable` `1.26` `1.26.1`                     | June 5th     | `sha256:c05ecaed537e08cf11e06de73cac84c68d9139e96e8a6b2e6e9e67bcab486405` |

