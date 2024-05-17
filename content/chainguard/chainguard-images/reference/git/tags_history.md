---
title: "git Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the git Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-17 00:44:46
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
|  `latest-glibc`          | May 16th     | `sha256:cfb56f9819929051f27047731b55c06804b336a63d6e01424c718516cfffac6b` |
|  `latest-glibc-dev`      | May 16th     | `sha256:be98aed8fcf1c59831c0dacb5aaf9b2266344d90acd42ac15038ce4b36682069` |
|  `latest-glibc-root`     | May 16th     | `sha256:96bdbd0f57f83777c2f9972f8399b90c078b7db9a24794b2e6e1e152c0e902b4` |
|  `latest-glibc-root-dev` | May 16th     | `sha256:6a89dc488e427fce2b7e71db997cbcca375a281ec9db4d0f8bc214e321c9c098` |
|  `latest-root`           | May 16th     | `sha256:8332cf36bb4cd9412f4a66eb6f2b8ae5c473d64f5c9aeffec4fd950310dc241e` |
|  `latest`                | May 16th     | `sha256:41ca20d738c119fa68a55831a0ef49417547cffcb20ca1f52e1c305c787bb58c` |
|  `latest-root-dev`       | May 16th     | `sha256:26e03234f7e3962ad9aee92fb5657a492bfd3eccbd2ecbe502db2b3474629278` |
|  `latest-dev`            | May 16th     | `sha256:4f750b8acce18e383e1d186e600d03b2df55bc7f2a8d7f84c903dc85a92a75cb` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                                                                                    | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-glibc` `glibc-2.45` `2.45.1` `2` `2.45` `glibc-2` `latest` `glibc-2.45.1`                                                                         | May 16th     | `sha256:413c8150832e549d1dd0e59902dde99582a684475dfbb2cbae78cf520c28fc63` |
|  `glibc-root-2.45.1` `glibc-root-2` `root-2` `latest-root` `glibc-root-2.45` `root-2.45.1` `root-2.45` `latest-glibc-root`                                 | May 16th     | `sha256:ff7881f0f1d390a70b975609749b409ade58b66a6d39e11f4f9a20603603438f` |
|  `root-2.45.1-dev` `root-2.45-dev` `latest-glibc-root-dev` `glibc-root-2.45.1-dev` `latest-root-dev` `glibc-root-2-dev` `root-2-dev` `glibc-root-2.45-dev` | May 16th     | `sha256:2078beeed6f34e2c0b3aff0879989dfdf7dd676d497f4de4a8a2914d9e1d9295` |
|  `2.45-dev` `latest-dev` `2-dev` `glibc-2.45-dev` `2.45.1-dev` `glibc-2.45.1-dev` `glibc-2-dev` `latest-glibc-dev`                                         | May 16th     | `sha256:0eacb9e3c84be7bc5b8fe3357535f54798942a3c3e6327e7c4c827b0e01e5b3b` |
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

