---
title: "git Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the git Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-27 00:41:27
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
|  `latest-glibc-dev`      | June 26th    | `sha256:93748918d794eeb77e2e793abe373567f4f26867c1d990e09adda5a258ee9a86` |
|  `latest-glibc`          | June 26th    | `sha256:f2b5d3b2bc70adf6014bddaab06cfee4bdf8d45d641e3f8ffeb4ebe45ac73a16` |
|  `latest-glibc-root`     | June 26th    | `sha256:9f065e63ccd7e6e69e7f3ad931249fed542e6e3df96341583d794b1108330400` |
|  `latest-glibc-root-dev` | June 26th    | `sha256:09c3eba3c7faacd72fcca13e11ba2f05736e707a8a1215e415bc5ae5cf07246b` |
|  `latest-dev`            | June 23rd    | `sha256:846e1a4dbb50d840bf799f49688647f93028416217cebe3631572806a9c51fb2` |
|  `latest-root`           | June 23rd    | `sha256:d6631a4bfaa73f5edc536bfd7ab9e165f394a6fc1ff1e8834574f49bc0f4c2e9` |
|  `latest-root-dev`       | June 23rd    | `sha256:f9a47a22f7d4e93f5b31ce55b4ebfdf6aa8b5ac7dc85664846c474308c760bb1` |
|  `latest`                | June 23rd    | `sha256:06119871a608d163eac2daddd0745582e457a29ee8402bd351c13f294ede30e1` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                                                                                    | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `glibc-2.45.2-dev` `2.45-dev` `glibc-2-dev` `2.45.2-dev` `latest-glibc-dev` `2-dev` `glibc-2.45-dev` `latest-dev`                                         | June 26th    | `sha256:589d0a2e29ebf05557f38d20ef2eaab8419ab177e00bdd0edbb1bef6075ec771` |
|  `2.45.2` `latest-glibc` `latest` `glibc-2.45` `glibc-2.45.2` `2.45` `glibc-2` `2`                                                                         | June 26th    | `sha256:5bda9a0661a6ee3d3d6a180a9819ca8855cfaad17ef97bcdf67dbe5e16e548a7` |
|  `latest-glibc-root-dev` `glibc-root-2.45.2-dev` `root-2.45.2-dev` `glibc-root-2.45-dev` `root-2.45-dev` `root-2-dev` `latest-root-dev` `glibc-root-2-dev` | June 26th    | `sha256:f304c4ff8da6a54f8db2cb2d585754282c25e1c3dbb618fd0e10e8d9c7214601` |
|  `root-2` `root-2.45` `glibc-root-2.45.2` `latest-root` `latest-glibc-root` `glibc-root-2.45` `root-2.45.2` `glibc-root-2`                                 | June 26th    | `sha256:4887f04f7feae984bf5063ca7199edb4778ba09e4b7e83b2d18ef0436ea2669f` |

