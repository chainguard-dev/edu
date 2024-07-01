---
title: "jre Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jre Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-01 00:36:20
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
|  `latest-dev` | June 28th    | `sha256:11041bb40ddc77530428d4b6dc24cfa1e92ac1247c893f1b153081443feca213` |
|  `latest`     | June 28th    | `sha256:fc0e81c1af2e96e2ab881e1561cbd9d1a9c1d13a35fbf42f1ee9bde6046d5b92` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-22.0` `openjdk-22` `latest` `openjdk-22.0.1`                             | June 28th    | `sha256:a47e4a5c229b355a4954690312838b76d22ae6112b10c851c293a20b2efdfca0` |
|  `openjdk-15.0` `openjdk-15` `openjdk-15.0.10.5` `openjdk-15.0.10`                 | June 28th    | `sha256:744c45db7154a7f230e20b38fea01eda07cbe7949dd00ce7973c35da7f3417b6` |
|  `openjdk-14.0` `openjdk-14.0.2.12` `openjdk-14.0.2` `openjdk-14`                  | June 28th    | `sha256:74ece91e3c6bbc40e366d546c906d5a3ec051a1883229439418cb9a10ce2875e` |
|  `openjdk-16.0.2.7` `openjdk-16.0.2` `openjdk-16` `openjdk-16.0`                   | June 28th    | `sha256:237f08800423cf7526d67bf33f862d54ed29156ba93ebb933036d443a18efd0d` |
|  `openjdk-8.412.08` `openjdk-8.412` `openjdk-8`                                    | June 28th    | `sha256:df2a6b63db5b1d74d209e1aa319d03120d71a5bdb9d56baa0db2161b63dd071f` |
|  `openjdk-8.412-dev` `openjdk-8-dev` `openjdk-8.412.08-dev`                        | June 28th    | `sha256:2d2bb28dc3d472014ca31c6fc7f254da5bcf03abee38513d7403339718b5a826` |
|  `openjdk-17.0.11` `openjdk-17.0` `openjdk-17`                                     | June 28th    | `sha256:e601c8b7f8804e6d02c12626befab045ba2fdfbda7428e7b8e330b7b448a17ed` |
|  `openjdk-14-dev` `openjdk-14.0-dev` `openjdk-14.0.2-dev` `openjdk-14.0.2.12-dev`  | June 28th    | `sha256:b533b8b3d7d077cd4837da847785bcb3493a80f98eb8432b25a0002e3fc83d59` |
|  `openjdk-11` `openjdk-11.0` `openjdk-11.0.23`                                     | June 28th    | `sha256:ab886b534c64a6c7fed9be267bf092c4885e68aba235a85da8e767461e0e1315` |
|  `openjdk-15.0.10.5-dev` `openjdk-15.0-dev` `openjdk-15.0.10-dev` `openjdk-15-dev` | June 28th    | `sha256:2f697da75f21a947e326979b1ddb2e85b67faf572e441dc63ee78b76c988b217` |
|  `openjdk-21` `openjdk-21.0.3` `openjdk-21.0`                                      | June 28th    | `sha256:9081b83a4661a0f93614483f2c3383c30c3639ebeec3e0c8d7366b7d7f8ed805` |
|  `openjdk-16.0.2-dev` `openjdk-16-dev` `openjdk-16.0.2.7-dev` `openjdk-16.0-dev`   | June 28th    | `sha256:4e60c256845bfe79463aea50c89046495cb7404457862a1b9280531f876e3508` |
|  `openjdk-21-dev` `openjdk-21.0-dev` `openjdk-21.0.3-dev`                          | June 28th    | `sha256:1298e9e324fb842884c9551adee97260738c0027e632e61384fdb58a9c631d64` |
|  `openjdk-17.0-dev` `openjdk-17.0.11-dev` `openjdk-17-dev`                         | June 28th    | `sha256:f990b8d8c826e37489ffd4c117ad0ec8680a301ea9d503177ecb002540864df6` |
|  `openjdk-11-dev` `openjdk-11.0.23-dev` `openjdk-11.0-dev`                         | June 28th    | `sha256:e488e6b864c2419e573e3c8a3fff147250d2b4224bdb463036cf3f879680c814` |
|  `openjdk-22-dev` `openjdk-22.0.1-dev` `openjdk-22.0-dev` `latest-dev`             | June 28th    | `sha256:9cc43b4f3dad9837c34ce34aaa6cf8963c973b20b01f70e90f297be4f2c7ad44` |

