---
title: "jre Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jre Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-24 00:45:45
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
|  `latest`     | May 23rd     | `sha256:60a5ced9abd4c678c15f98049db141f96a2a46c364cb0893cc585eb2f1a65916` |
|  `latest-dev` | May 23rd     | `sha256:229f3ab1b923e7890f4ffccb7b019e620419393f6d2619c7d35e2c0d5e12cb86` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-11.0-dev` `openjdk-11-dev` `openjdk-11.0.23-dev`                         | May 23rd     | `sha256:c024219f03cd55aaacb41b707098f50980aa0acb87949630b24f585a77b70f06` |
|  `openjdk-8.392` `openjdk-8.392.08` `openjdk-8`                                    | May 23rd     | `sha256:70d52aad2bed070508fe97a1783af67e24c39f34fdf19e7bfdb3ffd69617380b` |
|  `openjdk-22` `openjdk-22.0` `latest` `openjdk-22.0.1`                             | May 23rd     | `sha256:add2aa4d739e94e73fdb442b9dfb3b77eeb463f768f51bed532e01672833be60` |
|  `openjdk-16.0.2` `openjdk-16.0` `openjdk-16` `openjdk-16.0.2.7`                   | May 23rd     | `sha256:8aa1a96c1f0c46d8f9cb6823dba2b5b18da85d0d95ecb0f5d2a999e3694ff274` |
|  `openjdk-22.0-dev` `openjdk-22-dev` `openjdk-22.0.1-dev` `latest-dev`             | May 23rd     | `sha256:c0678a2cd0c02b73529429779bf190a70f23159225af3347b3433d06dc8b228e` |
|  `openjdk-11.0` `openjdk-11` `openjdk-11.0.23`                                     | May 23rd     | `sha256:0aed86fe2e76bbfb90ca55e41dec8919bdddd87c5a1286464bb634e95b5dae0e` |
|  `openjdk-21.0-dev` `openjdk-21-dev` `openjdk-21.0.3-dev`                          | May 23rd     | `sha256:e8bb4f6c7b7f141e38c65944ba29477aa09ae60ca989700b93864beffc842c93` |
|  `openjdk-16-dev` `openjdk-16.0-dev` `openjdk-16.0.2.7-dev` `openjdk-16.0.2-dev`   | May 23rd     | `sha256:0120cb8e3553f88ce09ba0d6c5ecd42e1f7fec2887c0e0c4181f536185a8cbf3` |
|  `openjdk-15.0.10` `openjdk-15.0.10.5` `openjdk-15` `openjdk-15.0`                 | May 23rd     | `sha256:ff8e5ea9b875c57f66de914c154f5013c4de592fe94b382b9ed0240004193110` |
|  `openjdk-21` `openjdk-21.0` `openjdk-21.0.3`                                      | May 23rd     | `sha256:0185e9fa55ebaf8df96e4986d03903de2c3d09ee873de59ed8e4b16c29b0acc0` |
|  `openjdk-15.0.10-dev` `openjdk-15-dev` `openjdk-15.0.10.5-dev` `openjdk-15.0-dev` | May 23rd     | `sha256:c2656bfc5e905efc45e03e2f427031e3b9c03e4ef690d9fa5ec74c918dcf7436` |
|  `openjdk-8.392.08-dev` `openjdk-8.392-dev` `openjdk-8-dev`                        | May 23rd     | `sha256:f406cc211632cadd20a776a6e076f04e1ec021095aeb5c3d5b58caf0b2b2d138` |
|  `openjdk-17-dev` `openjdk-17.0-dev` `openjdk-17.0.11-dev`                         | May 23rd     | `sha256:60a3f0ce409b40a9ab41713caa6f2a7728b4bfd4b258d9bc3084372a0b7c8cb7` |
|  `openjdk-17.0.11` `openjdk-17.0` `openjdk-17`                                     | May 23rd     | `sha256:0f6d771f9baa698958ab06a51e0951081ede3f65543a5831eb32c296e3d4187e` |
|  `openjdk-14.0.2` `openjdk-14.0` `openjdk-14.0.2.12` `openjdk-14`                  | May 23rd     | `sha256:6e59a4143fe01c47bd06ac764ff476b8d7641dfd4a59c6f6b2944cae1b34fdd9` |
|  `openjdk-14-dev` `openjdk-14.0.2-dev` `openjdk-14.0.2.12-dev` `openjdk-14.0-dev`  | May 23rd     | `sha256:5dd588369efd39c67494b01e2ac95cb00a1dd3558a39570616f4a3bfcfdf26fd` |
|  `openjdk11.0.19.5` `openjdk11.0.19`                                               | May 16th     | `sha256:677dee78db811af812e1bb2bd33c1f247a5a4e0418169c194d965fc618768bba` |
|  `openjdk11.0.19.5-dev` `openjdk11.0.19-dev`                                       | May 16th     | `sha256:30327ab04c691b2d4f2bfa4391531384ea89b4e204cc65b90eee78a5cbc83156` |

