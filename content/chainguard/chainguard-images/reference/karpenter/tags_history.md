---
title: "karpenter Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the karpenter Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-25 00:53:12
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
|  `latest-dev` | April 22nd   | `sha256:0a1c795cdea0fff2e2ba015c74dc5b79f9da1760bc014e3040ca344c17e97ea9` |
|  `latest`     | April 11th   | `sha256:2fa1f66d366ae5d2f594c5942e6ed02007c2242ff7877c10a7f970a044ed35a5` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0.35-dev` `0.35.4-dev`                      | April 24th   | `sha256:09867b03568d076c0646a5e5e72279f55d5e1e1ac302e6aadec9d27fb5bf6a1e` |
|  `0` `0.36.0` `0.36` `latest`                 | April 24th   | `sha256:0f1a24830639d33071b2b664059e959446c245422e297d1e10767a05c8d45df5` |
|  `0.35.4` `0.35`                              | April 24th   | `sha256:034abc1b4bb7a96a9bc5a9c4ee7090e3ccb184dcdd9d1598f38c3329ae210ce0` |
|  `0.36.0-dev` `0.36-dev` `0-dev` `latest-dev` | April 24th   | `sha256:1b83625e12dddb2f149638a7285b740842a4170620be390641c328f205d033f2` |
|  `0.35.2-dev`                                 | April 2nd    | `sha256:74e3f2c40db018adab0ec934cb1089d3506d311bf1eec2e1a23d2953649660b1` |
|  `0.35.2`                                     | March 28th   | `sha256:8ec243996c11256ac91c346a1c44b2d5691d37584b410739e57920bd65d699e2` |
|  `0.27.2`                                     | April 19th   | `sha256:4920dd60eb95cc5ad09a92de21c100c4bfe6f10f9a1b493266009f2400294c73` |
|  `0.27.2-dev`                                 | April 19th   | `sha256:930f5d798690e11cfdede6413133fb4d96c03c7d502153060e267db2ef7373c4` |

