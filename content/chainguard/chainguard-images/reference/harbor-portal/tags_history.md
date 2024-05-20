---
title: "harbor-portal Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the harbor-portal Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-20 00:48:18
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/harbor-portal/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/harbor-portal/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/harbor-portal/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/harbor-portal/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | May 17th     | `sha256:8755b99fa9e97a2264873d1f6afd38eb8a2380dc7a0c74d0409128f041a76d5a` |
|  `latest-dev` | May 17th     | `sha256:db3c10c05c38686994f88a86232652f3e5ef9bbc5a1fafd868121e0c395b1bf7` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2-dev` `2.10-dev` `latest-dev` `2.10.2-dev` | May 19th     | `sha256:de20166d15c23808c6f5e9fd0def09cfcc1a732bf7c032c9db8f1e514ed75ab2` |
|  `2.9-dev` `2.9.4-dev`                        | May 19th     | `sha256:ee8d94116582afca18269fda95f7040ccb642dbc076cd4cd858b41fdc8c2da2b` |
|  `2.8.6-dev` `2.8-dev`                        | May 19th     | `sha256:5423dd3845ec26466c7834cd9b4fb1c640a24c85524e00927554e7fdac0a78e8` |
|  `latest` `2` `2.10` `2.10.2`                 | May 17th     | `sha256:3fa2a2e8b76e721c5a0e97dbf4efa6fe59907e0b7adb8279af787b18e8acf0b3` |
|  `2.8` `2.8.6`                                | May 17th     | `sha256:b3d864f2c7d17d9db47fb3c98d060350de6dc60c2e8e29cbfc1c30048ab84375` |
|  `2.9.4` `2.9`                                | May 17th     | `sha256:04a85b011dd27c62e273ad6ff8a25de01c73995dee0dbc912a3085186fe5b022` |
|  `2.8.5`                                      | April 21st   | `sha256:4df8e44c5b258219ce9e324cece03401fb6a0814a35b592888649425ca13b1ce` |
|  `2.8.5-dev`                                  | April 21st   | `sha256:3ddcdd0f256a6587e5e9cb3054c1b4b4210970d0e7529c27cf8caf8e23b460a5` |

