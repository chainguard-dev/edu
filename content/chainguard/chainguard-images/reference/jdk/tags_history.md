---
title: "jdk Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jdk Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-07 00:46:50
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
|  `latest-dev` | June 6th     | `sha256:e54f00de0b29dd3ab1e23f97999b6790e154d3ce2ff6da6e2dc80c4c2f1eeea2` |
|  `latest`     | June 6th     | `sha256:a59fc9fb65cb667cd5e205ca965c3d8e20b111b200bc8636b575dc455be2f32a` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-22.0-dev` `latest-dev` `openjdk-22.0.1-dev` `openjdk-22-dev`             | June 6th     | `sha256:1cb06657cead4fdf8ee4cec01c58ba6048e7f6ab8771cdf43a6e134654407173` |
|  `openjdk-22.0.1` `latest` `openjdk-22.0` `openjdk-22`                             | June 6th     | `sha256:35de3a19a2982e97ac3db2895c7debe6ec73085a4c1debae825704ae0ce75bfa` |
|  `openjdk-14.0` `openjdk-14` `openjdk-14.0.2` `openjdk-14.0.2.12`                  | June 6th     | `sha256:693e76416d0e6dc4287d5f1ee2f97a1c7444d471de58c929111c3ed91881a556` |
|  `openjdk-16.0-dev` `openjdk-16-dev` `openjdk-16.0.2.7-dev` `openjdk-16.0.2-dev`   | June 6th     | `sha256:98f08957b78e4cf1ed5305342d3cdc1d3a045a74d6f0b72367f06a27cf2cfdca` |
|  `openjdk-14-dev` `openjdk-14.0.2.12-dev` `openjdk-14.0.2-dev` `openjdk-14.0-dev`  | June 6th     | `sha256:4553167fb5e0d6d8e8d1ebaa6e802fd9b4c6894239437e227592a50ad3204ec6` |
|  `openjdk-15.0` `openjdk-15.0.10.5` `openjdk-15.0.10` `openjdk-15`                 | June 6th     | `sha256:e2a3a21f41346151d73f2c067bbf548989f5c658afd9c70c6fad132a629c5ead` |
|  `openjdk-16.0` `openjdk-16.0.2.7` `openjdk-16.0.2` `openjdk-16`                   | June 6th     | `sha256:abfae615f65e688fec931500f449c13add0df3c5b07e35190bd922cae5993a42` |
|  `openjdk-15.0.10-dev` `openjdk-15.0.10.5-dev` `openjdk-15.0-dev` `openjdk-15-dev` | June 6th     | `sha256:c3becbf3ef13374baa2eab8e603dc0f61b6666653be57f8776a1cdf05341d0d2` |
|  `openjdk-21.0-dev` `openjdk-21-dev` `openjdk-21.0.3-dev`                          | June 5th     | `sha256:c7cd60c131e8b8d845e97ae21374d5462cf70f05d4cef688580cf863af8a3b2f` |
|  `openjdk-8.412-dev` `openjdk-8-dev` `openjdk-8.412.08-dev`                        | June 5th     | `sha256:dddde9c1586002525cf157dc8c72ed876270c39c71c06c732be2ab9e705830a4` |
|  `openjdk-8.412` `openjdk-8` `openjdk-8.412.08`                                    | June 5th     | `sha256:5566e209c1f461bd308cfdaaf5a19fa9a0e539c72cd7f053896c3f5d9ef829ba` |
|  `openjdk-11.0.23` `openjdk-11.0` `openjdk-11`                                     | June 5th     | `sha256:4cb2b13c5f6c45c34d6af0235ccabd401154d76a07721a7f7258d9ae44804964` |
|  `openjdk-17.0.11` `openjdk-17.0` `openjdk-17`                                     | June 5th     | `sha256:523f4faffa753f57f83ceca057a745e7209a04bbe5b1afe966ae163c25cd2ffc` |
|  `openjdk-17-dev` `openjdk-17.0.11-dev` `openjdk-17.0-dev`                         | June 5th     | `sha256:1b6cb0ba15f1be28b774a629256f9d76157da6e259ec895118b7f8fed7bfad65` |
|  `openjdk-21.0` `openjdk-21` `openjdk-21.0.3`                                      | June 5th     | `sha256:93342b6a77952e18d974c2c26bf0ee57e29dea020429a94f1888b88bdd8758eb` |
|  `openjdk-11.0-dev` `openjdk-11.0.23-dev` `openjdk-11-dev`                         | June 5th     | `sha256:08be9f2f5c22e632cab2d3e6a3fc56c61eab7c753c271d5a6b376b642f9a176f` |

