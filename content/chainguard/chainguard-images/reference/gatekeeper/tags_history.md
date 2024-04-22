---
title: "gatekeeper Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the gatekeeper Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-22 00:45:38
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
|  `latest`     | April 21st   | `sha256:991a66ae28c5cf2cf28d3ab1ae5443aa02e9cf23f83f4e49706236d8299682eb` |
|  `latest-dev` | April 21st   | `sha256:da879cffae468a51699f1ea729bcc9a249a7be240d7ecc4369f39e8d25ea6e94` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `3-dev` `3.14.1-dev` `3.14-dev` | April 21st   | `sha256:bb4a70fee00810b883280fb52fff97157d99a5a55c1d47486f77c9fba65eb80d` |
|  `3.12` `3.12.0`                              | April 21st   | `sha256:993bd3e4e14fad421815e30350231596d21f5095a5883fe2f4e7672d5e462a83` |
|  `3.13.4` `3.13`                              | April 21st   | `sha256:0e30065020148ff2349367e0fcd7c6b57f6ec0a310efb5a9f5e6d47448b3afd1` |
|  `3.14` `3.14.1` `latest` `3`                 | April 21st   | `sha256:3c6be7aed8348cc86839f6c52f75f8b63ffe62516f7d7ea6eddae237173b440c` |
|  `3.13-dev` `3.13.4-dev`                      | April 21st   | `sha256:5f9139db14102504ac7f3e5f5069f9c3dd76a02c849a65f8bfa54880853896eb` |
|  `3.12-dev` `3.12.0-dev`                      | April 21st   | `sha256:35d5e68e19cbdee86dbef563bb51f4dd2c02f39eb393c4031b8c11c84bcd8f3e` |

