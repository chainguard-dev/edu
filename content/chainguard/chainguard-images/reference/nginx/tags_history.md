---
title: "nginx Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the nginx Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-12 00:54:01
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/nginx/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/nginx/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/nginx/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/nginx/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 11th   | `sha256:ecd6fe8039a4b5145d928e5700e045ca646c689c4d1cd20e40256f77e8b90c55` |
|  `latest`     | April 11th   | `sha256:f01d7c54cb2388def2fff2cfacf83f1d6e0dfcebeda75b461e1e0128a8ea5c31` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.24` `stable` `1.24.0`                     | April 11th   | `sha256:92559dd7e71faa0c1727b4439bfc5b6ef93c7201df39b0b760d45497614230b5` |
|  `1.25` `1.25.4` `latest` `1` `mainline`      | April 11th   | `sha256:3e9c4dcdb6482af179ac1fa6152db91e47f5bb8c9348414c9e80ec24d9df03f2` |
|  `1-dev` `1.25.4-dev` `1.25-dev` `latest-dev` | April 11th   | `sha256:cb556b15b8f9354d6cb7a2a78bb984743b50078f2f2738b9a56f820346345a2c` |
|  `1.24-dev` `1.24.0-dev`                      | April 11th   | `sha256:8d86ff6919f8f4a15a1646b88edef751d5ba9513280b46714cafe145b231bd2d` |

