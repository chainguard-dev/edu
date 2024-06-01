---
title: "go Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the go Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-01 00:50:07
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/go/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/go/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/go/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/go/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 31st     | `sha256:6e93d99d5f5c246ccf7e0b2329fb7787def11dd569eb572222c796e87cff4de0` |
|  `latest`     | May 31st     | `sha256:4727ccbcce136929829a263371444a44229e9e923692eec4eba78a9523a276ef` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.18-dev` `1.18.10-dev`                     | May 30th     | `sha256:5d275f6232886bdaa43851145d200055a724c8a161fc5050c0f8477b3faed8e2` |
|  `1.19` `1.19.13`                             | May 30th     | `sha256:82c4b878d50b83c0bed2cc0d47b3542953ab72f9972178594ff3375028d1b6f0` |
|  `1.22-dev` `1.22.3-dev` `1-dev` `latest-dev` | May 30th     | `sha256:45e2e5032226eb7d86bab6d36545ed7ba005d185214d338b807ee016b6c00b3b` |
|  `1.22.3` `latest` `1` `1.22`                 | May 30th     | `sha256:66c811cbdec25f535cc09ba91ec0a84d3f32b9edb8a2a5fe5bda3f414652dcc7` |
|  `1.21.10-dev` `1.21-dev`                     | May 30th     | `sha256:83db971462d884118e697ac95f2585c4e6280b19cec1c7703eac3a12addf15f2` |
|  `1.17.13` `1.17`                             | May 30th     | `sha256:f770e51adcb918c38f215de2b2906379e6dfcacd966d61f543f7e65ba4c250d1` |
|  `1.18.10` `1.18`                             | May 30th     | `sha256:7323ecccefdbd8613dd76dd84f2077bb9270b4116ed8deb1772e79a9e71c7d43` |
|  `1.21.10` `1.21`                             | May 30th     | `sha256:aca4196918dffb2886d22a8ff2f29f473b2a7238919b6ba1c382bb009ebab109` |
|  `1.20.14-dev` `1.20-dev`                     | May 30th     | `sha256:a187407d11528c32ae9b5ed6e80b58e5496ef41ba946fc260a4da8bb145a458d` |
|  `1.20.14` `1.20`                             | May 30th     | `sha256:19b95132f38432a31e7601959baed35f89a570b2354492298d6bddf6d1ed879e` |
|  `1.17-dev` `1.17.13-dev`                     | May 30th     | `sha256:ca76c92333db8933b5e2fa5601d788ca6254379d0ed04ce03be2cd475a7e43fa` |
|  `1.19-dev` `1.19.13-dev`                     | May 30th     | `sha256:db44057e4c39ff981a1ca8cc8cd1e4404ed82dafa954d46df5d462826faa5b1e` |
|  `1.21.9`                                     | May 2nd      | `sha256:5d9d7e9964c94a6e9c3ee76aec4c7ee8241270a84b6aa0117bc9f36eea1c1c5f` |
|  `1.22.2`                                     | May 2nd      | `sha256:5664b8cd131b8d8002ab658debb989e74504a0a63cc6c8b5e5b634612d61df84` |
|  `1.22.2-dev`                                 | May 2nd      | `sha256:7803a5c3307994c91c1a32e36cd01b32b82c32babb952599aefdd0ed827c3e89` |
|  `1.21.9-dev`                                 | May 2nd      | `sha256:adf5aa4cb4542297930f03c44e0539ae89acdc8e565c26fffee6dca569e5891b` |
|  `1.19.8`                                     | May 2nd      | `sha256:06838d22698818b0efe3dfaae3734464070be3061e379266f6c710728b22cb54` |
|  `1.20.3-dev`                                 | May 2nd      | `sha256:7723d919c3839a569d534c74f719cd02232ad13e4a1185a381909422f2e87c8c` |
|  `1.19.8-dev`                                 | May 2nd      | `sha256:eb613f6a2cdfb70c5d50be5d9183b575754ec83fee35e8f62d7cb02b7875bbb2` |
|  `1.20.3`                                     | May 2nd      | `sha256:47a6d2a9faeaa739803fa495ef0721055a24142ebd1f0ab4e2306b6cebf860d1` |

