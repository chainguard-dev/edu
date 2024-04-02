---
title: "hugo Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the hugo Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-02 00:36:12
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/hugo/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/hugo/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/hugo/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/hugo/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 1st    | `sha256:6c8ef7dcc5da1e67f9dd5ae86a1574cd04791d974cec72cdb41c177c73a00a0a` |
|  `latest`     | March 28th   | `sha256:8a534a113ce3a9ab45aa71b4e650eb6e896cd3b5de2dbad2532df1ed2ca508ed` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                         | Last Changed | Digest                                                                    |
|-------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0.124-dev` `0-dev` `latest-dev` `0.124.1-dev` | April 1st    | `sha256:1a062a1178666fde4ba1cbe777e4a34c79729fc04a40aad17a4c5a322086b170` |
|  `0.124.1` `latest` `0` `0.124`                 | March 28th   | `sha256:aee03cf7df7bacc58e2c2a904f6247ffc9be52ea9d7375dabe2adef8c47b5aba` |
|  `0.124.0-dev`                                  | March 18th   | `sha256:5ad99380d1980f35cdfd07d57b42f206adff9c94403cda39017f3523e5b0dc80` |
|  `0.124.0`                                      | March 18th   | `sha256:cc468ce2d60da53a51ca413acedd6e34daa88be9f9fc7b2d6353a648e4d9a848` |
|  `0.123.8` `0.123`                              | March 14th   | `sha256:7f00272e81a2d45c123593126127b0d78376893d89f38a1ba70180f820cc39ac` |
|  `0.123-dev` `0.123.8-dev`                      | March 14th   | `sha256:64337f694bda1eb3a493d65b0bd3db927e61c1e03479db541f706ca6a53ad1f1` |
|  `0.123.7-dev`                                  | March 7th    | `sha256:d61917c7b99eeda024884acc36e61d413122ed8c105e840f8e6252c9ef24e541` |
|  `0.123.7`                                      | March 7th    | `sha256:6ca957efbc5863f32ee4fdb63a44a8c72c5fd1f6bca09b643eaa7a0b8d05fb4f` |

