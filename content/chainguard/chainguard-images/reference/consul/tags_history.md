---
title: "consul Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the consul Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-24 00:43:49
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
|  `latest`     | June 22nd    | `sha256:bd94fcfdfc47df15c182242005dcdd61c8bcdaf5fb1a1427b4588db5fae7986b` |
|  `latest-dev` | June 22nd    | `sha256:6688cf0451a96cb9132fa8bd9746d2492dcc01e23454c9848205de93c1cc3749` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.16` `1.16.7`                              | June 23rd    | `sha256:a2f2dfc8f0ad3a98eb860f5346891d1c3a897e32a03618f360a55aaea99788e8` |
|  `1.17.4-dev` `1-dev` `latest-dev` `1.17-dev` | June 23rd    | `sha256:a2a723e9be71c62bc03b0b82ba60f8f7b3ccf666f27c8add0ff5f4d741f15c4b` |
|  `latest` `1.17.4` `1` `1.17`                 | June 23rd    | `sha256:6462f81472e837f38cea4bf6f9e581ecbb39e0ff2bb7ae0ec21b13e7060002d7` |
|  `1.15` `1.15.11`                             | June 23rd    | `sha256:26ec4420e97e8720e6444bdbec4fae8f1b6fe15bdd396f162818d5b8b5ae466f` |
|  `1.16.7-dev` `1.16-dev`                      | June 23rd    | `sha256:86164d899b6fa6bb74811b32244844013ffc00840c91c286f1419345c3bc63a8` |
|  `1.15-dev` `1.15.11-dev`                     | June 23rd    | `sha256:bfe60c98c11f3fa254c88ee364f2dbad4c50e6184c6957940e265ab166ba6606` |

