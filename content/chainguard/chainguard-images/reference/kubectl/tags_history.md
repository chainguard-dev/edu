---
title: "kubectl Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the kubectl Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-02-29 16:25:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/kubectl/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/kubectl/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/kubectl/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kubectl/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed  | Digest                                                                    |
|---------------|---------------|---------------------------------------------------------------------------|
|  `latest-dev` | February 27th | `sha256:17125754a06da0c3f8dfd011424367ba374df2ac36dc2fd5b7358cdf85b8666d` |
|  `latest`     | February 27th | `sha256:568f0ff915f0e7e96be1ac75555b261def54bbaf0c707b37fd17acb3406bb8f0` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **[Production Images](https://www.chainguard.dev/chainguard-images)**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed  | Digest                                                                    |
|-----------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `1.28-dev` `1.28.7-dev`                      | February 26th | `sha256:759eb07db8b975a8eb99008f656b6325355588e19a9bb2550fa1f0e1d12714cb` |
|  `1.25` `1.25.16`                             | February 26th | `sha256:ed21c317f3a3a8dcd25ff3d4a36514a1044f8327cb7a5e2c207373fbf027194a` |
|  `1.26.14-dev` `1.26-dev`                     | February 26th | `sha256:2e6f937ba3ed4e90c99b2b47dcd6d8c79d2c97de74aab075698b662e4d782bc8` |
|  `1.25-dev` `1.25.16-dev`                     | February 26th | `sha256:44a8b16907a9c2fb69b558dd6c373fc98db9b194f34c44e7931619a416c8bfd0` |
|  `1.29-dev` `1.29.2-dev` `latest-dev` `1-dev` | February 26th | `sha256:2912589142002685df0408ca7b9b2faa83ffa4f899235282941620b96a2b22c4` |
|  `1.26` `1.26.14`                             | February 26th | `sha256:4138730fe5df265ddd51e65652c541907ec2d699a53e3ef70a67934f3d8f40b6` |
|  `1.28` `1.28.7`                              | February 26th | `sha256:5223421d6e595685794f8653a30259e5799aa81640fb16a101f5db4ec2a2565e` |
|  `1.27-dev` `1.27.11-dev`                     | February 26th | `sha256:a526848ea6ca130e3fa3f06cdec24c50915ec9110f241efbd78b7ff6e4c5535f` |
|  `1.27.11` `1.27`                             | February 26th | `sha256:7f4979e85e88624fe26814e5b369782faf97407afcef3677dc584e238678fafa` |
|  `1` `1.29.2` `1.29` `latest`                 | February 26th | `sha256:431b79f73a1a4eedfb60cc95f8393c3622a659ebc3a2de87b3218cf68f8ab90b` |
|  `1.26.13-dev`                                | February 17th | `sha256:2ae722999708e44d507b7338e57a42de657edb3fb321526ffa66830a29559a09` |
|  `1.27.10-dev`                                | February 17th | `sha256:35f684370397299d9af404a9d30f3407213c22647760485406c4b9b70ab5548a` |
|  `1.29.1-dev`                                 | February 17th | `sha256:83b7f0f5c3edb3b043aad9348d86793f37e791b04a244bed404d3ca92e1db5c8` |
|  `1.28.6-dev`                                 | February 17th | `sha256:60e8ddc6d1670b2c139fc4f4e1176b166e85198a9ff7b9f201a7e0216d8e6932` |
|  `1.29.1`                                     | February 15th | `sha256:8673097f34047be48558d875c9f7773cb32df6256a621a29156dffb0f8532fc8` |
|  `1.26.13`                                    | February 5th  | `sha256:8f14d8dd7b72931dca970144ef109d90e09e815f1a94b8b0ee9d0f6c83095ffc` |
|  `1.27.10`                                    | February 5th  | `sha256:643409336c619f4647f534e913ff80a88f30a67a64a925979448a3da6cf9cbeb` |
|  `1.28.6`                                     | February 5th  | `sha256:00f2cc2d6fe7cac208febeee271ebd43020de911ad47970fa2acf5b60a36a6f6` |

