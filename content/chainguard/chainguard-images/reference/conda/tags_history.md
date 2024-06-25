---
title: "conda Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the conda Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-25 00:42:19
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/conda/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/conda/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/conda/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/conda/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 24th    | `sha256:1d2c13d8a274551c7993538fa095190a2df6ff0e4f33b75c06e8257f4a5e4779` |
|  `latest`     | June 24th    | `sha256:e9e58283af2f98aeac84033387e03909494f3a18d8678ad12db3ea8b9f4ee059` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `24.1.1-dev`                                  | June 23rd    | `sha256:5cc378d8637c21bf1bfd4dd8ece690fc461eac284819f482a07314a07175b884` |
|  `24.1.2-dev` `24.1-dev` `latest-dev` `24-dev` | June 23rd    | `sha256:3dfade7d2f6f29303f6b65bee4bb29b3d819f26078a29c1f175b8d85a943ec86` |
|  `24.1` `24` `latest` `24.1.2`                 | June 23rd    | `sha256:72705352c264d6d4e6a49ea91cfad1cd89b466629efe143ac6a17391facb776a` |
|  `24.5.0` `24.5`                               | June 23rd    | `sha256:49355b972a74fc42d10aaeb9d4044320020c93de3006fb1c9690da26e8a4bccb` |
|  `24.1.1`                                      | June 23rd    | `sha256:bc09cdf9043cc650ccc4b1d7bd5a2e622adda0e294ab3b059282dd161df2dcfe` |
|  `24.5.0-dev` `24.5-dev`                       | June 23rd    | `sha256:abfb2dbbd1df3d110ef16fb3d094904186c0d85561b42d782a0896bbf18d5ea4` |

