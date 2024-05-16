---
title: "jre Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jre Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-16 00:37:58
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
|  `latest-dev` | May 15th     | `sha256:874b9fc024a9a50e753d4665cfabd601bada5591bddefff360dcb545a8100fb9` |
|  `latest`     | May 15th     | `sha256:e1cd12b0f1584269370ce15eed8e8dd47c8f7a666f3bfbaed7f71ac1c6b0c761` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-21.0-dev` `openjdk-21-dev` `openjdk-21.0.3-dev`                          | May 14th     | `sha256:87adea2cba5d66d68d66146cbc6cede1d9b96185103613fd812ab604b571cc8e` |
|  `latest-dev` `openjdk-22.0.1-dev` `openjdk-22.0-dev` `openjdk-22-dev`             | May 14th     | `sha256:60eb8080c21f5830c90126d99e16f2cef7087a83bb1223cd647071d543c4290a` |
|  `openjdk-16-dev` `openjdk-16.0.2-dev` `openjdk-16.0-dev` `openjdk-16.0.2.7-dev`   | May 14th     | `sha256:11f520e2a61b01c95db52e789c25c6a101a3d5ac4f65d5b7cfb0c949ff60078e` |
|  `openjdk-17.0-dev` `openjdk-17.0.11-dev` `openjdk-17-dev`                         | May 14th     | `sha256:9f9b68358b37405a7b87626fe3cece9576a8fde5b304b96b4f0f79523c3d0c30` |
|  `openjdk-11.0-dev` `openjdk-11.0.23-dev` `openjdk-11-dev`                         | May 14th     | `sha256:8c9c34f3b20930384abe92a48e31572066ee9e49909d3af9894995838a311c01` |
|  `openjdk-8-dev` `openjdk-8.392.08-dev` `openjdk-8.392-dev`                        | May 14th     | `sha256:8fb446e62099befc4911af9e4f051f1f715c2aacda50cc9d841118e68d084538` |
|  `openjdk-14.0.2-dev` `openjdk-14-dev` `openjdk-14.0.2.12-dev` `openjdk-14.0-dev`  | May 14th     | `sha256:a2de64be3ca3b99c789d2229e0a6315e61ab1a000f44f2c23c82192ae409e2f2` |
|  `openjdk-15.0-dev` `openjdk-15.0.10.5-dev` `openjdk-15-dev` `openjdk-15.0.10-dev` | May 14th     | `sha256:56771125c4b177233f9bcd14153eeeac831b6cd87a0048bf3fb27500f1478f87` |
|  `openjdk-17.0.11` `openjdk-17.0` `openjdk-17`                                     | May 13th     | `sha256:99f4e6f472619761a6e739445db52aceda3dadcff8815e4e36550a69b3a8549b` |
|  `openjdk-11.0` `openjdk-11.0.23` `openjdk-11`                                     | May 11th     | `sha256:8c80f2cadf779faeb08959b0d755a6c92d6528cabe7bb3a1d8d32bd7b74a4602` |
|  `openjdk-14.0.2` `openjdk-14.0` `openjdk-14.0.2.12` `openjdk-14`                  | May 11th     | `sha256:0ae6bee285553e32fb2cc0adc2046c50e82b9dcab0648dc8d8dde0bbd319a479` |
|  `openjdk-21.0` `openjdk-21.0.3` `openjdk-21`                                      | May 11th     | `sha256:b2c2d7498a875c0315b53bc3d9441a8f10fa8c8c61800cd3f6c3be0781c41c32` |
|  `openjdk-8.392` `openjdk-8.392.08` `openjdk-8`                                    | May 10th     | `sha256:c4d78c1f468e52370fb3bfaf03166f14f421c5d2854cf4ee703eb70f97a57b5d` |
|  `openjdk-15.0` `openjdk-15` `openjdk-15.0.10.5` `openjdk-15.0.10`                 | May 10th     | `sha256:a219de1dbb06c53d9d11390dbfc0f3005adb78f259b6f5b4b85bfd4943798f1a` |
|  `openjdk-22.0` `latest` `openjdk-22.0.1` `openjdk-22`                             | May 10th     | `sha256:57400d410ae71aee7a621acdeb024cade196e93fec3df4861e9e6b4f93cd2725` |
|  `openjdk-16.0` `openjdk-16.0.2.7` `openjdk-16.0.2` `openjdk-16`                   | May 10th     | `sha256:7c1461ba6016c745c1d1d652377149c448ee3e3544178b0121ef0de55f7ff16f` |
|  `openjdk17.0.7.5-dev`                                                             | April 21st   | `sha256:d25a9f37fd4ae0a8aa5f0bb7675c9dfaa033e45ac0e4deb4a14e45aee3a4a62b` |
|  `openjdk17.0.7.5`                                                                 | April 21st   | `sha256:eeb678140e97079f4d1e554fa3575831329e78e1382605249ea8ea5558a96d11` |
|  `openjdk11.0.18-dev`                                                              | April 19th   | `sha256:1aa1a3510171eadd787e4a20ae76bef2ff04485d355e01dac1ddef5dbe70a2f2` |
|  `openjdk11.0.18`                                                                  | April 19th   | `sha256:b83713162fda412772e173171870d95621f170ffd46a629f880b44e9bca3a919` |

