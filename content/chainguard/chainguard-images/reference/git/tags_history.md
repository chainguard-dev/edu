---
title: "git Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the git Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-05 00:36:13
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
|  `latest`                | June 2nd     | `sha256:ec71921b0356838c6a720d1cc15472e160a6fa7e3cf1ef776154e70892c2b090` |
|  `latest-root-dev`       | June 2nd     | `sha256:28feaef348531865019ff676e4ea38d8491d1336b552f2bd48225ff5059be233` |
|  `latest-dev`            | June 2nd     | `sha256:eac2eb6821780fc2139ecc747424bc14f9301b1d37ca86f9bc70603de8cfbf4d` |
|  `latest-root`           | June 2nd     | `sha256:41d3f1d4b0662b147ec6b956aa4678b9a0af91e2b7768c23ae7c1ce2f5afb772` |
|  `latest-glibc`          | June 1st     | `sha256:256d1e46c37047da30e7bfd3052140b16a9640ca142a51e5072c6a6d26c24676` |
|  `latest-glibc-dev`      | June 1st     | `sha256:0c22623691c58d15bde0e43279bfe070fd9bdf506bc26d74b09e705528082ea5` |
|  `latest-glibc-root-dev` | June 1st     | `sha256:b2886820d38d03e1524aa24f5a73e75f6946e654383384c6efd82c3ce9777421` |
|  `latest-glibc-root`     | June 1st     | `sha256:8fb20a1aafd6459086b7384b634558dc7f650c5448deb97a5b8271200f94bee8` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                                                                                    | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `glibc-2` `2` `glibc-2.45.2` `glibc-2.45` `latest` `latest-glibc` `2.45` `2.45.2`                                                                         | June 1st     | `sha256:16440f412e22562e87bddacb0ea96d15373ecbb9dc95ef23bbd01f1a0a7f90fb` |
|  `2-dev` `glibc-2.45.2-dev` `2.45-dev` `latest-dev` `glibc-2-dev` `latest-glibc-dev` `glibc-2.45-dev` `2.45.2-dev`                                         | June 1st     | `sha256:f7a23a96513ffb6125398ca3c19070da935a3ec105ca424e8341b17e1b148a81` |
|  `root-2.45.2-dev` `root-2-dev` `root-2.45-dev` `glibc-root-2.45.2-dev` `latest-root-dev` `glibc-root-2.45-dev` `latest-glibc-root-dev` `glibc-root-2-dev` | June 1st     | `sha256:7e70bc91b9e37c59a2ebb77ff202c2f95e6fcbb3275d4992a0d9b646e7f715f5` |
|  `root-2.45` `glibc-root-2.45` `latest-root` `glibc-root-2.45.2` `glibc-root-2` `latest-glibc-root` `root-2` `root-2.45.2`                                 | June 1st     | `sha256:633f0ec4e940fbca8ab13f0048943c9c2cebb53277b88f47da24c94cbceb09e8` |
|  `root-2.45.1` `glibc-root-2.45.1`                                                                                                                         | May 30th     | `sha256:61d8b2544f0ed4b455debf2300c7a20257a5eee1fdcd621208665b4f870a292f` |
|  `root-2.45.1-dev` `glibc-root-2.45.1-dev`                                                                                                                 | May 30th     | `sha256:b6ae07c98340f572688b8678fc81318c8a1475cdc8aec66e5914dc586f839d63` |
|  `2.45.1` `glibc-2.45.1`                                                                                                                                   | May 30th     | `sha256:7a36e339581ac80e18551d55c884ad7843bbad822f50f27cf68b8e3c2e32bcfc` |
|  `glibc-2.45.1-dev` `2.45.1-dev`                                                                                                                           | May 30th     | `sha256:f8c6b4210586298cff7c8b93360dd6738d1d8e1a7defeeaed58a8ab92d8bd557` |

