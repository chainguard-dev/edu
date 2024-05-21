---
title: "fluentd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the fluentd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-21 00:38:36
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/fluentd/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/fluentd/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/fluentd/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/fluentd/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)              | Last Changed | Digest                                                                    |
|----------------------|--------------|---------------------------------------------------------------------------|
|  `latest-splunk-dev` | May 20th     | `sha256:46cd3580a22b9e76e51f6324357076c9cd1aa07bbeb7b3be7857a123a9a2745b` |
|  `latest-dev`        | May 20th     | `sha256:3d11546bc0d32eeb5028c9a4274008e145c6d706e8d494c740cb493bf231724f` |
|  `latest`            | May 17th     | `sha256:f38b1e332a42b5759554e94bb800ba9db8b3c14631f89486c26bcb395798c771` |
|  `latest-splunk`     | May 17th     | `sha256:4ee6efb2258c6bc30bb49b0665d34ec5335300818792f59f35ee2b9169c6b23e` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                      | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.16-dev` `1.16.5-dev` `1-dev` `latest-dev`                                | May 19th     | `sha256:0dc37f7892ab11d1cd8eb68557f985139e029f427c44b4ac0a53915571c70569` |
|  `1.16.5-r0-splunk-dev` `1.16.5-splunk-dev` `1-splunk-dev` `1.16-splunk-dev` | May 19th     | `sha256:6d13a72f4e5d872aa72ebfd501925e702df8fa350670b91703048821f393bd0a` |
|  `1-splunk` `1.16-splunk` `1.16.5-r0-splunk` `1.16.5-splunk`                 | May 17th     | `sha256:2072d182ae588983bde502d00f1a65e24d965a85dcf2cad5446bf9a8c8e96598` |
|  `1` `1.16` `1.16.5` `latest`                                                | May 17th     | `sha256:e2ece8130c6b2c68a1ec8f68b26970d13d027ee479424b085c81f6426d45361d` |

