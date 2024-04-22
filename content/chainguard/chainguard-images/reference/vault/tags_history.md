---
title: "vault Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the vault Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-22 00:45:38
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/vault/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/vault/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/vault/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/vault/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 21st   | `sha256:9b313c0cdd5a005a5eb3b72eb0d69e3ff4ebe757f6b9a4f8819c07f41b0a9349` |
|  `latest`     | April 21st   | `sha256:9c7c6c9cb6d98ebb9650e2fde9b9deb5a06cb6f34bc8d1004c1a38fd9c922536` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.13.13-dev` `1.13-dev`                      | April 21st   | `sha256:99ee5c308d6e29c22113a5f003cf7a4431e92e1f27663f908bce48a9caa878f0` |
|  `1.14.11-dev` `1.14-dev` `latest-dev` `1-dev` | April 21st   | `sha256:c1168eadff52e3e67e2163a1501f1cd174eb1955df7a5706aacf75ada99231ee` |
|  `1.14` `1.14.11` `1` `latest`                 | April 21st   | `sha256:797df5c9ea21e76a5635d467f6bfcba72b770bdc95f775e3f3517dfef627723c` |
|  `1.13.13` `1.13`                              | April 21st   | `sha256:acf82ac7be71a99faef1ba0fdc7362a7968be7849694b82c166781d3baae29f7` |
|  `1.14.10-dev`                                 | April 11th   | `sha256:cd051dd1c2ac090d69efc06da6cdb48fc7f2ee2d7e35a03992384ee5e32971af` |
|  `1.14.10`                                     | March 28th   | `sha256:e53f50a49ecf38393595171fc0acb1396b442dae0c1b0ca579dbfb80b643c574` |

