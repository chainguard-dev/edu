---
title: "jre Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jre Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-12 00:54:01
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
|  `latest`     | April 11th   | `sha256:cda68ba366e46bbda98cc73ea919ac048cbf81547f66448424d4f866963d1107` |
|  `latest-dev` | April 11th   | `sha256:88aceb7ab090f339ba70fed2c432dae806bece0aacf02805408fbf1a10b08392` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-22.0` `openjdk-22` `latest` `openjdk-22.0.0`                             | April 9th    | `sha256:888a85750c94957a1448ebded4f843d876aef1446225411c607014c93bd8c149` |
|  `openjdk-8.392.08` `openjdk-8.392` `openjdk-8`                                    | April 9th    | `sha256:24deaa9735f0b762d50bd5fed127dfd48e50a110d7de6b5970cb32732ac9f9a1` |
|  `openjdk-8-dev` `openjdk-8.392.08-dev` `openjdk-8.392-dev`                        | April 9th    | `sha256:bb38c764b745918ba5636f194d756deae8668de76752cf0cc47bdc5099164e74` |
|  `openjdk-11.0.22-dev` `openjdk-11.0-dev` `openjdk-11-dev`                         | April 9th    | `sha256:963e7ae2bcc2a0f3c4fc9e1649590440c64fc83610d6121129b44785ba2bfdd8` |
|  `openjdk-22.0-dev` `latest-dev` `openjdk-22-dev` `openjdk-22.0.0-dev`             | April 9th    | `sha256:1925e0c8a86fedd21941260730fb72dc02965e3ed61baeef0ea0b5308221208a` |
|  `openjdk-14.0.2.12` `openjdk-14.0.2` `openjdk-14.0` `openjdk-14`                  | April 9th    | `sha256:de5285e8dda5d4e3a42e74031acdb5e0a57a61dc8237ce8f0ddc6a4eb8216444` |
|  `openjdk-21.0-dev` `openjdk-21-dev` `openjdk-21.0.2-dev`                          | April 9th    | `sha256:c0a41f6e49b977799aaa662565ad0dfb58c1a55a18f8f5ce75f41086c597f28a` |
|  `openjdk-21` `openjdk-21.0` `openjdk-21.0.2`                                      | April 9th    | `sha256:a502d1a62dcc6694ffc58aa0fcc495717e33e513817390a0428780a1ffb75452` |
|  `openjdk-15.0` `openjdk-15.0.10.5` `openjdk-15` `openjdk-15.0.10`                 | April 9th    | `sha256:6d255adb05925a36af3de145a2a5137ec94af1f965299d4a2d80db9508599a2b` |
|  `openjdk-16.0.2-dev` `openjdk-16-dev` `openjdk-16.0-dev` `openjdk-16.0.2.7-dev`   | April 9th    | `sha256:4a49ed61ea7ea582ccfd84fc31e22af1aedfdd698f431576858b419fb52b924b` |
|  `openjdk-16.0` `openjdk-16.0.2` `openjdk-16` `openjdk-16.0.2.7`                   | April 9th    | `sha256:1ce1d34d038ff09a9297f484a8203230cca7e55624aa654425ea4bded467f7c7` |
|  `openjdk-14.0.2.12-dev` `openjdk-14-dev` `openjdk-14.0.2-dev` `openjdk-14.0-dev`  | April 9th    | `sha256:1f0695e42d70ea426ce0367d8591f6c210db361ef9ecf80f97cb5361a5dcfd76` |
|  `openjdk-11` `openjdk-11.0` `openjdk-11.0.22`                                     | April 9th    | `sha256:7746771ded40c7fad130a0f863f42496686d1f67200122857d7687d65b548668` |
|  `openjdk-15.0-dev` `openjdk-15.0.10-dev` `openjdk-15.0.10.5-dev` `openjdk-15-dev` | April 9th    | `sha256:1200d9948b5f0bdbccaa965c40285e94ffd066965feee57bdae3e7289f7c544c` |
|  `openjdk-17.0.10` `openjdk-17.0` `openjdk-17`                                     | April 9th    | `sha256:eee6152375ca913bb2f3c455e8154aa8f3fb9ca44f953e2bf83902072de541ff` |
|  `openjdk-17-dev` `openjdk-17.0-dev` `openjdk-17.0.10-dev`                         | April 9th    | `sha256:3da29747d2a1bbf21635afcb6de6e9503c9b25d2a05365824972f863fe88dadc` |

