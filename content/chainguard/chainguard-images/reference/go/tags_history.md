---
title: "go Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the go Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-15 00:39:35
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
|  `latest-dev` | April 29th   | `sha256:beee32faa83f4598019d2468b0d611c2163e3521fb8e090925f7ce9aa38ecb4f` |
|  `latest`     | April 29th   | `sha256:4d51574ef33b4edc57a22da062fe335a500eda30a1f1315cb39b4977bf2aef5f` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `1.22-dev` `1.22.3-dev` `1-dev` | May 14th     | `sha256:d5b4f3404b13cd37947d3eb6cf11c80d205863e18ea41e8957cb674b04f1613d` |
|  `1.18.10-dev` `1.18-dev`                     | May 14th     | `sha256:c778596f10e79383caac26a9296fa5bc77f9348d88669eed6da1bb5871e56571` |
|  `1.18.10` `1.18`                             | May 14th     | `sha256:55ee8e29b5ef40740427e253ffe188da6ea3eee7b4dbc8fec937ae167d3e1822` |
|  `1.20` `1.20.14`                             | May 14th     | `sha256:95877e3fe2675b42855f2f6a4020e6d3039ff3abd145a086452cb149c7099d1a` |
|  `1.17.13-dev` `1.17-dev`                     | May 14th     | `sha256:f7657b6eba7d99ce25085bf92cb3c04c2a94c3b45617c1c76f15f2aac18f3ff0` |
|  `1` `latest` `1.22.3` `1.22`                 | May 14th     | `sha256:71939ae99ae154befb3c49033302a72bd47cb4d9fb651c64adce915b38edc58f` |
|  `1.20-dev` `1.20.14-dev`                     | May 14th     | `sha256:56f93d7ed4bc6575720c61228f6b86566bc6e47323e8b6efceabafdd7c51287c` |
|  `1.17.13` `1.17`                             | May 14th     | `sha256:266bc3e98916e88e2653f4f0110d8a635b0e4d531ad7afd79defb34e260a4add` |
|  `1.19.13` `1.19`                             | May 14th     | `sha256:54bc1090705d99bfd41804096aa0036a4603f015a103df774711b47c4c20904f` |
|  `1.21.10` `1.21`                             | May 14th     | `sha256:836b4ad91c92add74411891a1223673082644d4ac11c26163d46ea0a86a9267d` |
|  `1.19.13-dev` `1.19-dev`                     | May 14th     | `sha256:c5f3dc305fd947fa4b05ed89e2b77f454d79b522c6463ea56f04d3ec9d2a3f3c` |
|  `1.21.10-dev` `1.21-dev`                     | May 14th     | `sha256:99e30c3874e37bf91c78bcdb8de5a331ea73ff9facd0257771499db92b189bf3` |
|  `1.21.9`                                     | May 2nd      | `sha256:5d9d7e9964c94a6e9c3ee76aec4c7ee8241270a84b6aa0117bc9f36eea1c1c5f` |
|  `1.22.2`                                     | May 2nd      | `sha256:5664b8cd131b8d8002ab658debb989e74504a0a63cc6c8b5e5b634612d61df84` |
|  `1.22.2-dev`                                 | May 2nd      | `sha256:7803a5c3307994c91c1a32e36cd01b32b82c32babb952599aefdd0ed827c3e89` |
|  `1.21.9-dev`                                 | May 2nd      | `sha256:adf5aa4cb4542297930f03c44e0539ae89acdc8e565c26fffee6dca569e5891b` |
|  `1.19.8`                                     | May 2nd      | `sha256:06838d22698818b0efe3dfaae3734464070be3061e379266f6c710728b22cb54` |
|  `1.20.3-dev`                                 | May 2nd      | `sha256:7723d919c3839a569d534c74f719cd02232ad13e4a1185a381909422f2e87c8c` |
|  `1.19.8-dev`                                 | May 2nd      | `sha256:eb613f6a2cdfb70c5d50be5d9183b575754ec83fee35e8f62d7cb02b7875bbb2` |
|  `1.20.3`                                     | May 2nd      | `sha256:47a6d2a9faeaa739803fa495ef0721055a24142ebd1f0ab4e2306b6cebf860d1` |

