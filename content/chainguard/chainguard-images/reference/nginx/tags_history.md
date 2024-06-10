---
title: "nginx Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the nginx Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-10 00:50:47
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
|  `latest-dev` | June 9th     | `sha256:60600135946cf8d1c125ebee2d62384cabffce2c96777bdec1b4214e7ac59400` |
|  `latest`     | June 7th     | `sha256:703d3d482c8874a678e47be77336a5e286ec1d73082a41561a9e1b20b1a993e8` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `1.27.0-dev` `1-dev` `1.27-dev` | June 8th     | `sha256:2a89facfb2c7b6487c49b0d0671c8d3352928c2662b95e237d20ebac1d2cd99b` |
|  `1.26-dev` `1.26.1-dev`                      | June 8th     | `sha256:944898c191d57dc20d88970879305a0dec8cc9e19243352a4ba295a8bf387a68` |
|  `1.26` `stable` `1.26.1`                     | June 7th     | `sha256:44afa85e60dffd7b41e257f42d1ff4d76d10dd4d3045d9faed35b37faf1ae65c` |
|  `latest` `1.27` `mainline` `1` `1.27.0`      | June 7th     | `sha256:9d64c46dd9b7803183840aa1cd3f41ed358546702c67490f547111ecd06263a8` |
|  `1.25` `1.25.5`                              | June 5th     | `sha256:4f8f7cadfcc4cb7bc591aaabc4d4a2ce33c7ddb45fed40725f166073d3d3aa34` |
|  `1.25.5-dev` `1.25-dev`                      | June 5th     | `sha256:c4c336a3dd640019f5fc60f4efa21df86d2c86a7c09a9bd943ff82cc2f4dd5c2` |

