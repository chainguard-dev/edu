---
title: "step-cli Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the step-cli Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-24 00:53:13
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/step-cli/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/step-cli/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/step-cli/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/step-cli/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | April 23rd   | `sha256:ffbe6f5df941eb349974cf222f81a455fa0c92360ba6580d27239253d8efa0a2` |
|  `latest-dev` | April 23rd   | `sha256:4721728a9b5ac51d5e570dddfbb7f5575c15027c68bcdca0f6e904bfa8260784` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0` `0.26.1` `0.26` `latest`                 | April 23rd   | `sha256:ce9270f52ea28e1b7f44b12aa3f8ac684f57a65bacf28343f5c64db88ca5873c` |
|  `0.26.1-dev` `0-dev` `0.26-dev` `latest-dev` | April 23rd   | `sha256:eea47bc74af14af5dddfd7bdc51bd6c0337c805a9a6da555e1a1a3c31cc93f86` |
|  `0.26.0-dev`                                 | April 21st   | `sha256:c58861a16bbf5286470f8608892591da684289394dbebd736841a0cbc9f1dcfa` |
|  `0.26.0`                                     | April 21st   | `sha256:5f8d80635bbc72c9eae0d69c4cbdd7b0d515cad0980eaa77c466136cc70434d8` |

