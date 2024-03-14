---
title: "fluentd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the fluentd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-14 00:37:02
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/fluentd/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/fluentd/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/fluentd/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/fluentd/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)              | Last Changed | Digest                                                                    |
|----------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev`        | March 13th   | `sha256:30c8982070ecf2b0f84694c0fffb833cd933e3ec80e66e71c850035e2b1a2ee5` |
|  `latest-splunk-dev` | March 13th   | `sha256:e74e497844cff0966772fb19a9c2143f47c306dfe2512c9011d79ea81555a63e` |
|  `latest`            | March 12th   | `sha256:a3420d83e3334d5cb96a5b06c81039edd6ff239c663d4a0d6c6c521783202735` |
|  `latest-splunk`     | March 12th   | `sha256:1ba66d96ee5ada53ab6c0073215fa1c74fba7c96f7f5779f03aaa506f5c92d3e` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                      | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1-splunk-dev` `1.16.3-r1-splunk-dev` `1.16-splunk-dev` `1.16.3-splunk-dev` | March 13th   | `sha256:683028dbf718a5d34dae6e657ef577cbbc064ae1a5384ce68cd7408c157d8b7f` |
|  `latest-dev` `1-dev` `1.16-dev` `1.16.3-dev`                                | March 13th   | `sha256:4f2cb6b45a8b53491b6008fc3d8f87dffdee1ad6a9e52e541df9e657e6d2bf79` |
|  `1.16-splunk` `1.16.3-r1-splunk` `1.16.3-splunk` `1-splunk`                 | March 12th   | `sha256:9270681dc485f8edc1a6f1ef104ff27aaed8e4ce1987ef266ba3b5dff2238c89` |
|  `1.16.3` `latest` `1.16` `1`                                                | March 12th   | `sha256:5766852cc8733201701966c1c9cce52d8196d2bc6b5ae2e8d373d762c77b48ac` |

