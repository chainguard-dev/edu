---
title: "karpenter Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the karpenter Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-14 00:46:23
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
|  `latest-dev` | April 29th   | `sha256:83b4361f303033c68a916d0e3c94bf4407a7f410c504e2c403fbe3956b7eb5c3` |
|  `latest`     | April 26th   | `sha256:9bf50de7cb239835c36bbc713843b08d18aa8e3182d6867311bd560457a69f1e` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0.36.1-dev` `0.36-dev` `latest-dev` `0-dev` | May 13th     | `sha256:d3e936d536ea6bafedb7ed8175ad8b265b22ee56ecb17425449896d1f322917d` |
|  `0.35.4-dev` `0.35-dev`                      | May 13th     | `sha256:be6ce50c4f8e4b348c6c0789274b0491d8d6620424dadc5d3e6967336a23c2a6` |
|  `0.36.1` `0.36` `latest` `0`                 | May 10th     | `sha256:b74d197c1e28c2eda06ac445cbe8b66c1b90eb6436ac7c9815ebcaa083afbb16` |
|  `0.35.4` `0.35`                              | May 9th      | `sha256:eeed545c84c71a7b1be453adcd363203d23f124b16f9d2559d436f5c3fe8eb13` |
|  `0.36.0-dev`                                 | April 24th   | `sha256:1b83625e12dddb2f149638a7285b740842a4170620be390641c328f205d033f2` |
|  `0.36.0`                                     | April 24th   | `sha256:0f1a24830639d33071b2b664059e959446c245422e297d1e10767a05c8d45df5` |
|  `0.27.2`                                     | April 19th   | `sha256:4920dd60eb95cc5ad09a92de21c100c4bfe6f10f9a1b493266009f2400294c73` |
|  `0.27.2-dev`                                 | April 19th   | `sha256:930f5d798690e11cfdede6413133fb4d96c03c7d502153060e267db2ef7373c4` |

