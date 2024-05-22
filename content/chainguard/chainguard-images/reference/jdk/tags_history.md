---
title: "jdk Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jdk Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-22 00:47:17
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
|  `latest-dev` | May 21st     | `sha256:03eac181e874af81b1093611d97e6449dfc71d6573816dadf47ed6bc8bc43445` |
|  `latest`     | May 21st     | `sha256:2857a5e627008ec155683eb2076b2fd4a37c1697cf1046f9174852414de03690` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-21.0.3-dev` `openjdk-21-dev` `openjdk-21.0-dev`                          | May 21st     | `sha256:cecdbdca88574d384e84ac3463b9d16b049b115267964a42cb3b5c2e34c4c170` |
|  `openjdk-17.0.11` `openjdk-17.0` `openjdk-17`                                     | May 21st     | `sha256:554a12d11dc3c79ac05c2419f28daa6710affcdae101b90eb61b9d66945db74f` |
|  `openjdk-14.0.2-dev` `openjdk-14-dev` `openjdk-14.0.2.12-dev` `openjdk-14.0-dev`  | May 21st     | `sha256:7a807050138007114824754f9b63cd4a7965cb89779521a73a5efa8ccfae2811` |
|  `openjdk-11` `openjdk-11.0` `openjdk-11.0.23`                                     | May 21st     | `sha256:9fee982ff617c1ade7ffb9b9abc9a4f3949394bd28d6271f7304642a2f4a6819` |
|  `openjdk-16.0.2` `openjdk-16.0.2.7` `openjdk-16` `openjdk-16.0`                   | May 21st     | `sha256:c6a1efb99fc4af238d15b91f27932dc007b73c891139545e1f9245b9d3a7c286` |
|  `openjdk-14.0` `openjdk-14.0.2.12` `openjdk-14.0.2` `openjdk-14`                  | May 21st     | `sha256:8b63389f28b0c5bb2e9951d8a9d264540e5e3b0c9321579350880cfe78054546` |
|  `openjdk-15.0.10-dev` `openjdk-15-dev` `openjdk-15.0-dev` `openjdk-15.0.10.5-dev` | May 21st     | `sha256:c856974861c7484cb886e108430e765f18373113e1901f929ba862f23cbf3b5f` |
|  `openjdk-21.0.3` `openjdk-21` `openjdk-21.0`                                      | May 21st     | `sha256:06d73ac56feeb3285741d46a8c7f21c6811011c4424d0a2fa5e12f72a59e0588` |
|  `openjdk-11.0-dev` `openjdk-11.0.23-dev` `openjdk-11-dev`                         | May 21st     | `sha256:01492bc3a29485f14442bd6c918c732c92c52f33c2d1ad494301969175f6ee19` |
|  `openjdk-16.0.2.7-dev` `openjdk-16-dev` `openjdk-16.0.2-dev` `openjdk-16.0-dev`   | May 21st     | `sha256:7b8f932c2a8850feaf5d5deffe1a2aee3d79350e887d5cade3fa79705eec196e` |
|  `openjdk-8.392-dev` `openjdk-8-dev` `openjdk-8.392.08-dev`                        | May 21st     | `sha256:e8198c5e10eb3cea1d6caf14960cb0784269cc55882ea3bb5e2c05b940048901` |
|  `openjdk-15.0` `openjdk-15` `openjdk-15.0.10` `openjdk-15.0.10.5`                 | May 21st     | `sha256:be912bd2394dd07f8608d38112e15961770d19be120cc43b5ff4938f0486d4b3` |
|  `openjdk-22.0.1-dev` `openjdk-22-dev` `latest-dev` `openjdk-22.0-dev`             | May 21st     | `sha256:acf3a78610ceae2dca5df8c334c155073650723e6bfe3d86a662d8e8ae905608` |
|  `openjdk-8.392` `openjdk-8` `openjdk-8.392.08`                                    | May 21st     | `sha256:beea58cdc6d52dbc3df66b00f8cb8bc250fba19a4f9e2ec8f585d025b39fb04c` |
|  `openjdk-17.0-dev` `openjdk-17.0.11-dev` `openjdk-17-dev`                         | May 21st     | `sha256:31e8410d016243effb8db686fa934bf8f4c47978f76dec76aba1a4a50a1a8452` |
|  `latest` `openjdk-22.0` `openjdk-22` `openjdk-22.0.1`                             | May 21st     | `sha256:6f87aaa169023a5bf59e204facf695d9f3827bbd0429083b890ebd812bd3816e` |
|  `openjdk-11.0.19.5-dev` `openjdk-11.0.19-dev`                                     | May 16th     | `sha256:892756bac53e2b57c43cd8b92d1790d223a18535e7186167dd65b41a51bdab7d` |
|  `openjdk-11.0.19.5` `openjdk-11.0.19`                                             | May 16th     | `sha256:4f282df7a3ebd9751b2372d077f7525f93f379e037cdf3b0d9cb3eb081fde668` |

