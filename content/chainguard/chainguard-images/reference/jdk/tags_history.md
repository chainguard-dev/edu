---
title: "jdk Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jdk Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-15 00:39:35
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/jdk/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/jdk/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/jdk/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/jdk/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 29th   | `sha256:edd009c0ff17ed9b589ede796cc1bd19149fb3b3f275e0357ab684f9685ac10e` |
|  `latest`     | April 22nd   | `sha256:6a733cdd53c73b6c6c0b58bf322ac7480c38e9271d277bb141debaa9f4ec066d` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `openjdk-22.0-dev` `openjdk-22-dev` `openjdk-22.0.1-dev`             | May 14th     | `sha256:f0369ac43a065b475c9875335d3bf11f67995721237f5b1e0291710c63c8a645` |
|  `openjdk-16-dev` `openjdk-16.0.2-dev` `openjdk-16.0.2.7-dev` `openjdk-16.0-dev`   | May 14th     | `sha256:35c01956e2b51018baad30f36f0a766133441857c4a1323998cdaf34f7159bfb` |
|  `openjdk-15-dev` `openjdk-15.0.10-dev` `openjdk-15.0-dev` `openjdk-15.0.10.5-dev` | May 14th     | `sha256:99f36891863f6e4e4a55dc2d378857884a96059d6817535074fe4240c0b8ea70` |
|  `openjdk-11.0.23-dev` `openjdk-11.0-dev` `openjdk-11-dev`                         | May 14th     | `sha256:35fde034611a23a5bd702a50998dd60f900599abefd9beb318a9f4ee30fadf8b` |
|  `openjdk-8.392.08-dev` `openjdk-8.392-dev` `openjdk-8-dev`                        | May 14th     | `sha256:4fec2137d8be9f560556180388d504060f89c0f5f18c7c11c32bb59dc99c5fa2` |
|  `openjdk-17.0-dev` `openjdk-17.0.11-dev` `openjdk-17-dev`                         | May 14th     | `sha256:ebad3d3f3df05f513a4d4de5fe08d8e3cda704daa712240fda7eb9c569320bb1` |
|  `openjdk-21.0.3-dev` `openjdk-21-dev` `openjdk-21.0-dev`                          | May 14th     | `sha256:d07e4168c767bef95b3b9f8eb2d86e92fa82864c49d5888a1dd55af1e10a1af3` |
|  `openjdk-14.0.2-dev` `openjdk-14.0.2.12-dev` `openjdk-14.0-dev` `openjdk-14-dev`  | May 14th     | `sha256:fa20b0b7fd413504d0d989051768e7fdc129c1faa817100c1634598a7e538dee` |
|  `openjdk-17` `openjdk-17.0.11` `openjdk-17.0`                                     | May 13th     | `sha256:79c21d0906f67c2839ac02a2481aeb164c6a7ac357b0cec4b80578dd5f5c8cf1` |
|  `openjdk-11.0` `openjdk-11.0.23` `openjdk-11`                                     | May 13th     | `sha256:c3331f2ff989e1f0680496923e5508b933d561001ff31244f31cac3a9ea98704` |
|  `openjdk-14.0.2` `openjdk-14.0.2.12` `openjdk-14` `openjdk-14.0`                  | May 13th     | `sha256:cee3cc17e77b1a9e92ae0d5c52850274c99cb168264a22d3bd68299641a55052` |
|  `openjdk-15.0` `openjdk-15.0.10` `openjdk-15.0.10.5` `openjdk-15`                 | May 13th     | `sha256:648138bc11e601e968395ce7613f939dc0c9f29c66a6fb6318165bda294a95f5` |
|  `latest` `openjdk-22` `openjdk-22.0` `openjdk-22.0.1`                             | May 13th     | `sha256:909017486cba84bf8854317d9dce7a3cf12bc7208ced9be24f706c4d82ef7900` |
|  `openjdk-8.392.08` `openjdk-8.392` `openjdk-8`                                    | May 13th     | `sha256:00377bec50d3cbce12468cd5920d63d03c6e56ad717584041808666cf865ebc9` |
|  `openjdk-21.0.3` `openjdk-21` `openjdk-21.0`                                      | May 13th     | `sha256:047c7045ba455cac74e0bef142282ccca87aec3dca362c7af2b5057e45f9118c` |
|  `openjdk-16.0.2.7` `openjdk-16` `openjdk-16.0.2` `openjdk-16.0`                   | May 13th     | `sha256:2597780fbbd8ab0b1183c7c202324686a8d76b621661360d010b3e4beb84735c` |
|  `openjdk-17.0.7.5`                                                                | April 21st   | `sha256:42f156acccda6a812a7792a6201b040080865c08d8d88602c9ef7a03c1fb291d` |
|  `openjdk-17.0.7.5-dev`                                                            | April 21st   | `sha256:e2436f9e5d2e780ea5809773e14715030fe90c677badba52a4d134e649beb8c3` |
|  `openjdk-11.0.18`                                                                 | April 19th   | `sha256:616a92ccf6b7da35d0bb32536342dbe71d44aec2a8056f3eba8835d3259806e5` |
|  `openjdk-11.0.18-dev`                                                             | April 19th   | `sha256:45d4fb375ddc407a53ef2fb5ad02c22dfb49e7ce11f1dc9f265552f29c8fc467` |
|  `openjdk-17.0.6-dev`                                                              | April 17th   | `sha256:8af23710b78109323329b8195092c9185f81ed7b002f363fbd85a95ad35bf40c` |
|  `openjdk-17.0.6`                                                                  | April 17th   | `sha256:429deb189bb4d575511a91844b2bdb45e3be956b748b2756408e3be517210541` |

