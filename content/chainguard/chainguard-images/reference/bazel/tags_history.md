---
title: "bazel Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the bazel Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-11 00:42:18
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
|  `latest`     | June 10th    | `sha256:e6fb0e3e72d72aacc747545900d326fa01e082d40619aa58b3c4ebaf8f4361af` |
|  `latest-dev` | June 10th    | `sha256:1614e67b68dbdc1d5623874136db82aae9b3f677dd8010bd6f74f2ecb80912a3` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `7-dev` `7.2.0-dev` `latest-dev` `7.2-dev` | June 10th    | `sha256:c299951edb9e6dc9176f463198f9453ab0f707e4e42fb2fc23cea0308872d85e` |
|  `7.2` `latest` `7` `7.2.0`                 | June 10th    | `sha256:edc4ca2fc76078db71c9d73f1001f57b615dcead871bf4a7614de7360bec49fe` |
|  `5.4` `5` `5.4.1`                          | June 8th     | `sha256:a9a4cd6fae5ac59b254f5a6b5f5c1bc997d4f1ce4c8a8e12fe3eb8daece87853` |
|  `7.1.2` `7.1`                              | June 8th     | `sha256:1163fdaa1985f8970cf640653934bbd54bcdd5593bbe57a724e7e475745c891b` |
|  `6.5.0-dev` `6.5-dev` `6-dev`              | June 8th     | `sha256:9f35bc64ffd7354ee49f6b9a015538e80eea778e244135909931f954b6c21318` |
|  `5.4.1-dev` `5-dev` `5.4-dev`              | June 8th     | `sha256:95f0291a40ae590fb807be2864cc891d76301e233db564ce9145bd6b87dddd6e` |
|  `6.5.0` `6` `6.5`                          | June 8th     | `sha256:2ede2a2bd74f6e0135fc8a8e0a6e09bd28a435a8db86170bbaf38110121c42ac` |
|  `7.1-dev` `7.1.2-dev`                      | June 8th     | `sha256:a7a6569d7d87c36603ffc207b001436ec191ae9e1702a41d4fc9d6aea3989585` |

