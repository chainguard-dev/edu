---
title: "git Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the git Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-02 00:32:13
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/git/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/git/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/git/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/git/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)                  | Last Changed | Digest                                                                    |
|--------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-glibc-root`     | July 1st     | `sha256:701e2b663dc7cfa235324260de79ab134074938b934a3a889304a1ee03443e87` |
|  `latest-glibc-root-dev` | July 1st     | `sha256:b9f708b7be7d81eeca9094ef47bd7ae76a389bf3ad7934e930ada14e24f503c6` |
|  `latest-glibc-dev`      | July 1st     | `sha256:0d94fd8a5b80f829b43c611b31a094aed2322e4ac72be90b474d08684801f44f` |
|  `latest-glibc`          | July 1st     | `sha256:20091b065fefc782c346d5d09845f1507516e3a13e062f15b2baaa049c88d0bf` |
|  `latest-root`           | June 30th    | `sha256:86896961b6049d834913780b8c8fef780f0db67b60010ad06bf06f90207d58b7` |
|  `latest-root-dev`       | June 30th    | `sha256:3f4264d49e56b723af56ec35dfea31c56404a00756e9d03fc51afec9274eb70d` |
|  `latest-dev`            | June 30th    | `sha256:88181f421a9db0388c0be4186d5db575eabffbaa1b84a782db5aada93e5f328b` |
|  `latest`                | June 30th    | `sha256:08af28f81fffaf3546514b38ff144adcca17c49690169284788bbdb0ac644ea6` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                                                                                    | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `glibc-2` `latest` `glibc-2.45` `2.45.2` `2` `glibc-2.45.2` `latest-glibc` `2.45`                                                                         | July 1st     | `sha256:ca8e887e3f5a0153f238d370ed6dc1aa7e766c565c876148327f6875132eab8d` |
|  `root-2-dev` `root-2.45.2-dev` `glibc-root-2-dev` `latest-glibc-root-dev` `latest-root-dev` `glibc-root-2.45-dev` `root-2.45-dev` `glibc-root-2.45.2-dev` | July 1st     | `sha256:43600ff29c5353fe4d69a7ff498f85c991539d769aabeb7159a1c86531d47246` |
|  `glibc-2.45-dev` `2.45.2-dev` `glibc-2-dev` `2-dev` `latest-dev` `latest-glibc-dev` `glibc-2.45.2-dev` `2.45-dev`                                         | July 1st     | `sha256:bf854d3812a3defc7f8a4d075ea88a0866decfc04b445cff0605afb8c0bbef2e` |
|  `glibc-root-2.45.2` `latest-root` `root-2` `latest-glibc-root` `glibc-root-2` `glibc-root-2.45` `root-2.45` `root-2.45.2`                                 | July 1st     | `sha256:823b6cd6d772ccd0764f331276108cf53190b4ee0268c9ad9ef2d27d13a3c24a` |

