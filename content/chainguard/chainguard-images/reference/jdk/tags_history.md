---
title: "jdk Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jdk Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-10 00:50:47
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
|  `latest-dev` | June 9th     | `sha256:879b1ce81ea3525c881f1ce9af335af32a2100b492e4ad94c180b4821cb95235` |
|  `latest`     | June 6th     | `sha256:a59fc9fb65cb667cd5e205ca965c3d8e20b111b200bc8636b575dc455be2f32a` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-17-dev` `openjdk-17.0-dev` `openjdk-17.0.11-dev`                         | June 8th     | `sha256:a67c2a210be95f067e426b0e75bb2ab00e36f87791149df5483e14877edc8760` |
|  `openjdk-22-dev` `latest-dev` `openjdk-22.0-dev` `openjdk-22.0.1-dev`             | June 8th     | `sha256:a4875aa76a536c24ec17fd0581b1d53539fd3e3818ed34aa86318add1763847e` |
|  `openjdk-8-dev` `openjdk-8.412.08-dev` `openjdk-8.412-dev`                        | June 8th     | `sha256:5d554482788675e6b92ec195b6db8453589c3a5e4a32c2564b283afa910e6860` |
|  `openjdk-15.0-dev` `openjdk-15.0.10-dev` `openjdk-15.0.10.5-dev` `openjdk-15-dev` | June 8th     | `sha256:452dae5285ae10ae0afa910b4c9f61dcb764c7045a93f7d1e5f3e77cf3ef6490` |
|  `openjdk-16.0.2.7-dev` `openjdk-16.0.2-dev` `openjdk-16-dev` `openjdk-16.0-dev`   | June 8th     | `sha256:ded86bd1d99b3a59393fd28dae51638c30cfcd963d144b79483be614dc580a50` |
|  `openjdk-14.0.2.12-dev` `openjdk-14.0.2-dev` `openjdk-14-dev` `openjdk-14.0-dev`  | June 8th     | `sha256:ca2b5c2ee053a128e9a36b07c0d7e9b580066bdcccdab893201ad1845b7e08e9` |
|  `openjdk-11-dev` `openjdk-11.0.23-dev` `openjdk-11.0-dev`                         | June 8th     | `sha256:663a57f9b242c46b91123514fbf2cbe31d855edb5f085badee880431a02deae6` |
|  `openjdk-21-dev` `openjdk-21.0.3-dev` `openjdk-21.0-dev`                          | June 8th     | `sha256:c24dd6361f5e984a207c1f010c658eb8c1b98bf4722c056e011410ff31974f35` |
|  `openjdk-8.412.08` `openjdk-8.412` `openjdk-8`                                    | June 7th     | `sha256:d6a12adb91421b064f184601558ad20ba76b83f100a7994b567ef8c10a217079` |
|  `openjdk-22.0.1` `latest` `openjdk-22.0` `openjdk-22`                             | June 6th     | `sha256:35de3a19a2982e97ac3db2895c7debe6ec73085a4c1debae825704ae0ce75bfa` |
|  `openjdk-14.0` `openjdk-14` `openjdk-14.0.2` `openjdk-14.0.2.12`                  | June 6th     | `sha256:693e76416d0e6dc4287d5f1ee2f97a1c7444d471de58c929111c3ed91881a556` |
|  `openjdk-15.0` `openjdk-15.0.10.5` `openjdk-15.0.10` `openjdk-15`                 | June 6th     | `sha256:e2a3a21f41346151d73f2c067bbf548989f5c658afd9c70c6fad132a629c5ead` |
|  `openjdk-16.0` `openjdk-16.0.2.7` `openjdk-16.0.2` `openjdk-16`                   | June 6th     | `sha256:abfae615f65e688fec931500f449c13add0df3c5b07e35190bd922cae5993a42` |
|  `openjdk-11.0.23` `openjdk-11.0` `openjdk-11`                                     | June 5th     | `sha256:4cb2b13c5f6c45c34d6af0235ccabd401154d76a07721a7f7258d9ae44804964` |
|  `openjdk-17.0.11` `openjdk-17.0` `openjdk-17`                                     | June 5th     | `sha256:523f4faffa753f57f83ceca057a745e7209a04bbe5b1afe966ae163c25cd2ffc` |
|  `openjdk-21.0` `openjdk-21` `openjdk-21.0.3`                                      | June 5th     | `sha256:93342b6a77952e18d974c2c26bf0ee57e29dea020429a94f1888b88bdd8758eb` |

