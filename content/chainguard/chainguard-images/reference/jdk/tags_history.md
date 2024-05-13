---
title: "jdk Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jdk Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-13 00:45:28
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
|  `openjdk-16.0.2.7-dev` `openjdk-16-dev` `openjdk-16.0-dev` `openjdk-16.0.2-dev`   | May 10th     | `sha256:da32902209f44d7fc9f507c2aa1b1000b85aff0aa52a2341832ce278bf9a4ab5` |
|  `openjdk-16.0.2.7` `openjdk-16.0.2` `openjdk-16` `openjdk-16.0`                   | May 10th     | `sha256:51df4016d983a445235e70818421644f72ac7cfecf58428950d0e1f826168d08` |
|  `openjdk-15-dev` `openjdk-15.0-dev` `openjdk-15.0.10.5-dev` `openjdk-15.0.10-dev` | May 10th     | `sha256:5a1a737bdb0772424c7d9d772f8c7346d67404b0313d2cd8bed140bb96f23729` |
|  `openjdk-17-dev` `openjdk-17.0-dev` `openjdk-17.0.11-dev`                         | May 10th     | `sha256:661e350931cf9ddea98fe2c0c788df89e20646cca8452f92f21b00f9f21cf432` |
|  `openjdk-21.0-dev` `openjdk-21-dev` `openjdk-21.0.3-dev`                          | May 10th     | `sha256:d8e95cc78dd94745aaf4e6a08022658eeb8b14dfc1d87b768003f3bbf21fa7c5` |
|  `openjdk-21.0` `openjdk-21.0.3` `openjdk-21`                                      | May 10th     | `sha256:0137e2f053ce822500629953e5c3bfe3611a7bf11f163f2ca36cfe671db23ab9` |
|  `openjdk-11.0.23` `openjdk-11.0` `openjdk-11`                                     | May 10th     | `sha256:b708794a788652e4b41e4aa7f8c67d9b5bb5dfbbf6d531e7d949bc6c87283646` |
|  `openjdk-8` `openjdk-8.392` `openjdk-8.392.08`                                    | May 10th     | `sha256:d4d64a84efaa33dbdbdc2c1d6fa3c9b029e70ce3719dcc8537328dc6ef205135` |
|  `openjdk-14.0.2.12` `openjdk-14` `openjdk-14.0.2` `openjdk-14.0`                  | May 10th     | `sha256:94447f838d22e9291dc85e996313c709358a356d10b0d52808b3475eb7994415` |
|  `latest` `openjdk-22.0.1` `openjdk-22.0` `openjdk-22`                             | May 10th     | `sha256:985cf47aae4c8c43abd13ba8497ccd1b5dc6e52f88bc5144aa04e46da23460c6` |
|  `openjdk-22.0-dev` `openjdk-22.0.1-dev` `latest-dev` `openjdk-22-dev`             | May 10th     | `sha256:21801db296cbfad0f9d769192946ecb0bcbe84e6eec948bfbad325d22eff311f` |
|  `openjdk-17` `openjdk-17.0` `openjdk-17.0.11`                                     | May 10th     | `sha256:039d4d68e017c75da124e6127e2df4798fba04764bb75f0c8702f1be98c498fb` |
|  `openjdk-14.0-dev` `openjdk-14.0.2-dev` `openjdk-14-dev` `openjdk-14.0.2.12-dev`  | May 10th     | `sha256:24619e4de939dd6841c58e90a7bced1b387305779c80c274cd36df39935dda0c` |
|  `openjdk-15.0` `openjdk-15.0.10.5` `openjdk-15.0.10` `openjdk-15`                 | May 10th     | `sha256:4b93c715f95de7f0d05ee1f241d7316b2e973ac50685730ccc850a29c3d551a6` |
|  `openjdk-11.0-dev` `openjdk-11-dev` `openjdk-11.0.23-dev`                         | May 10th     | `sha256:be9e5c4387713d2b8ea32a75cdae09699b1391ce7f1abc8646a32a5047e28481` |
|  `openjdk-8.392.08-dev` `openjdk-8.392-dev` `openjdk-8-dev`                        | May 10th     | `sha256:0657eae11fdb05cb568c0cefa3c01e7e1c3441b985bb9fa94acd237d3e1d898b` |
|  `openjdk-17.0.7.5`                                                                | April 21st   | `sha256:42f156acccda6a812a7792a6201b040080865c08d8d88602c9ef7a03c1fb291d` |
|  `openjdk-17.0.7.5-dev`                                                            | April 21st   | `sha256:e2436f9e5d2e780ea5809773e14715030fe90c677badba52a4d134e649beb8c3` |
|  `openjdk-11.0.18`                                                                 | April 19th   | `sha256:616a92ccf6b7da35d0bb32536342dbe71d44aec2a8056f3eba8835d3259806e5` |
|  `openjdk-11.0.18-dev`                                                             | April 19th   | `sha256:45d4fb375ddc407a53ef2fb5ad02c22dfb49e7ce11f1dc9f265552f29c8fc467` |
|  `openjdk-17.0.6-dev`                                                              | April 17th   | `sha256:8af23710b78109323329b8195092c9185f81ed7b002f363fbd85a95ad35bf40c` |
|  `openjdk-17.0.6`                                                                  | April 17th   | `sha256:429deb189bb4d575511a91844b2bdb45e3be956b748b2756408e3be517210541` |

