---
title: "jellyfin Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jellyfin Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-28 00:45:11
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
|  `latest`     | May 27th     | `sha256:828d779811ce8e32dac0b0c7a2d67962a364f519ea9d1bf3b2a3cdaeb20759ac` |
|  `latest-dev` | April 29th   | `sha256:f5aa2ec95931e4363d4d8d523b62a735d8d2e7d5e13ce796bdefa9148e1ad7b0` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `10.9.3` `10.9` `10` `latest`                 | May 27th     | `sha256:961921b48dd375524e9a555500996ce9876bb3c9ddbae0cd73c27b9144a22978` |
|  `10.9.3-dev` `10-dev` `latest-dev` `10.9-dev` | May 27th     | `sha256:a3391e263d0e6861bef4a21540c1cbe65092e19b5f18767e3f58416e06a66ccf` |
|  `10.9.2-dev`                                  | May 24th     | `sha256:b28b22939fe68732b929a311ae1e64a30b9ff6226876ad716588cdd5824c39ba` |
|  `10.9.2`                                      | May 24th     | `sha256:f8fb1b5fee58fd485a7b7d362d6b0c3dfefc42d67f101d688bef1770d8f67b37` |
|  `10.8.13-dev` `10.8-dev`                      | May 13th     | `sha256:b7038f768a1d862411699b8a81e933b41df1d36be0d82027cac07e4bbb6c47db` |
|  `10.8` `10.8.13`                              | May 13th     | `sha256:0f4b3f0412a642910da1a0b5030c9613cbc9dfbf1468739d60b5bbe4a3eb96d2` |

