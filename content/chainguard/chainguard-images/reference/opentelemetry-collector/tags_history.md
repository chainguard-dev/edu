---
title: "opentelemetry-collector Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the opentelemetry-collector Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-05 00:42:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/opentelemetry-collector/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/opentelemetry-collector/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/opentelemetry-collector/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/opentelemetry-collector/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | July 3rd     | `sha256:d56e558931d2e2f152542163c27bb8134961b3e6c616b849c8cd9742631604ad` |
|  `latest`     | July 3rd     | `sha256:d3341df763256fca86d74e5eea0f73d0c4f0d913da28de2d1c3fc9e0807f56cd` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                         | Last Changed | Digest                                                                    |
|-------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0-dev` `0.104-dev` `0.104.0-dev` `latest-dev` | July 3rd     | `sha256:d90c9107972dd1dbca34ccb85ac66e8c2e0a49455977a7bc901e41a22fd84b66` |
|  `0.104` `0` `latest` `0.104.0`                 | July 3rd     | `sha256:042773a2b8f82205dc45d4589869d1166c93437d42bc8b9c7221f3c4c40d238d` |
|  `0.103` `0.103.0`                              | June 28th    | `sha256:b8860e008cac352e6bd47299e5e229dbb19b23d041c5e7025d195f522664f480` |
|  `0.103-dev` `0.103.0-dev`                      | June 28th    | `sha256:3fc5d82c3cf0ae6b59967268f1ef8827400afcc196bed5912ac7bc75f0a9fac6` |

