---
title: "harbor-core Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the harbor-core Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-13 00:45:28
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/harbor-core/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/harbor-core/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/harbor-core/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/harbor-core/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | April 29th   | `sha256:3a814a86291f75b71f03c22e457dca2b9ddf8e92176ac2622864267f791c333f` |
|  `latest-dev` | April 29th   | `sha256:93a65cc31f22fb1d3b8faf6d6d5a2c5da4d92896dc9c39e1a51e92adccf1f4ff` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2.10-dev` `latest-dev` `2-dev` `2.10.2-dev` | May 10th     | `sha256:18f52aa0a4428275d40e155f0b5a01e5c0d9a20db3fe4affd22cf70e65c1869c` |
|  `2.10` `2.10.2` `latest` `2`                 | May 10th     | `sha256:7ecffb0565c8f243900f79f415118d6dce5e7c0e3347492a058b974d6be850dc` |
|  `2.8.6` `2.8`                                | May 9th      | `sha256:916ed40079acc3c0e385b6125f1284008ed568de04724000ab15d9a507a99953` |
|  `2.8-dev` `2.8.6-dev`                        | May 9th      | `sha256:74e81952f7ed5e85fc3f537e75990339a605d3afaed49d6da21da88ffd54d742` |
|  `2.9` `2.9.4`                                | May 9th      | `sha256:767a2c0b5a82c8280e928185d8ea528155ca4dd033e10c6f98c45b9d3ee2414b` |
|  `2.9.4-dev` `2.9-dev`                        | May 9th      | `sha256:b616efa73a8aa6f9e32716c3fdc6ceaf4f4c8248157cb07486cc8e3a763f1223` |
|  `2.8.5`                                      | April 21st   | `sha256:0658ade46bdeda39ef4c73cb1b482e12054bec8d9d92b308519d94e65f7e376b` |
|  `2.8.5-dev`                                  | April 21st   | `sha256:dc04549f03607e7f9ce712f17398058a98f1a19092042f922830d1190f976229` |

