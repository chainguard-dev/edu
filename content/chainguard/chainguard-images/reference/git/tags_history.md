---
title: "git Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the git Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-01 00:50:07
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
|  `latest-root`           | May 31st     | `sha256:9a663a492a2061c0cb86ffdc34f4ba0f4e8283321969560088c1b4d97e785ac5` |
|  `latest-glibc`          | May 31st     | `sha256:112afd322a889656cf207b1ac58c19e0ad39f7b96b8a62392be232e3dcaeb75c` |
|  `latest`                | May 31st     | `sha256:4ad268dd2abb204b601fbeb6522ea8f7ea7f789fdb2821abce0cfb85143fe31a` |
|  `latest-dev`            | May 31st     | `sha256:9e453e652ee1f4c1031d90dd9f50098abbbb5a2ac4344d2f45073ef5724b9f15` |
|  `latest-root-dev`       | May 31st     | `sha256:2af786558f96c33f685d8a8c5d242f921a0f59cf3415931a5052f7c3fc957e86` |
|  `latest-glibc-root`     | May 31st     | `sha256:3761875cc34f55df7fe7225b412de40129d3eacd6b1219ca35afe9d25f22da8d` |
|  `latest-glibc-root-dev` | May 31st     | `sha256:501723845b48b77682cdc5a6d8dfdf3db9b2ceecffe5a75fb1773c0e66cbeba6` |
|  `latest-glibc-dev`      | May 31st     | `sha256:9f648e8faff329538cec1d3b678c2d2a4170a0102a6582cf02bb37b575120feb` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                                                                                    | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `glibc-2.45` `latest` `2` `glibc-2` `latest-glibc` `2.45.1` `2.45` `glibc-2.45.1`                                                                         | May 30th     | `sha256:7a36e339581ac80e18551d55c884ad7843bbad822f50f27cf68b8e3c2e32bcfc` |
|  `latest-root` `root-2.45.1` `root-2.45` `glibc-root-2.45.1` `latest-glibc-root` `root-2` `glibc-root-2.45` `glibc-root-2`                                 | May 30th     | `sha256:61d8b2544f0ed4b455debf2300c7a20257a5eee1fdcd621208665b4f870a292f` |
|  `root-2.45.1-dev` `glibc-root-2.45.1-dev` `latest-root-dev` `root-2-dev` `glibc-root-2-dev` `latest-glibc-root-dev` `root-2.45-dev` `glibc-root-2.45-dev` | May 30th     | `sha256:b6ae07c98340f572688b8678fc81318c8a1475cdc8aec66e5914dc586f839d63` |
|  `glibc-2.45-dev` `2.45-dev` `2-dev` `latest-dev` `latest-glibc-dev` `glibc-2.45.1-dev` `glibc-2-dev` `2.45.1-dev`                                         | May 30th     | `sha256:f8c6b4210586298cff7c8b93360dd6738d1d8e1a7defeeaed58a8ab92d8bd557` |
|  `2.45.0-dev` `glibc-2.45.0-dev`                                                                                                                           | May 14th     | `sha256:042068e25cbad28a8e3b127e8db212d9c4fa1aa5cc84751c262b3c83006cd1b2` |
|  `glibc-root-2.45.0` `root-2.45.0`                                                                                                                         | May 14th     | `sha256:f2ff396551bfe42e62401b04a65df65bf43f04d3aff283d0c42454d97d70d7d8` |
|  `2.45.0` `glibc-2.45.0`                                                                                                                                   | May 14th     | `sha256:827fbc62d3e475394599edbf9095a353b4ec964a64797b62b143ef100a464027` |
|  `glibc-root-2.45.0-dev` `root-2.45.0-dev`                                                                                                                 | May 14th     | `sha256:48efe16835214c405ce9131641af0e51f342d50b5e98f05dff415afb65ceb469` |
|  `glibc-2.40.1` `glibc-2.40`                                                                                                                               | May 31st     | `sha256:d9a4dfac6a30414987e34ef7a7eb5b647a8abca66269e1e3199a317ea10bf723` |
|  `glibc-root-2.40.1` `glibc-root-2.40`                                                                                                                     | May 31st     | `sha256:134bfe7b2df942f3f19e57002ae046eb6b34a87a8445342c61c8258efa382ddd` |
|  `glibc-2.40.1-dev` `glibc-2.40-dev`                                                                                                                       | May 31st     | `sha256:a026934a01663b2d17c5d9faa0730fb26866e8779434d0b5cb82ace802985532` |

