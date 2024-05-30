---
title: "dependency-track Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the dependency-track Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-30 00:47:59
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/dependency-track/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/dependency-track/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/dependency-track/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/dependency-track/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 29th     | `sha256:7a77b83a1f1a7886e5dc068c604d0e7d62f70bf05cdfee66ce9d5d49bd7eff8e` |
|  `latest`     | May 29th     | `sha256:4dad881f0dba474c8fabde6b7bfd1ecaeac4a4b400a5154102cf7732f7956529` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `4.11-dev` `4.11.1-dev` `latest-dev` `4-dev` | May 29th     | `sha256:b6513c900cfaabad828ad7654021476bd97097f1d6f5d310afbaa91a36de5f83` |
|  `4.11.1` `4.11` `4` `latest`                 | May 29th     | `sha256:b8bfc088edffd906b5fb15e9e3f9899cbb6cb9ec859d9bb3cfbaa2c5886107fa` |
|  `4.11.0`                                     | May 17th     | `sha256:006f45332a04ecd3c06f0eb9154c83efcb2d1d52f8a234598131d18e52385659` |
|  `4.11.0-dev`                                 | May 17th     | `sha256:1898d230cb795e6c56906d31b870992fd25ce537fdcb432eb53331a9f49ff23e` |
|  `4.10-dev` `4.10.1-dev`                      | May 2nd      | `sha256:c274b306b668e2d2a37122c866e927b6e574fdd6b669f137befae732c3d61fbb` |
|  `4.10.1` `4.10`                              | May 2nd      | `sha256:1d19779826424532fdd25332cdfa169d9909f037d015d4b606def95696e538d4` |

