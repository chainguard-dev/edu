---
title: "consul Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the consul Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-10 00:43:45
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/consul/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/consul/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/consul/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/consul/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | May 9th      | `sha256:12bde318df77e4ef0fe9c76d2ed8616fdf3127dbce117eff0ba2e7dc1fa6ab87` |
|  `latest-dev` | May 9th      | `sha256:0f8fedcb56913d7d894744529e0598586f64f81239345e649a81c1b4fd7842e2` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.15` `1.15.11`                             | May 9th      | `sha256:2c3a02fa5b6160b0696969639d9cdac07f0bf67053efb3cf3864ba42f951efd3` |
|  `1.16.7` `1.16`                              | May 9th      | `sha256:4367c6883f66fe6a2709efcefeb2c1ea4f2c44a8c292d987861b3a64d59e224b` |
|  `1.15-dev` `1.15.11-dev`                     | May 9th      | `sha256:044ce6118ece0e8dbdb4ff7966ecc964e359f1894036370ffc5510b814fc28cf` |
|  `1.16-dev` `1.16.7-dev`                      | May 9th      | `sha256:ca5231dee6603e83bbef4524fe8bc6b8811979f7a99dd18c0ee8ca855a740f7b` |
|  `1.17.4` `1.17` `1` `latest`                 | May 7th      | `sha256:9690b3086f0bbf5d549a76a73b10fa647812be25baa1ec7edd041a3eafa79f62` |
|  `1.17-dev` `1-dev` `latest-dev` `1.17.4-dev` | May 7th      | `sha256:7fed1d61d2ec01c073a488a247d655a0ede8c354e226064b1ea5a51db66c83f3` |

