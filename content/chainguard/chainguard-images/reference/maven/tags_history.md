---
title: "maven Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the maven Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-01 00:46:56
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/maven/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/maven/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/maven/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/maven/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)                        | Last Changed | Digest                                                                    |
|--------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-21` `latest`         | April 30th   | `sha256:ea87034d96a17a3bc1796f18be59f963eca847a0a4b22b358229521d25b345ec` |
|  `openjdk-21-dev` `latest-dev` | April 30th   | `sha256:db98058f9c8ac9479b063811f96aff61b76b8ed39e46e22b2cc3e2f6c1241609` |
|  `openjdk-11-dev`              | April 30th   | `sha256:74aaa9cca8827a11338bf3a8617f25d183e3d5b2e78dde356a83e8fff79e591b` |
|  `openjdk-17-dev`              | April 30th   | `sha256:9a43964d0a75d28412014fdd3740572b00a8cec779ee3d2c1ef047924efaf2f3` |
|  `openjdk-11`                  | April 30th   | `sha256:a8ae40e07eee53fd2f06cd71638abdaec9492da918854ccd1d26617e5994dd87` |
|  `openjdk-17`                  | April 30th   | `sha256:207acaadc274a237be9245726d647f63a6b2b9addc73ce109e5e51c547f2eddb` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-17-3-dev` `openjdk-17-3.9.6-dev` `openjdk-17-dev` `openjdk-17-3.9-dev`              | April 30th   | `sha256:a2b4f55c5d1a1db3bb38a499b6e31e7d2e89848c399f944bc7c05bd2226c1061` |
|  `latest` `openjdk-21` `openjdk-21-3.9` `openjdk-21-3` `openjdk-21-3.9.6`                     | April 30th   | `sha256:be58f854a756429b059afb24051ce293405bc8b824d6cb5ad957f6a4f7e605b1` |
|  `openjdk-11-3-dev` `openjdk-11-3.9-dev` `openjdk-11-dev` `openjdk-11-3.9.6-dev`              | April 30th   | `sha256:a56a37cb808966a72b5f4df895d59ebd508ce38912d274fa79f20a3699ae0535` |
|  `latest-dev` `openjdk-21-3.9-dev` `openjdk-21-3-dev` `openjdk-21-dev` `openjdk-21-3.9.6-dev` | April 30th   | `sha256:61f3fad0da532afa72cb11cf5b9602293e217d36605cea098c07394a76a8d3fc` |
|  `openjdk-17-3.9` `openjdk-17-3` `openjdk-17` `openjdk-17-3.9.6`                              | April 30th   | `sha256:3e54b024a2ba126f52a9d653f99476b7b5bf5d146f629aeb7eed4f45bbc2b092` |
|  `openjdk-11-3.9.6` `openjdk-11-3.9` `openjdk-11` `openjdk-11-3`                              | April 30th   | `sha256:5de38d0b6bc52dc192bc1203d54ab2b7c51adb1f3e9e1d5a83105e3d1c38e1bb` |

