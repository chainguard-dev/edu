---
title: "vault Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the vault Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-05 00:36:13
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
|  `latest-dev` | June 2nd     | `sha256:a873af234cad221782367bad58e8a262a44048f68c04e1a07f7f7f735f8dbfb2` |
|  `latest`     | May 31st     | `sha256:27f8bd7517d7df0d6748e1ccd8d75e0d49cb3a9a5ea345968ae94fc03839199d` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.15-dev` `1.15.8-dev`                      | June 4th     | `sha256:aabb5d84ec5113829a5e8148580898b48f5f03ed39bad7662cc9c04d79842f9a` |
|  `1.15.8` `1.15`                              | June 4th     | `sha256:b9f00324aec4a8f3fae7e68fa3bbd26d4b689011bbff248d48cc60d67f8bf5a5` |
|  `1.16` `1` `latest` `1.16.3`                 | June 4th     | `sha256:daa26e339663c89db21d9a1173e77c04c0f2085c569e3adbbd6a78be80971112` |
|  `1.14.12` `1.14`                             | June 4th     | `sha256:70d7ea130f5c051aa19a2c86e1302cd9cd35214bd3546fa3050cbc45f942fadc` |
|  `1.14.12-dev` `1.14-dev`                     | June 4th     | `sha256:f4b2ae032c3dffb00de76c7c38f8d7f4bc4904b1183886b3305c2c078775c7c8` |
|  `1-dev` `latest-dev` `1.16-dev` `1.16.3-dev` | June 4th     | `sha256:a637d8810744ba2966c2f5cf39e21eb9fbdecdd2019ba364564af460f854f05e` |
|  `1.16.2-dev`                                 | June 1st     | `sha256:85725e757f182bc6867f8d3bfd667c06df6f3ea19bedf502002088fed57ac045` |

