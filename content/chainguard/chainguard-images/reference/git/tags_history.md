---
title: "git Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the git Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-23 00:42:59
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
|  `latest-glibc-root-dev` | April 22nd   | `sha256:d49f736a9a89d3f1534ab0a050c455fd0e54ce5bc5cbbb7c3879cafd7cc751bd` |
|  `latest-glibc-root`     | April 22nd   | `sha256:18375cab89505fe793ba55f84174331f383c2127a549318a206b376556add0f3` |
|  `latest-glibc-dev`      | April 22nd   | `sha256:a1aff12c0a50c46346b49e7df823b507e36b5c463d1e262b41c8b5a4ec272015` |
|  `latest-glibc`          | April 22nd   | `sha256:368b42e7c9827e3aa8d3bb650f1e78c9530f564aeeb78952ab7663f126d9789e` |
|  `latest-root-dev`       | April 18th   | `sha256:2413d55ff4ad73a12034b36a2c57a03d3508674d6bf072a8b790530f4211a909` |
|  `latest`                | April 18th   | `sha256:f20defbb71126cae9e76cb95d24399df877b4fe62476525c0e67b05c0206b51d` |
|  `latest-dev`            | April 18th   | `sha256:0b30f3459d974ca7ac7644b3fa636fc069af55a400869a7a3fc274761147e7dc` |
|  `latest-root`           | April 18th   | `sha256:5faf844366d2223561a9633e2ecbb1a5cde8f8d716078d579c666ff734fd52a3` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                   | Last Changed | Digest                                                                    |
|-------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-glibc` `glibc-2.44` `glibc-2` `glibc-2.44.0`                                     | April 21st   | `sha256:f7a2aa865cc1d894d1b495aedb4a506c8c3beb6bb2aff6e674b095212b67dfd8` |
|  `glibc-root-2.44-dev` `latest-glibc-root-dev` `glibc-root-2-dev` `glibc-root-2.44.0-dev` | April 21st   | `sha256:14b2f555f9357820c258525e78c8a1043e2b3cfeb5cd65c90f5b42c10277bd7b` |
|  `glibc-root-2.44.0` `latest-glibc-root` `glibc-root-2` `glibc-root-2.44`                 | April 21st   | `sha256:e7d75a590697423d72df8fefb4ce8841e7b38cc89c7804f404dae9b3b7b0b11b` |
|  `glibc-2-dev` `latest-glibc-dev` `glibc-2.44.0-dev` `glibc-2.44-dev`                     | April 21st   | `sha256:1e89e0e1d06f58d535ee408a974f11f01233d776fe743188775cd36fb2532d58` |

