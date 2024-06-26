---
title: "consul Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the consul Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-26 00:35:03
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/consul/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/consul/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/consul/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/consul/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | June 25th    | `sha256:291275b82d8c7ccc67af240a4a9ffa1c54ff4c0e35371d5adc9534803f43c0a2` |
|  `latest-dev` | June 25th    | `sha256:169f19fdbf07c5fa3d70429e0779349379e426b6090ae7cfc07f567f113be835` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.15.11` `1.15`                             | June 25th    | `sha256:7781a334714a6e0ed677c72cfd7f77238fe580765ffe42754d257bfe1ed8b6ff` |
|  `1.16.7` `1.16`                              | June 25th    | `sha256:48f66f21d001b8549447f97aeed370d5ae710adde2c2dd468144ac0e87c087c1` |
|  `1.16-dev` `1.16.7-dev`                      | June 25th    | `sha256:a566279597ea5754c669fe9ff518c88132aa2ef20eea2bb333e6c7568f1be5a1` |
|  `1.15-dev` `1.15.11-dev`                     | June 25th    | `sha256:c7c73f8451f02a4d9b7b7129c27c222ee10a65a5265472ed5d9d147a1b88a03d` |
|  `1-dev` `latest-dev` `1.17-dev` `1.17.4-dev` | June 25th    | `sha256:d06cb7cbbaed3842b7db6d496ee00a9ceeb9d7510f47b5380c0bdc30469baabb` |
|  `1.17` `1` `latest` `1.17.4`                 | June 25th    | `sha256:eb95a160fe7b2d4588d545c98c86a246d9078ca0ec61a041542677da6cac8fba` |

