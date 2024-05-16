---
title: "go Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the go Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-16 00:37:58
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
|  `latest-dev` | May 15th     | `sha256:1a0be8a99b5d4dd4d3cdddb18dd608762a040be613cceb16ef02911b92adc641` |
|  `latest`     | May 15th     | `sha256:6011c1778c16972f52b9c840bf668b23973e5cdfa5ad09ce24af6c76673bc492` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.18-dev` `1.18.10-dev`                     | May 15th     | `sha256:e82bfb8ab762ad3f9cb39dc711310ee14bd6bf1003135b530d133e945233ecba` |
|  `1.18` `1.18.10`                             | May 15th     | `sha256:df43ac858e4ed9e1a0d007424a73c4c154ed137f89e4b6876cbf75fae1f039ea` |
|  `1.17` `1.17.13`                             | May 15th     | `sha256:d271bbc3a9c6179daa00df19e38bbeafcef0243322ef3aa82fa4d1422e8b1bb2` |
|  `1.19.13` `1.19`                             | May 15th     | `sha256:4257a2cfe86acedb0b20ea9828e488adc950c63f074ad95a8d3202b99caed312` |
|  `1.22.3` `1.22` `1` `latest`                 | May 15th     | `sha256:a14dd990fdb5852b0d5c1ba5a6dfbc193464305148fc4463cd184b580e11c218` |
|  `1.20.14` `1.20`                             | May 15th     | `sha256:61def3f272b1c8a36809fb1a7af35275b61fc509dcc1fc7150059f731abd49a4` |
|  `1-dev` `1.22-dev` `latest-dev` `1.22.3-dev` | May 15th     | `sha256:f5922a22e1384b0dc6fdedc07822b701448750ac939d3ef9c57150d796c79e0a` |
|  `1.21.10` `1.21`                             | May 15th     | `sha256:cda5c83172e8d1aaa7db98d4388d80214b2c74ef1415d2b112c4ff5bd90fc155` |
|  `1.19.13-dev` `1.19-dev`                     | May 15th     | `sha256:35c6db5fba64b5b1e3719be5eadd7cac81e64df4edcdab50419d941f3b09ebb5` |
|  `1.20-dev` `1.20.14-dev`                     | May 15th     | `sha256:ad33a3e3760879126653c78beeaa5c4f3df3322b8326c2b005b269deedb87d0b` |
|  `1.21.10-dev` `1.21-dev`                     | May 15th     | `sha256:3693fc0ba00f194bff95c786fece7e6cf850fd81a338d60bfaf1157b3ce4e8be` |
|  `1.17-dev` `1.17.13-dev`                     | May 15th     | `sha256:5d77ca98edcfd2417ab55b7ab40f09be0440bab98ab1ef897bb055aaeff86bc4` |
|  `1.21.9`                                     | May 2nd      | `sha256:5d9d7e9964c94a6e9c3ee76aec4c7ee8241270a84b6aa0117bc9f36eea1c1c5f` |
|  `1.22.2`                                     | May 2nd      | `sha256:5664b8cd131b8d8002ab658debb989e74504a0a63cc6c8b5e5b634612d61df84` |
|  `1.22.2-dev`                                 | May 2nd      | `sha256:7803a5c3307994c91c1a32e36cd01b32b82c32babb952599aefdd0ed827c3e89` |
|  `1.21.9-dev`                                 | May 2nd      | `sha256:adf5aa4cb4542297930f03c44e0539ae89acdc8e565c26fffee6dca569e5891b` |
|  `1.19.8`                                     | May 2nd      | `sha256:06838d22698818b0efe3dfaae3734464070be3061e379266f6c710728b22cb54` |
|  `1.20.3-dev`                                 | May 2nd      | `sha256:7723d919c3839a569d534c74f719cd02232ad13e4a1185a381909422f2e87c8c` |
|  `1.19.8-dev`                                 | May 2nd      | `sha256:eb613f6a2cdfb70c5d50be5d9183b575754ec83fee35e8f62d7cb02b7875bbb2` |
|  `1.20.3`                                     | May 2nd      | `sha256:47a6d2a9faeaa739803fa495ef0721055a24142ebd1f0ab4e2306b6cebf860d1` |

