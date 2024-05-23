---
title: "git Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the git Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-23 00:45:07
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
|  `latest-dev`            | May 22nd     | `sha256:aab18a96fa32d77892406d8dca2d94c3ad882693eb2b670a45ecc893e1daf02d` |
|  `latest`                | May 22nd     | `sha256:f06036ea97419c784339638cf4a21b52d39df8dfd8aa0e0e73307fc1082c6043` |
|  `latest-root-dev`       | May 22nd     | `sha256:51c7c0164a6b4db491284ad755a0530df11c98d3081a5a05478656c34c9f991f` |
|  `latest-root`           | May 22nd     | `sha256:fa7a03c2cbfa3b961931f0fc0a3489e19fb06ae085f4c2dfd980347ed012c796` |
|  `latest-glibc-root-dev` | May 22nd     | `sha256:d9141d4eb4907857133a81b6e31e71ffd63e63398c3ec3800d335214859044d2` |
|  `latest-glibc-root`     | May 22nd     | `sha256:d54ee629c7ebbaa5e78162e03265717c00c4dc41a320c4e7a71a2e297c5091e1` |
|  `latest-glibc-dev`      | May 22nd     | `sha256:924d7711db30deb0e5faf45c4e2154f4edfc936b6503e2ef1c570b2a6191118f` |
|  `latest-glibc`          | May 22nd     | `sha256:83a11b0f522f52153b4045c4fff5139f4f237ebee45c2b109c8f906555cd4351` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                                                                                    | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `root-2.45.1` `glibc-root-2` `root-2` `latest-root` `latest-glibc-root` `glibc-root-2.45` `glibc-root-2.45.1` `root-2.45`                                 | May 22nd     | `sha256:70f128b79a5a6682f9737a08dc90a689708fe85d6edbb03508c612f8c4c2cbe5` |
|  `2-dev` `glibc-2-dev` `2.45-dev` `latest-glibc-dev` `2.45.1-dev` `glibc-2.45.1-dev` `latest-dev` `glibc-2.45-dev`                                         | May 22nd     | `sha256:6f54837a854eba6090db9bbbe1227075ad2c801f484151c7b27d211198169827` |
|  `glibc-root-2.45-dev` `glibc-root-2.45.1-dev` `latest-root-dev` `root-2-dev` `root-2.45-dev` `latest-glibc-root-dev` `root-2.45.1-dev` `glibc-root-2-dev` | May 22nd     | `sha256:b2ca934e75bff8ae165754d8d490734a5249e70c6415a18f0c846d1489019262` |
|  `glibc-2.45.1` `2.45.1` `2` `latest-glibc` `2.45` `glibc-2` `glibc-2.45` `latest`                                                                         | May 22nd     | `sha256:468fe40cf33ce926cb8916d0fcbee12da044937648fd2ed718552fdc0b3efbdc` |
|  `2.45.0-dev` `glibc-2.45.0-dev`                                                                                                                           | May 14th     | `sha256:042068e25cbad28a8e3b127e8db212d9c4fa1aa5cc84751c262b3c83006cd1b2` |
|  `glibc-root-2.45.0` `root-2.45.0`                                                                                                                         | May 14th     | `sha256:f2ff396551bfe42e62401b04a65df65bf43f04d3aff283d0c42454d97d70d7d8` |
|  `2.45.0` `glibc-2.45.0`                                                                                                                                   | May 14th     | `sha256:827fbc62d3e475394599edbf9095a353b4ec964a64797b62b143ef100a464027` |
|  `glibc-root-2.45.0-dev` `root-2.45.0-dev`                                                                                                                 | May 14th     | `sha256:48efe16835214c405ce9131641af0e51f342d50b5e98f05dff415afb65ceb469` |
|  `root-2.40.0`                                                                                                                                             | April 27th   | `sha256:9e3145982ed708b7490b05cc89a9f232412718c035f56915e7481fe508533d3e` |
|  `glibc-2.40.0-dev`                                                                                                                                        | April 27th   | `sha256:9a4062b9ad586a8aa2903442d792e334ba808cfa230acd6da1cf29fc0264e696` |
|  `glibc-root-2.40.0`                                                                                                                                       | April 27th   | `sha256:7be4de5e55c5ebe608183205cd23a9c9cc4df8df4d681971fb5a3c2de73a4f84` |
|  `glibc-2.40.0`                                                                                                                                            | April 27th   | `sha256:e1dd4ec03f692da3ae993f57126fdd6cc600daa7af01291369fd3eebc86521f7` |
|  `2.40.0`                                                                                                                                                  | April 26th   | `sha256:f5906926d6cf3ca4ed97295570341ce776674716e70b6783c87e59f278bf5cbf` |
|  `2.40.0-dev`                                                                                                                                              | April 25th   | `sha256:dff31aeb5de3d3cdb6eba4e071b68dbfb1d8616864add22b616dca7b4a4165bc` |

