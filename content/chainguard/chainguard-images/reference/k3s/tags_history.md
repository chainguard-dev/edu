---
title: "k3s Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the k3s Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-01 00:36:20
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/k3s/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/k3s/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/k3s/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/k3s/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 28th    | `sha256:366ac68359c6ddcea9e63d543aebb42e5a0f9c002139b26c823054e4dc61a19c` |
|  `latest`     | June 28th    | `sha256:617a95db656daebc3b9ea1b0bd432f7b34de1e2ad789695e17f13901868bfe99` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.30.2-dev` `1.30-dev` `1-dev` `latest-dev` | June 28th    | `sha256:9c6a1f9967adb9d996f2289fafad875009b6ded249f1b553f5ca15878be30123` |
|  `1` `1.30` `1.30.2` `latest`                 | June 28th    | `sha256:b2d5e63ee6bc5a98a27db35e8e29731c8f5a55a513b4579ae1f1c4b2b73586a1` |
|  `1.30.1`                                     | June 26th    | `sha256:bcbaf5961798db1c3eb534f5e7be6dd2f56a474ecb51b6d1b5e32cdd18d59eab` |
|  `1.30.1-dev`                                 | June 26th    | `sha256:d1316fb7a79c407999589f8b0946449b9db6d69b7aa0a4681dec4227a2346c3a` |

