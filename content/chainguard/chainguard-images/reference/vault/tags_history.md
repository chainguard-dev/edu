---
title: "vault Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the vault Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-29 00:47:42
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
|  `latest`     | March 28th   | `sha256:7e9cf7926e07bc22fc0a2702c62294617150d262aba404adc92b358de8737d34` |
|  `latest-dev` | March 28th   | `sha256:63dcbdde532c349871301f5857a676919c43be087a2bf3404c6f7f0c417f9f7b` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.13` `1.13.13`                              | March 28th   | `sha256:6d59be0807b4cb738c4f300be9033903b4c51f4a190385d7110ae30be2a6b0c7` |
|  `1.13.13-dev` `1.13-dev`                      | March 28th   | `sha256:4faa327e1192e43848dfd6158502ff77c96e653754fdffa7938f9db2616b021a` |
|  `latest` `1` `1.14` `1.14.10`                 | March 28th   | `sha256:e53f50a49ecf38393595171fc0acb1396b442dae0c1b0ca579dbfb80b643c574` |
|  `1-dev` `1.14.10-dev` `latest-dev` `1.14-dev` | March 28th   | `sha256:694e1a07d50ca7cc0351834a258607e28641e7f4910209566079f190ae2e1f0d` |

