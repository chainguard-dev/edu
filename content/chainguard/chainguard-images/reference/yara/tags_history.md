---
title: "yara Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the yara Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-14 00:46:23
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/yara/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/yara/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/yara/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/yara/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 13th     | `sha256:579c815278db40e1db55794b9e98753dda4d2e1bb39556a0f3a9b8b72ec3e170` |
|  `latest`     | May 2nd      | `sha256:387e9758d8d0a749b42198f2b900b7c48926e5f67b80c8419caa0c621ed950a4` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `4.5.0-dev` `latest-dev` `4.5-dev` `4-dev` | May 13th     | `sha256:1c140facf4d4bf52d7b10a0359144238bb3d5e1ee25f59862b4566feb087c666` |
|  `4.5` `4` `4.5.0` `latest`                 | May 3rd      | `sha256:9115634a5b1464592bcb267bdf651ea2d6bfcd1e395d7ef4a64e73256b578a85` |

