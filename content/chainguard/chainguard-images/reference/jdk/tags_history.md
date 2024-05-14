---
title: "jdk Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jdk Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-14 00:46:23
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
|  `openjdk-17` `openjdk-17.0.11` `openjdk-17.0`                                     | May 13th     | `sha256:79c21d0906f67c2839ac02a2481aeb164c6a7ac357b0cec4b80578dd5f5c8cf1` |
|  `openjdk-17.0.11-dev` `openjdk-17-dev` `openjdk-17.0-dev`                         | May 13th     | `sha256:a99c02453495c65feba802bd6d3ada56f1d907a4631602446c1b97e9cd453a31` |
|  `openjdk-11.0` `openjdk-11.0.23` `openjdk-11`                                     | May 13th     | `sha256:c3331f2ff989e1f0680496923e5508b933d561001ff31244f31cac3a9ea98704` |
|  `openjdk-14.0.2` `openjdk-14.0.2.12` `openjdk-14` `openjdk-14.0`                  | May 13th     | `sha256:cee3cc17e77b1a9e92ae0d5c52850274c99cb168264a22d3bd68299641a55052` |
|  `openjdk-15.0` `openjdk-15.0.10` `openjdk-15.0.10.5` `openjdk-15`                 | May 13th     | `sha256:648138bc11e601e968395ce7613f939dc0c9f29c66a6fb6318165bda294a95f5` |
|  `openjdk-16.0.2-dev` `openjdk-16.0-dev` `openjdk-16.0.2.7-dev` `openjdk-16-dev`   | May 13th     | `sha256:adcbbc64ecb8ce690a6fb1f58caf369f3a4f8995d25f53735ce1d449153540fb` |
|  `latest` `openjdk-22` `openjdk-22.0` `openjdk-22.0.1`                             | May 13th     | `sha256:909017486cba84bf8854317d9dce7a3cf12bc7208ced9be24f706c4d82ef7900` |
|  `openjdk-21-dev` `openjdk-21.0-dev` `openjdk-21.0.3-dev`                          | May 13th     | `sha256:3f54aaee23c2bd707356465d352a8aa8451ffb2c9867d73adace0d4f25537c6e` |
|  `openjdk-15.0-dev` `openjdk-15.0.10.5-dev` `openjdk-15-dev` `openjdk-15.0.10-dev` | May 13th     | `sha256:37e142db4a0bbcb6e2a83d01bee74fc5eb7d414a2ee7c3b85edc607ec916ebcb` |
|  `openjdk-14-dev` `openjdk-14.0.2.12-dev` `openjdk-14.0-dev` `openjdk-14.0.2-dev`  | May 13th     | `sha256:93f1bf2b889311f642a41dbd97855301dc6139cc3857b97da6311fc7c431fc6b` |
|  `openjdk-8.392.08` `openjdk-8.392` `openjdk-8`                                    | May 13th     | `sha256:00377bec50d3cbce12468cd5920d63d03c6e56ad717584041808666cf865ebc9` |
|  `openjdk-21.0.3` `openjdk-21` `openjdk-21.0`                                      | May 13th     | `sha256:047c7045ba455cac74e0bef142282ccca87aec3dca362c7af2b5057e45f9118c` |
|  `openjdk-11.0-dev` `openjdk-11-dev` `openjdk-11.0.23-dev`                         | May 13th     | `sha256:fcbcce55666faba4861c4678366df9c46c289ea11e186f437f74cb7963db4a7b` |
|  `openjdk-16.0.2.7` `openjdk-16` `openjdk-16.0.2` `openjdk-16.0`                   | May 13th     | `sha256:2597780fbbd8ab0b1183c7c202324686a8d76b621661360d010b3e4beb84735c` |
|  `openjdk-22.0.1-dev` `openjdk-22.0-dev` `openjdk-22-dev` `latest-dev`             | May 13th     | `sha256:7b9d47779e67de03ea659b64f7decff659cd1b75eb1a98809c9d35cd874a1a93` |
|  `openjdk-8.392-dev` `openjdk-8.392.08-dev` `openjdk-8-dev`                        | May 13th     | `sha256:70dba6b0ffd23ce31bd2fe416f13d66a639650a36952d49da98f85ee8123a6d9` |
|  `openjdk-17.0.7.5`                                                                | April 21st   | `sha256:42f156acccda6a812a7792a6201b040080865c08d8d88602c9ef7a03c1fb291d` |
|  `openjdk-17.0.7.5-dev`                                                            | April 21st   | `sha256:e2436f9e5d2e780ea5809773e14715030fe90c677badba52a4d134e649beb8c3` |
|  `openjdk-11.0.18`                                                                 | April 19th   | `sha256:616a92ccf6b7da35d0bb32536342dbe71d44aec2a8056f3eba8835d3259806e5` |
|  `openjdk-11.0.18-dev`                                                             | April 19th   | `sha256:45d4fb375ddc407a53ef2fb5ad02c22dfb49e7ce11f1dc9f265552f29c8fc467` |
|  `openjdk-17.0.6-dev`                                                              | April 17th   | `sha256:8af23710b78109323329b8195092c9185f81ed7b002f363fbd85a95ad35bf40c` |
|  `openjdk-17.0.6`                                                                  | April 17th   | `sha256:429deb189bb4d575511a91844b2bdb45e3be956b748b2756408e3be517210541` |

