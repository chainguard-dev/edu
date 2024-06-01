---
title: "octo-sts Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the octo-sts Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-01 00:50:07
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/octo-sts/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/octo-sts/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/octo-sts/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/octo-sts/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 31st     | `sha256:b14127cd72d6220e3a3db2d44809116136d42dc1d4b862fd961994a19cded8ff` |
|  `latest`     | May 23rd     | `sha256:25454dd98ca6221a4a34119994f0849529dd0475cf602cd9c1657949b674147c` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `0.2-dev` `0-dev` `0.2.0-dev` | June 1st     | `sha256:4a3839e9c8b18f08f26e6b0f2726a010f5935672eb4148afe185615242fcd870` |
|  `0` `latest` `0.2` `0.2.0`                 | May 23rd     | `sha256:a8fe8d841c17e9939340395826155e57e247c25601ae87c0954d961a72a28cb5` |
|  `0.1` `0.1.0`                              | May 17th     | `sha256:0ddf02893e4bd2de7632a03cbfd0e39a103429ffd7fbc8e825d61b53d62df6e8` |
|  `0.1.0-dev` `0.1-dev`                      | May 17th     | `sha256:6ec4d2c7a4f5492d5a8c93cd257309092c6abe41d13f39e26e51d4dc68bec509` |

