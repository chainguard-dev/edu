---
title: "octo-sts Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the octo-sts Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-23 00:45:07
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
|  `latest-dev` | May 22nd     | `sha256:eee0c5fc2e97887a1957b75a2acd78bd5dd8376b2a62f7ad7b0f415be51d1974` |
|  `latest`     | May 21st     | `sha256:c9af2afd889d4bf5334f897f212d92c0ebfc8271f8d1d1159d51f4958d5e03ad` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `0.2-dev` `0.2.0-dev` `0-dev` | May 22nd     | `sha256:e377cb8cdb3db46e671d9700f5340d8ca96144b1fcd922fe2ba96980a61560a3` |
|  `latest` `0.2.0` `0.2` `0`                 | May 21st     | `sha256:9fef8ca7edfa004858de97944e897e2e6ffd3c3b9f47e3c9bb0d98c686dd9764` |
|  `0.1` `0.1.0`                              | May 17th     | `sha256:0ddf02893e4bd2de7632a03cbfd0e39a103429ffd7fbc8e825d61b53d62df6e8` |
|  `0.1.0-dev` `0.1-dev`                      | May 17th     | `sha256:6ec4d2c7a4f5492d5a8c93cd257309092c6abe41d13f39e26e51d4dc68bec509` |

