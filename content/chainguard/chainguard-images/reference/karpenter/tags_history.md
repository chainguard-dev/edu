---
title: "karpenter Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the karpenter Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-17 00:44:46
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/karpenter/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/karpenter/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/karpenter/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/karpenter/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 16th     | `sha256:026fa6050153b909ff3cfe125b553431ef8d845f876849d690cb4b17995c3791` |
|  `latest`     | May 15th     | `sha256:588c7a7829f87ce2b2c8c215c5f185edffe23a6e80e25eaaf9b73d8a19959d05` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0.35.4-dev` `0.35-dev`                      | May 16th     | `sha256:10fca4ea580d6b957785a0f616c63947df81626a9331659841e10446c03b4a25` |
|  `0-dev` `0.36.1-dev` `latest-dev` `0.36-dev` | May 16th     | `sha256:9a9eb15272dde90295f85a11e9cfad6c713ce66c69e2061c153362a28b197a77` |
|  `0.36` `latest` `0` `0.36.1`                 | May 15th     | `sha256:1711bdf42c476eff4391f2de277e096d542068050660158ed76d6d8a17052023` |
|  `0.35.4` `0.35`                              | May 15th     | `sha256:d3dca661f8ca83b2c55d83d63af0df43da4c7a7a0d45c9846350a609219dbaf5` |
|  `0.36.0-dev`                                 | April 24th   | `sha256:1b83625e12dddb2f149638a7285b740842a4170620be390641c328f205d033f2` |
|  `0.36.0`                                     | April 24th   | `sha256:0f1a24830639d33071b2b664059e959446c245422e297d1e10767a05c8d45df5` |
|  `0.27.2`                                     | April 19th   | `sha256:4920dd60eb95cc5ad09a92de21c100c4bfe6f10f9a1b493266009f2400294c73` |
|  `0.27.2-dev`                                 | April 19th   | `sha256:930f5d798690e11cfdede6413133fb4d96c03c7d502153060e267db2ef7373c4` |

