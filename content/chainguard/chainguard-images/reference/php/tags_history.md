---
title: "php Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the php Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-10 00:50:47
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/php/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/php/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/php/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/php/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)           | Last Changed | Digest                                                                    |
|-------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev`     | June 9th     | `sha256:14ac3043b57c96f40e850cf86bb6632dd26ab79ef09600e02b34f720e4c12d63` |
|  `latest-fpm-dev` | June 9th     | `sha256:02fb5915dc19c733d0ecbf59981773257aa83f8b6fdd54d4c77848faa51574a8` |
|  `latest`         | June 5th     | `sha256:7d30da5d239a96ba98fff600ea1d3d743283292ec23c8bd2b823d387cca639f2` |
|  `latest-fpm`     | June 5th     | `sha256:e1659c6562cd6f604103bf1a83b8acb309fdf14e384b5a7840c81010d781d125` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                          | Last Changed | Digest                                                                    |
|----------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `8-fpm-dev` `8.2.20-r0-fpm-dev` `8.2.20-fpm-dev` `8.2-fpm-dev` `latest-fpm-dev` | June 8th     | `sha256:9bedca59ef16fa48eb95da9983251d5784f02594e1875196a04296502f746bdf` |
|  `8.2.20-dev` `8.2-dev` `8-dev` `latest-dev`                                     | June 8th     | `sha256:21735b320477b7c9481bb8c08a7eea5d96a42f9447108768dc53d98bd407f34f` |
|  `latest` `8.2.20` `8` `8.2`                                                     | June 5th     | `sha256:9ba8e099155a150be82ebdd2995cf627eec8630c508a0db8ea2a73f176dd649e` |
|  `8.2-fpm` `latest-fpm` `8.2.20-fpm` `8-fpm` `8.2.20-r0-fpm`                     | June 5th     | `sha256:95195f0912f0f4fcaf42ccd4a371d9b8f2008268381c66dfeb49b157e0701341` |

