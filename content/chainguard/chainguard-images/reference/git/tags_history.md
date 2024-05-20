---
title: "git Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the git Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-20 00:48:18
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
|  `latest-root`           | May 19th     | `sha256:b92fc5f802ee8b6c7b69b4324b7d44a45b1671c455d008f6c59ee4853c9797ef` |
|  `latest`                | May 19th     | `sha256:b9b8e2da60a6249533b8f14f06e1267124004f0c287c674d2e87331bf18336d0` |
|  `latest-dev`            | May 19th     | `sha256:0a51c96baace5df59e04f9ecb8ca0ffdb1fa5dc615ce02fbcb10a8e06e1bbcff` |
|  `latest-root-dev`       | May 19th     | `sha256:c334999be184a11ba4e39ae4b67efb8073541a075d2dbbbd60a58e238b37b17a` |
|  `latest-glibc`          | May 17th     | `sha256:59e3f2e468d3312507861238e54469b5a6a4bf8085799933138dacad184abb59` |
|  `latest-glibc-dev`      | May 17th     | `sha256:f03afbddc8470caa67f96c0277752c314bec5451c819c735e05f48dacf92dce3` |
|  `latest-glibc-root-dev` | May 17th     | `sha256:a5fa9e0c98fd830daf18d5e63abcfe19ec866fd3bbeb0e99d012d334cbf025ab` |
|  `latest-glibc-root`     | May 17th     | `sha256:d38ba8bc94213ebe98b64caccc301670f1557110b535e540ad2f9482bdac5f4d` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                                                                                    | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `glibc-2-dev` `glibc-2.45-dev` `2-dev` `latest-dev` `2.45.1-dev` `latest-glibc-dev` `2.45-dev` `glibc-2.45.1-dev`                                         | May 19th     | `sha256:50fe76658a2e528d89e1cbc847f556a9189fe5ede1173e2db763fac7408448c2` |
|  `latest-glibc` `2.45` `2` `glibc-2.45` `glibc-2.45.1` `glibc-2` `latest` `2.45.1`                                                                         | May 19th     | `sha256:c5c5062833c0ccab2377ac15b2114258228ea4cedcbd6efd514030b0dc4e187f` |
|  `root-2.45.1-dev` `glibc-root-2.45-dev` `glibc-root-2.45.1-dev` `latest-root-dev` `glibc-root-2-dev` `root-2-dev` `latest-glibc-root-dev` `root-2.45-dev` | May 19th     | `sha256:2c17c85c7c001ff89cc9aa6f9a8f86b963b472a3cf67fbf97225581d909bac3a` |
|  `root-2` `root-2.45.1` `root-2.45` `glibc-root-2.45` `latest-glibc-root` `glibc-root-2` `glibc-root-2.45.1` `latest-root`                                 | May 19th     | `sha256:a4b910b151e2ff6003fc7f925a052997558a568a38104b3be8b21424ed2270ad` |
|  `2.45.0-dev` `glibc-2.45.0-dev`                                                                                                                           | May 14th     | `sha256:042068e25cbad28a8e3b127e8db212d9c4fa1aa5cc84751c262b3c83006cd1b2` |
|  `glibc-root-2.45.0` `root-2.45.0`                                                                                                                         | May 14th     | `sha256:f2ff396551bfe42e62401b04a65df65bf43f04d3aff283d0c42454d97d70d7d8` |
|  `2.45.0` `glibc-2.45.0`                                                                                                                                   | May 14th     | `sha256:827fbc62d3e475394599edbf9095a353b4ec964a64797b62b143ef100a464027` |
|  `glibc-root-2.45.0-dev` `root-2.45.0-dev`                                                                                                                 | May 14th     | `sha256:48efe16835214c405ce9131641af0e51f342d50b5e98f05dff415afb65ceb469` |
|  `glibc-root-2.44-dev` `glibc-root-2.44.0-dev`                                                                                                             | April 21st   | `sha256:14b2f555f9357820c258525e78c8a1043e2b3cfeb5cd65c90f5b42c10277bd7b` |
|  `glibc-root-2.44.0` `glibc-root-2.44`                                                                                                                     | April 21st   | `sha256:e7d75a590697423d72df8fefb4ce8841e7b38cc89c7804f404dae9b3b7b0b11b` |
|  `glibc-2.44` `glibc-2.44.0`                                                                                                                               | April 21st   | `sha256:f7a2aa865cc1d894d1b495aedb4a506c8c3beb6bb2aff6e674b095212b67dfd8` |
|  `glibc-2.44.0-dev` `glibc-2.44-dev`                                                                                                                       | April 21st   | `sha256:1e89e0e1d06f58d535ee408a974f11f01233d776fe743188775cd36fb2532d58` |
|  `root-2.40.0`                                                                                                                                             | April 27th   | `sha256:9e3145982ed708b7490b05cc89a9f232412718c035f56915e7481fe508533d3e` |
|  `glibc-2.40.0-dev`                                                                                                                                        | April 27th   | `sha256:9a4062b9ad586a8aa2903442d792e334ba808cfa230acd6da1cf29fc0264e696` |
|  `glibc-root-2.40.0`                                                                                                                                       | April 27th   | `sha256:7be4de5e55c5ebe608183205cd23a9c9cc4df8df4d681971fb5a3c2de73a4f84` |
|  `glibc-2.40.0`                                                                                                                                            | April 27th   | `sha256:e1dd4ec03f692da3ae993f57126fdd6cc600daa7af01291369fd3eebc86521f7` |
|  `2.40.0`                                                                                                                                                  | April 26th   | `sha256:f5906926d6cf3ca4ed97295570341ce776674716e70b6783c87e59f278bf5cbf` |
|  `2.40.0-dev`                                                                                                                                              | April 25th   | `sha256:dff31aeb5de3d3cdb6eba4e071b68dbfb1d8616864add22b616dca7b4a4165bc` |

