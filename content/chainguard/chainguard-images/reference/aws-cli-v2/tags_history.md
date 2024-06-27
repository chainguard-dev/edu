---
title: "aws-cli-v2 Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the aws-cli-v2 Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-27 00:41:27
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/aws-cli-v2/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/aws-cli-v2/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/aws-cli-v2/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/aws-cli-v2/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 26th    | `sha256:db71f652bd72d8b42d4c9de903f4fbe908c13c280b954d04ba7986bbf9d1c294` |
|  `latest`     | June 26th    | `sha256:e8585ac4561e278b19bb550c0edf9e34edaacef9dcbb747b84331c7a1eb864cf` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `2.17.3-dev` `2.17-dev` `2-dev` | June 26th    | `sha256:7bf52dd6c7800b0e218bdcefd0abc0a529d21f7d6d6c15d11be920598ee0ea43` |
|  `2.17.3` `latest` `2.17` `2`                 | June 26th    | `sha256:639f2872928a2aab5732ca068d37e0824af87b41b093e5482011b0a613a559c6` |
|  `2.17.2`                                     | June 26th    | `sha256:4a06df9f9aab683a4a5f4e251beda6aa09979bfd5886bb83334d0c27b25d8ba4` |
|  `2.17.2-dev`                                 | June 26th    | `sha256:4dbdd8c38af32c480a7b37dea093c02419014cf3abd7e194b5c6ba58492c6b32` |
|  `2.17.1-dev`                                 | June 25th    | `sha256:c882fd061c3c9d8560d396a600c88d6920295f880958aa34975597c21f5bd770` |
|  `2.17.1`                                     | June 25th    | `sha256:e10a359b92c2d08524420d7ed46e9a12ff6b1db136b5b96dd6a7c8ad8c89f3c3` |
|  `2.17.0-dev`                                 | June 23rd    | `sha256:d9bd75dd9d699d70f3b9dae68d8c125e5348dc88d05ef7ba2e16be0161f0a17c` |
|  `2.17.0`                                     | June 21st    | `sha256:51bd61d00bd24cdc607d9a0480c8d78485f50b867aaa600370b53fbfb9bb695f` |
|  `2.16-dev` `2.16.12-dev`                     | June 20th    | `sha256:d6e03a467852102e9c77eb7040b83f8e22adb61037713085489e3bbe4cbc8621` |
|  `2.16.12` `2.16`                             | June 20th    | `sha256:cd4564f83bb7c14884273cfeab15b7e4dec6f760059b62ad362012c8e4026530` |

