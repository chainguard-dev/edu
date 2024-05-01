---
title: "gatekeeper Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the gatekeeper Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-01 00:46:56
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/gatekeeper/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/gatekeeper/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/gatekeeper/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/gatekeeper/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 29th   | `sha256:8fda4e163563d17db0f5633bfbc203024b348da4bb4c5ce34876bc91e02de90e` |
|  `latest`     | April 21st   | `sha256:991a66ae28c5cf2cf28d3ab1ae5443aa02e9cf23f83f4e49706236d8299682eb` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `3.13.4-dev` `3.13-dev`                      | April 30th   | `sha256:5c2c0738a17770f577bd84d779fccfaaeda3f58d9d8b505795c8a84bb4b8a50d` |
|  `3-dev` `latest-dev` `3.15-dev` `3.15.1-dev` | April 30th   | `sha256:f53f750114f7bed387dbfef479e4d0b68d3002257fdf4d26ba5a358fe91bfdf1` |
|  `3.12-dev` `3.12.0-dev`                      | April 30th   | `sha256:322b879ec820c213a0b770d025cb91ceed3a3cd149e4e498dc6f7524357a8ff0` |
|  `3.14-dev` `3.14.1-dev`                      | April 30th   | `sha256:fc59e3867947b1737810f3458c236ca8a51af4d725080371078bd7739a614a76` |
|  `3.13.4` `3.13`                              | April 23rd   | `sha256:67e29847341edd4c7764070d45f7c7ba5b3780c07f2cd7bad757fc5e4b56b0bc` |
|  `3.15.1` `latest` `3.15` `3`                 | April 22nd   | `sha256:b0c2164576f26f142c5f63d0cadf67e07fb5ec31ca025f836a2ad62278e0ef62` |
|  `3.12` `3.12.0`                              | April 21st   | `sha256:993bd3e4e14fad421815e30350231596d21f5095a5883fe2f4e7672d5e462a83` |
|  `3.14` `3.14.1`                              | April 21st   | `sha256:3c6be7aed8348cc86839f6c52f75f8b63ffe62516f7d7ea6eddae237173b440c` |

