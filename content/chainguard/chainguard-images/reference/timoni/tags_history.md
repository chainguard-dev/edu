---
title: "timoni Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the timoni Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-17 00:44:46
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/timoni/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/timoni/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/timoni/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/timoni/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 16th     | `sha256:a69a5752fb1ef3630a3f300631cb273e17037359e6c060c1e3b810e19b39bdbc` |
|  `latest`     | May 16th     | `sha256:e5f80d645e089b61802969d878994a3363b8fe85a35c0ce7af3b67c263a6cfe9` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `0-dev` `latest-dev` `0.21.0-dev` `0.21-dev` | May 16th     | `sha256:929d586a2803b4b326ea61d48ffce5868b9aed8a145a0a70f03054fb15f6dec6` |
|  `0.21.0` `0.21` `latest` `0`                 | May 16th     | `sha256:06b8bbb4a0bae524fbd9595045b998e4836cc58e289f2a43925a53785cb7fe07` |
|  `0.20.0` `0.20`                              | April 21st   | `sha256:e068ca5e553a052f5266048b6f90c16c6ac8d4d44ddaeb690d0d33430454a21b` |
|  `0.20-dev` `0.20.0-dev`                      | April 21st   | `sha256:e5b3e3fa9bdc05a97d7d5bfce3079f5c7b636406947c06add5fba71b36a665ba` |

