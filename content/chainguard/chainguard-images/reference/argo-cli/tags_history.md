---
title: "argo-cli Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the argo-cli Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-02 00:37:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/argo-cli/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/argo-cli/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/argo-cli/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/argo-cli/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | May 1st      | `sha256:0e8f8e4b22a9eac93dd034aab2ea2a44305761c4e1cbcab1e25ccdbcf536c915` |
|  `latest-dev` | May 1st      | `sha256:ec630397596562ed25bfd645cd825ea5af5d27d0bd1af3698f1947fe5e1aa5c4` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `3.5-dev` `3-dev` `3.5.6-dev` | May 1st      | `sha256:30273223d4477418a3c9adce30944f6bdc639622c1f043639c75bdac94bae3ae` |
|  `3.5.6` `3.5` `latest` `3`                 | May 1st      | `sha256:0bb302def0ee78a8da380354bb3c7b514f96c161242c4d88705eb27ea0a31ec7` |
|  `3.5.5-dev`                                | April 11th   | `sha256:220a4514ddfc1dad7b1e9cfe05a99559bcbd4fd9af0642c6da5015adb6dd54af` |
|  `3.5.5`                                    | April 4th    | `sha256:02c1d1ae567247c43fa2552bf774838b4803d267ad92c23c0bfd96ac303afc7c` |

