---
title: "bazel Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the bazel Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-03 00:45:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/bazel/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/bazel/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/bazel/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/bazel/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | May 2nd      | `sha256:5b49358568ba94ac8cc8ad4aeae091ca57b88567e066b786aacfa52f523d4c4e` |
|  `latest-dev` | May 2nd      | `sha256:5cb0594234052f690fcd639ffa1521dedf8bf90bc46b1165926846bf58adda02` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `5.4` `5` `5.4.1`                          | May 2nd      | `sha256:b8d502c151755096ef6f32153e985ebefecb360df7299033527f0743371fe95c` |
|  `7.1.1-dev` `7.1-dev` `latest-dev` `7-dev` | May 2nd      | `sha256:f4a47cfb9f5793a52b89e41429477fd02d38def36a19eb872f986a6fe0e480e9` |
|  `7` `latest` `7.1.1` `7.1`                 | May 2nd      | `sha256:e7fc9cb4e13e356ad208ceb247d2ec120dd6aef1d932ef16d13fbafab7118ae8` |
|  `6.5-dev` `6-dev` `6.5.0-dev`              | May 2nd      | `sha256:c2f3750e49f8bdc368be40dc9593ab5691b8acc7bcd08a08c725f5fb99aba549` |
|  `6` `6.5.0` `6.5`                          | May 2nd      | `sha256:62688145198613b626652d0caaaefa4eda00be57f5661323169677da1512c32a` |
|  `5-dev` `5.4-dev` `5.4.1-dev`              | May 2nd      | `sha256:9b1e858037852ec22ad5ddaf1a5532c70dc3d9659552baa6f2e97cd5a1606ea4` |
|  `6.1.1`                                    | April 28th   | `sha256:e779a5ec7dfce8190755a7c683f3f8fed331ac6909ec52270d35362fba8df214` |

