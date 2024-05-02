---
title: "gatekeeper Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the gatekeeper Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-02 00:37:55
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
|  `latest-dev` | April 29th   | `sha256:8fda4e163563d17db0f5633bfbc203024b348da4bb4c5ce34876bc91e02de90e` |
|  `latest`     | April 21st   | `sha256:991a66ae28c5cf2cf28d3ab1ae5443aa02e9cf23f83f4e49706236d8299682eb` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `3.13-dev` `3.13.4-dev`                      | May 1st      | `sha256:8746b1492414ef4146c6780db4a634be2de2f4c00c926d82ab53f960b04854ce` |
|  `3.12-dev` `3.12.0-dev`                      | May 1st      | `sha256:6467510456bbcaabad7fe70aea2264f3a6d9b0347a4e7a478de2ea99f6a6a2d4` |
|  `3.15-dev` `3-dev` `latest-dev` `3.15.1-dev` | May 1st      | `sha256:e71aa1e08e1f13221bfe7b6622e6151ba07f59c15160a43651477e2b719a0c88` |
|  `3.13.4` `3.13`                              | May 1st      | `sha256:ccded1c7e42e8757d2a62bd18209f15ff6a9eed08d039eb06776b68249f0a865` |
|  `3` `latest` `3.15` `3.15.1`                 | May 1st      | `sha256:40626ac5fc5c8bea1381f7922c69dabc982b31ce16b676804a13c3e24314c128` |
|  `3.14` `3.14.1`                              | May 1st      | `sha256:e9aa2c15faf287d159c4ee2a7199f727f93bfd1d17e595e7dbad859fce265a68` |
|  `3.14.1-dev` `3.14-dev`                      | May 1st      | `sha256:2f155568ccd6eb67cbe1140814e34bc87c205c2f39ffcd46d7f4e95ec91f7aa3` |
|  `3.12` `3.12.0`                              | May 1st      | `sha256:bd8a9d66cbd0c144a85ee38d773883c3da654835263a0edcac90733874060fb5` |

