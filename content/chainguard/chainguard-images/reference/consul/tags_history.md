---
title: "consul Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the consul Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-09 00:39:12
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
|  `latest-dev` | July 8th     | `sha256:8e29d159ea2250f630ee5d68ba125475cdb26d97b5addbc183db8630eb8baf86` |
|  `latest`     | July 8th     | `sha256:ffd33b297bd9a00717c111d4f8464897d3188e8dba0270b8896b320f79f86071` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.15` `1.15.11`                             | July 8th     | `sha256:b7b7728e97fabe467c319759197e2a34a57846d13d22134633f4b0de102017d3` |
|  `latest` `1.17.4` `1.17` `1`                 | July 8th     | `sha256:066b0350f535c87a4bd2dff640a3be87eed877e05e10b8afb87dea675355e4d5` |
|  `1.16-dev` `1.16.7-dev`                      | July 8th     | `sha256:e000e5c781b1da21f262e19bb46dd33e734934466a15afda89275274194faf24` |
|  `1.17.4-dev` `latest-dev` `1.17-dev` `1-dev` | July 8th     | `sha256:e08ed4ec738fab302a3ee41067a9320c17d76a2700a39798133837e6baa7bef7` |
|  `1.15.11-dev` `1.15-dev`                     | July 8th     | `sha256:1959b73b485cb7caf21a962e40708be1bef57bbf2dd15155fd171693f09f52fc` |
|  `1.16.7` `1.16`                              | July 8th     | `sha256:bf6487f4a72aa5f356dc3d8cef038d974b9d182543b8d640e593b4d499d4d4a2` |

