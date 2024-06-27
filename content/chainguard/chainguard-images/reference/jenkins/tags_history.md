---
title: "jenkins Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jenkins Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-27 00:41:27
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/jenkins/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/jenkins/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/jenkins/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/jenkins/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 26th    | `sha256:524ebb2025452ed9dd634018e039c5ff1560cd93b0178b4e7122768b17a34745` |
|  `latest`     | June 26th    | `sha256:1c58d73e11af69558f58c5112c4a9d54655c7a8c0cd6a5378f4b834412fb740e` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                           | Last Changed | Digest                                                                    |
|-----------------------------------|--------------|---------------------------------------------------------------------------|
|  `2-dev` `latest-dev` `2.464-dev` | June 26th    | `sha256:c718a2fc4ee0148a253500c6b6f52dbcf5ca6d0ae35d32b1de0de0a829a806e7` |
|  `2` `latest` `2.464`             | June 26th    | `sha256:f7694a647a2d88510225e238497f0e5773632f7b0372484f40f566ee5fdb180d` |
|  `2.463-dev`                      | June 23rd    | `sha256:38cdaf7f96fd8f37cd8ce0375ebe16782327af8fda4d344885e750fa3d723a97` |
|  `2.463`                          | June 23rd    | `sha256:8a3aea0fed653cd14ecd1899351590fccbf4bf2a88fc4c09aeb71316d5c1e7e5` |

