---
title: "git Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the git Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-24 00:45:45
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
|  `latest-glibc`          | May 23rd     | `sha256:19dfea2c21fd55e08bda886e77b1f00075064f45a751b72f624daba48d85ccb9` |
|  `latest-glibc-root`     | May 23rd     | `sha256:a8369fc160c85ce337e239d4e102e5322dcc71f9218deaf98e9c3ff160b411dc` |
|  `latest-glibc-root-dev` | May 23rd     | `sha256:c108a1595e36a967682ced21167eac0ef12a91d5ac5d6f36d4a3eabe9cf3155b` |
|  `latest-glibc-dev`      | May 23rd     | `sha256:dd4bb108b8a8f2f957aadbe0224be1306bf0a8acf9455812d610c0fb85b9704d` |
|  `latest-dev`            | May 22nd     | `sha256:aab18a96fa32d77892406d8dca2d94c3ad882693eb2b670a45ecc893e1daf02d` |
|  `latest`                | May 22nd     | `sha256:f06036ea97419c784339638cf4a21b52d39df8dfd8aa0e0e73307fc1082c6043` |
|  `latest-root-dev`       | May 22nd     | `sha256:51c7c0164a6b4db491284ad755a0530df11c98d3081a5a05478656c34c9f991f` |
|  `latest-root`           | May 22nd     | `sha256:fa7a03c2cbfa3b961931f0fc0a3489e19fb06ae085f4c2dfd980347ed012c796` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                                                                                    | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `glibc-2.45-dev` `2.45-dev` `latest-dev` `2.45.1-dev` `latest-glibc-dev` `2-dev` `glibc-2-dev` `glibc-2.45.1-dev`                                         | May 23rd     | `sha256:b12e8f90af2f49f28e6db11f0e384613346af27d4bfeb64422fb2f7451756f4b` |
|  `root-2.45.1-dev` `latest-glibc-root-dev` `latest-root-dev` `root-2.45-dev` `glibc-root-2.45.1-dev` `glibc-root-2-dev` `root-2-dev` `glibc-root-2.45-dev` | May 23rd     | `sha256:140cf945eedcd73e02b0715b5f56c5befe763e77cb886cca4fb8e37e4a34f98f` |
|  `glibc-2.45` `latest` `latest-glibc` `2.45` `2` `glibc-2` `glibc-2.45.1` `2.45.1`                                                                         | May 23rd     | `sha256:2e7a9c6d3813ec2e3bae6436e09e8833fd5ce46ef5282b813adc47183a870b38` |
|  `latest-glibc-root` `root-2.45.1` `root-2.45` `root-2` `glibc-root-2.45.1` `glibc-root-2.45` `glibc-root-2` `latest-root`                                 | May 23rd     | `sha256:e43a1609b927011cdd2a717b45b8c07440bfe4cfe7db3fb9e91012014d6d6b2e` |
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

