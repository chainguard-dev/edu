---
title: "consul Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the consul Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-10 00:50:47
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
|  `latest-dev` | June 9th     | `sha256:70a16b849924f22fc70eaea98ca66d31619e2193e4378fc01419d93dd0dce400` |
|  `latest`     | June 5th     | `sha256:6de4347a099f9e35ee61280e7973e0ee3cb8b3fd114c820a273be2e50998fc27` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.16.7-dev` `1.16-dev`                      | June 8th     | `sha256:744c9522a97035a80f81bd46e9555cede267e37d30bfcfb71d9e165730c41b5f` |
|  `1.15-dev` `1.15.11-dev`                     | June 8th     | `sha256:3f6e979a3d6185a649dd7c19dc274fe32cf9b79fa5775b73a69bd715b4d3799e` |
|  `1-dev` `1.17-dev` `latest-dev` `1.17.4-dev` | June 8th     | `sha256:99466ff87236e89fe5be78a38c2d3fbebc78b2237aa7e6831860cf22126f3a92` |
|  `1.17` `1` `1.17.4` `latest`                 | June 5th     | `sha256:70ba373d42c9adac0ba49d5e06853f95ef0e85e8a6143e46da3c64c6203ad366` |
|  `1.16.7` `1.16`                              | June 5th     | `sha256:8c8fa898f0bed2902a70e1d529addb446b4cc361bfa1143b1f96571d1c81846f` |
|  `1.15.11` `1.15`                             | June 5th     | `sha256:a08c49523f5266a70960b93367b0e413a935b07bafebc8d24ba8f01d041f3e0f` |

