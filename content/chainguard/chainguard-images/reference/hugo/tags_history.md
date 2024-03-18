---
title: "hugo Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the hugo Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-18 00:56:27
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
|  `latest`     | March 17th   | `sha256:0986ab177b2fba16f0656d44c669b7270dc7b0eb6448c99ac744742a041487cd` |
|  `latest-dev` | March 17th   | `sha256:f102f670708aa4c8182213d9e49d66b60aa8506b6eb3b9c51bb083c4a1d1c66a` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                         | Last Changed  | Digest                                                                    |
|-------------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `0` `latest` `0.124.0` `0.124`                 | March 17th    | `sha256:18fd7dbc7fe4caeca650426fc4a1d67c831a693073fc3aad83df511330561a12` |
|  `0.124.0-dev` `0-dev` `0.124-dev` `latest-dev` | March 17th    | `sha256:53ac63a253098f820a71fa4f222c43fa081ffc95a8c137b83061cb9e532f86dd` |
|  `0.123.8` `0.123`                              | March 14th    | `sha256:7f00272e81a2d45c123593126127b0d78376893d89f38a1ba70180f820cc39ac` |
|  `0.123-dev` `0.123.8-dev`                      | March 14th    | `sha256:64337f694bda1eb3a493d65b0bd3db927e61c1e03479db541f706ca6a53ad1f1` |
|  `0.123.7-dev`                                  | March 7th     | `sha256:d61917c7b99eeda024884acc36e61d413122ed8c105e840f8e6252c9ef24e541` |
|  `0.123.7`                                      | March 7th     | `sha256:6ca957efbc5863f32ee4fdb63a44a8c72c5fd1f6bca09b643eaa7a0b8d05fb4f` |
|  `0.123.6-dev`                                  | March 1st     | `sha256:ba09bbd048aaa8fe9fde7d7bf83d71c31d9b7d8a34c2f02532a0fe12319cbe01` |
|  `0.123.6`                                      | February 29th | `sha256:16689601a29ec6edc8b435d0099cdb8095fa774342f50f5d0dc7a4ed9000f0d7` |

