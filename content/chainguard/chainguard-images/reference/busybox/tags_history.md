---
title: "busybox Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the busybox Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-03 00:46:08
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/busybox/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/busybox/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/busybox/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/busybox/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)         | Last Changed | Digest                                                                    |
|-----------------|--------------|---------------------------------------------------------------------------|
|  `latest`       | June 2nd     | `sha256:c74efaa7e158006d0cab2b467824ca86754ef3a6af18d80790d862e942e1ca86` |
|  `latest-glibc` | May 23rd     | `sha256:b1f74c11872f030ad7c37d10e45b8e214c45c5adcaf89278460193f1243b9cf4` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-glibc` `glibc-1.36.1` `glibc-1.36` `glibc-1` `1.36.1` `1.36` `latest` `1` | May 23rd     | `sha256:68d189d2bbc9bfe11336f0e21d412975826b427f8133d08adba36b690dcf935d` |
|  `glibc-1.36.0`                                                                    | May 26th     | `sha256:aa5f8fbd8ad3113b8a2204d27f9aed9146129fd72973627034f23a12bc757e14` |
|  `1.36.0`                                                                          | May 25th     | `sha256:40044e903ed084cfd16575da98578f8a3062e1a28aa5841ba19b9ed53da0ae92` |

