---
title: "nginx Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the nginx Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-26 00:35:03
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/nginx/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/nginx/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/nginx/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/nginx/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 24th    | `sha256:410be4c75991a13ef906f241d4fcfa3a8e1a2256b1cbe0ad6ad0396845728003` |
|  `latest`     | June 22nd    | `sha256:f0c926140831cde8a20bccd27cfe224c4d495fee3be66a2054b95f277283491c` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.26` `stable` `1.26.1`                     | June 25th    | `sha256:3f389af883260e114f5ec39337b598aa75890f18e6ba8c1b5c2498b8b3e2593d` |
|  `mainline` `1.27.0` `1` `latest` `1.27`      | June 25th    | `sha256:b88d1dd494cc00c9291ae22915a2311ba5e4cfca2897dec616e8bda847b94fa6` |
|  `1-dev` `1.27.0-dev` `latest-dev` `1.27-dev` | June 25th    | `sha256:26dc525f6cd05bebf5e17ac68de5a0954496705d8777a37fa0638bfc2aa0980c` |
|  `1.26-dev` `1.26.1-dev`                      | June 25th    | `sha256:031e4198384f6a1f4ebfbdb451b80ce2b52563f028f304d88071a0ddfdb533a5` |

