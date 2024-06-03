---
title: "jellyfin Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jellyfin Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-03 00:46:08
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/jellyfin/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/jellyfin/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/jellyfin/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/jellyfin/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 1st     | `sha256:0f50f4f8e6b90869c8b9fdc82b77eeb3841a5e8e50a8a54942b68a769d92af35` |
|  `latest`     | June 1st     | `sha256:0360fb65431457b81c4fc78f69af0e460a3484424b03797c88797b256e4f3af5` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `10.9-dev` `10-dev` `10.9.3-dev` `latest-dev` | June 1st     | `sha256:77933b64960723029598ceb8005c0af067a859a2515b0ceb60925d7b9bb2c6fc` |
|  `10.9.3` `10.9` `latest` `10`                 | June 1st     | `sha256:7a378f0a98841ca63905b7ca132d8542659f0087e7535b369a02aaa2a5362ce7` |
|  `10.9.2-dev`                                  | May 24th     | `sha256:b28b22939fe68732b929a311ae1e64a30b9ff6226876ad716588cdd5824c39ba` |
|  `10.9.2`                                      | May 24th     | `sha256:f8fb1b5fee58fd485a7b7d362d6b0c3dfefc42d67f101d688bef1770d8f67b37` |
|  `10.8.13-dev` `10.8-dev`                      | May 13th     | `sha256:b7038f768a1d862411699b8a81e933b41df1d36be0d82027cac07e4bbb6c47db` |
|  `10.8` `10.8.13`                              | May 13th     | `sha256:0f4b3f0412a642910da1a0b5030c9613cbc9dfbf1468739d60b5bbe4a3eb96d2` |

