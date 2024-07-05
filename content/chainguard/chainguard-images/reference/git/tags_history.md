---
title: "git Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the git Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-05 00:42:00
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
|  `latest`                | July 3rd     | `sha256:85fd2de0e610cf5ec6fd4fa2be124b7e9e2d8e0f4205505675a94f2a02faa93e` |
|  `latest-glibc-root`     | July 3rd     | `sha256:4508118d898cb2b62bd027ffa858cad57b765b7a83e32464e82de989f691ba23` |
|  `latest-glibc`          | July 3rd     | `sha256:c1b78613e7e26e47b6b01a4df484b0acd022b6d37412f5eb547b8bf6169275c4` |
|  `latest-root`           | July 3rd     | `sha256:f3ed07723172f93a50715cf6189be7c7526232ff88035e3eb24046bfffeb8f5c` |
|  `latest-dev`            | July 3rd     | `sha256:10bad424ee9e08f43e54053d9091b0468f145bb6ee418debe42b08b0603508c9` |
|  `latest-root-dev`       | July 3rd     | `sha256:0dd259c7682b75f3187530717a0cff85eaeaa26e58bb535d4e8281c0b689f7f2` |
|  `latest-glibc-root-dev` | July 3rd     | `sha256:8b6f54467154baddf7867500d0db3979707982c2b6fab1824e00917a0698fae1` |
|  `latest-glibc-dev`      | July 3rd     | `sha256:ee6530240e01514eeee18fdf83d8982180fcf59fd986925ddf1e2da3b84f630f` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                                                                                    | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `glibc-2.45` `latest` `2.45.2` `2.45` `2` `latest-glibc` `glibc-2` `glibc-2.45.2`                                                                         | July 3rd     | `sha256:22d9f5286042bc8879cf6ffda9ad3ebbc7c05fae321008a2ca37e74b134ee293` |
|  `root-2.45.2-dev` `glibc-root-2.45-dev` `glibc-root-2-dev` `latest-root-dev` `root-2-dev` `glibc-root-2.45.2-dev` `latest-glibc-root-dev` `root-2.45-dev` | July 3rd     | `sha256:f3ad95870a2c985b333eb0ebe4cf88131dd476c42999fb2e189bed38f5bdfb11` |
|  `root-2` `glibc-root-2.45` `root-2.45.2` `glibc-root-2.45.2` `latest-root` `root-2.45` `glibc-root-2` `latest-glibc-root`                                 | July 3rd     | `sha256:a755d15d95d8a923cadabc5fcd7c12e0d8b987a067be0fbd1e2ed4e887fa70c4` |
|  `2.45-dev` `latest-glibc-dev` `latest-dev` `glibc-2.45.2-dev` `2.45.2-dev` `glibc-2.45-dev` `glibc-2-dev` `2-dev`                                         | July 3rd     | `sha256:fa3d10152206600e6d17166822bab5babd41782978f2183d2c1643c7c14b5e48` |

