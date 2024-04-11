---
title: "git Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the git Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-11 12:38:02
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
|  `latest-root-dev`       | April 10th   | `sha256:0ca199609653444cc132f3846e91bd3cd48c6d73876fcc565b917c83f223f8d7` |
|  `latest-root`           | April 10th   | `sha256:6db0c478f2b19f70cae861a60bb7c832fdba1af4070094e60c8b8c7fe9dd481f` |
|  `latest`                | April 10th   | `sha256:6e5c4b1a3c80b39ce36760e59e6eb9a1969163eb8c8f40746cb798695e6fad82` |
|  `latest-dev`            | April 10th   | `sha256:2865e1c40211e3b6ff1ceca65ec89a0bdcea5030e2cc1637c5cc504f68c02b77` |
|  `latest-glibc-root`     | April 9th    | `sha256:1b40bceb575c94a71e74905114526e86b48429f45c093307a55605ebe1244068` |
|  `latest-glibc-dev`      | April 9th    | `sha256:555b34957d27272e3e5e21b607fb68c6ea6225783462e86c0dd452ac4f579089` |
|  `latest-glibc-root-dev` | April 9th    | `sha256:38d0b75e7f024db75d6c63e4a197095006fb93c42e164ec6cc30593c3548f9e3` |
|  `latest-glibc`          | April 9th    | `sha256:7eea0d3cfa982736555773f11cafd5da0134e76820324e33391f0f203d7b5428` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                   | Last Changed | Digest                                                                    |
|-------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `glibc-2-dev` `glibc-2.44.0-dev` `latest-glibc-dev` `glibc-2.44-dev`                     | April 9th    | `sha256:0b3509f48d3bb2fe09761a18c54b59f299873636cc74fae8e64f44b7ce21997c` |
|  `latest-glibc-root` `glibc-root-2` `glibc-root-2.44` `glibc-root-2.44.0`                 | April 9th    | `sha256:3fb19ec92c4103e0b6d833bc17f434000bd8cce84c1f295155b305f11a03b4fe` |
|  `glibc-2.44` `latest-glibc` `glibc-2.44.0` `glibc-2`                                     | April 9th    | `sha256:902d1bcd6d0ed0275c2aafc4fb4192fa8f3b5dbab1bbf8a5ef3f6611cad6a141` |
|  `latest-glibc-root-dev` `glibc-root-2.44.0-dev` `glibc-root-2-dev` `glibc-root-2.44-dev` | April 9th    | `sha256:d40311318d5399bca89b42c20227a0c75673dee659ec8e2f8b316da1a6f9b5a6` |

