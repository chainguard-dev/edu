---
title: "jre Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jre Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-29 00:47:42
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/jre/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/jre/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/jre/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/jre/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | March 28th   | `sha256:840404a7a9ee5478598558128aea14004a1756ebe0bec734f7ea029f689aa23d` |
|  `latest`     | March 28th   | `sha256:42ffe937ebd7f481639885e6e0d793789c5bcec647f3cd8beaba3288581e196a` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-22.0` `latest` `openjdk-22` `openjdk-22.0.0`                             | March 28th   | `sha256:ca818f359331ef98fd4db7f1a332e384e5959d48bc5b6143945a579249354e5e` |
|  `openjdk-21` `openjdk-21.0.2` `openjdk-21.0`                                      | March 28th   | `sha256:4de5381d2de037371d3002a066325242a62a0d5665dc8c2a834debfbbdb2b1ec` |
|  `latest-dev` `openjdk-22-dev` `openjdk-22.0.0-dev` `openjdk-22.0-dev`             | March 28th   | `sha256:1a26f028ac0baaa298dcf294dfb030ad12c48073fa245fd9b1f8a41e98766edd` |
|  `openjdk-21-dev` `openjdk-21.0.2-dev` `openjdk-21.0-dev`                          | March 28th   | `sha256:cbdeb8417cbaf537fc8d267a97b632e408ac65ffe826a61ec2d12d4baf1f52a1` |
|  `openjdk-14-dev` `openjdk-14.0.2-dev` `openjdk-14.0-dev` `openjdk-14.0.2.12-dev`  | March 28th   | `sha256:8f01e0d3e248261c9e07baeedccec0ccefeb16179d350e4f919e115de88a5984` |
|  `openjdk-15` `openjdk-15.0.10` `openjdk-15.0` `openjdk-15.0.10.5`                 | March 28th   | `sha256:f8df439cc079513d04fcd1f3403b369cd5336ccceb12b37f949af7b096d4a1ae` |
|  `openjdk-8-dev` `openjdk-8.392.08-dev` `openjdk-8.392-dev`                        | March 28th   | `sha256:57c47c4a47ea38a5caa64d13876f0744ae0ca3d1cf4f0bc8177e2a4e1bce6a5d` |
|  `openjdk-15.0.10.5-dev` `openjdk-15.0-dev` `openjdk-15.0.10-dev` `openjdk-15-dev` | March 28th   | `sha256:6cb278dcbd4002dd47afee1f66f29297fde3d63454f9a364d74a416569407590` |
|  `openjdk-11.0` `openjdk-11` `openjdk-11.0.22`                                     | March 28th   | `sha256:a7455928b2c6d8725e13a3659aec352a7a99e2936f026741e979870b520ea39a` |
|  `openjdk-16-dev` `openjdk-16.0.2.7-dev` `openjdk-16.0-dev` `openjdk-16.0.2-dev`   | March 28th   | `sha256:dcdc880a60bc6295f1d787af5ce09ac0159c63b2090b5fbcf2cf720b985d25c3` |
|  `openjdk-14.0.2.12` `openjdk-14.0` `openjdk-14.0.2` `openjdk-14`                  | March 28th   | `sha256:044ad3727afb45b63aa97878b8b1f76cbe1e4534d2274b8a14d681bfbfcd542e` |
|  `openjdk-17.0.10-dev` `openjdk-17.0-dev` `openjdk-17-dev`                         | March 28th   | `sha256:f3f77ca061bcf0e38b508af0ed9ce40bdb2430295e41165cf115ce191ab69565` |
|  `openjdk-17.0.10` `openjdk-17` `openjdk-17.0`                                     | March 28th   | `sha256:24115abc079fb3bd9de16b2507e68fdd497f85e9bb10ebcad1adca925684aa18` |
|  `openjdk-11-dev` `openjdk-11.0.22-dev` `openjdk-11.0-dev`                         | March 28th   | `sha256:d8449d24973d945967c9fbc38a30b09d13c77abda90089771a11802001e16f71` |
|  `openjdk-16.0.2.7` `openjdk-16.0.2` `openjdk-16` `openjdk-16.0`                   | March 28th   | `sha256:c9b9fa231da3307202e253b719945e9d75535897874a19bf50dc9caec82431be` |
|  `openjdk-8.392` `openjdk-8.392.08` `openjdk-8`                                    | March 28th   | `sha256:352322c1270276d8dc473e469130cf5b0c9f20c5613e9dac3f5e5d7f11881d61` |

