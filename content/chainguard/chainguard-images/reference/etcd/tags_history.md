---
title: "etcd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the etcd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-01 00:46:56
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/etcd/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/etcd/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/etcd/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/etcd/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 30th   | `sha256:2c2c993028a6127c7681085dcbcea9a044cdd75a02a9a72156dd3f5f97a3084a` |
|  `latest`     | April 22nd   | `sha256:aadc412c8dde0eca6ed3471cf2d29305cd4c40ddeb06481955fe8bb1e77e1ff1` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                      | Last Changed | Digest                                                                    |
|----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `3.5-dev` `latest-dev` `3.5.13-dev` `3-dev` | April 30th   | `sha256:33a02663c82ab5ec4ebcc57d8a36d55a7502a81feba55990678bb2cc3e057ce4` |
|  `3.4-dev` `3.4.32-dev`                      | April 30th   | `sha256:76d4a185c330507326f51eccf3127c5c60e54258ac0d19492df832165e73c9ca` |
|  `3.4.32` `3.4`                              | April 25th   | `sha256:d11026fd3c60e8673b132b6c6e82901287719cdf343c74b521a709f75c098bef` |
|  `3.4.31`                                    | April 21st   | `sha256:5d8abbcfb187978ef20eaca3d2b18382debc0f9e4095113a82136db41e34c04a` |
|  `3` `3.5.13` `latest` `3.5`                 | April 21st   | `sha256:55c42bb6a0403467c637d48379bdfb3278e0055a8114c113f30a09d18f1689ea` |
|  `3.4.31-dev`                                | April 21st   | `sha256:20d7842e9556329750de78172129f388f124a41b10aa679d691d01eec64eecd7` |

