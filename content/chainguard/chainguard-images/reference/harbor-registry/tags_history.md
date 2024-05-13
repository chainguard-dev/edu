---
title: "harbor-registry Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the harbor-registry Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-13 00:45:28
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/harbor-registry/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/harbor-registry/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/harbor-registry/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/harbor-registry/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 29th   | `sha256:a816da3bd952682f5fc9186c641966e1d141238a72031a09e0628e7b2c44e1f1` |
|  `latest`     | April 16th   | `sha256:2c2de23c3b6d44e63bda14b5f014d6c09fa745b9e7238917749fbe74991f04d8` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                            | Last Changed | Digest                                                                    |
|----------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `3-dev` `3.0-dev` `3.0.0_alpha1-dev` | May 10th     | `sha256:df8f0617c258a740829d222426776f2242af2a4f46dee1b5db31a4e90d5cb277` |
|  `3` `3.0` `3.0.0_alpha1` `latest`                 | May 10th     | `sha256:74ea8a91ec37f354d179b8f9e40c06d4bcbf1c449f88bd0379260028e428a675` |

