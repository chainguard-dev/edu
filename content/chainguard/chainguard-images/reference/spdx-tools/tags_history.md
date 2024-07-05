---
title: "spdx-tools Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the spdx-tools Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-05 00:42:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/spdx-tools/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/spdx-tools/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/spdx-tools/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/spdx-tools/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | July 3rd     | `sha256:df7da332275d9c4a3e4a236be8af53374a24ddbb334707407f23dcaffebb6ca9` |
|  `latest`     | July 3rd     | `sha256:0ae6644fe229415360f6f3c061f1abe07c9ef3d053172df97ac95119de78e3bb` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1-dev` `latest-dev` `1.1.8-dev` `1.1-dev` | July 4th     | `sha256:41d7641ed06dc066988b599a8ff947ea7352093468c5b9894abe57a30dc53e4f` |
|  `1` `1.1` `latest` `1.1.8`                 | July 4th     | `sha256:e9eeead140f4561d70ace08045bedd25b7afc9d93b5a3901493232e92d749fb4` |

