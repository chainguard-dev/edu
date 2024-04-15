---
title: "vault Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the vault Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-15 03:08:24
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
|  `latest`     | April 12th   | `sha256:0515b269499d12c07a1b61d1c6271e531172b891b5609ff1d4b369403861618c` |
|  `latest-dev` | April 12th   | `sha256:04ed29a24814a3199a5ee80e495483a8e23ca09f86f890c9e2400f06f411d65c` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.14.11-dev` `latest-dev` `1.14-dev` `1-dev` | April 12th   | `sha256:d52c69ea619852fdad43a0673c62ca509efa8dfd05e3766807b64a425776e404` |
|  `latest` `1.14` `1` `1.14.11`                 | April 12th   | `sha256:a67e449029f60b7f7f2b410ccf941db4338c59422161267811f394d44f4d141b` |
|  `1.13-dev` `1.13.13-dev`                      | April 11th   | `sha256:3e274a7ab017a2fa7d4ce519698c4d60a5b62e0da37d229878047dd92a407516` |
|  `1.14.10-dev`                                 | April 11th   | `sha256:cd051dd1c2ac090d69efc06da6cdb48fc7f2ee2d7e35a03992384ee5e32971af` |
|  `1.13` `1.13.13`                              | March 28th   | `sha256:6d59be0807b4cb738c4f300be9033903b4c51f4a190385d7110ae30be2a6b0c7` |
|  `1.14.10`                                     | March 28th   | `sha256:e53f50a49ecf38393595171fc0acb1396b442dae0c1b0ca579dbfb80b643c574` |

