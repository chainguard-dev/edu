---
title: "docker-cli Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the docker-cli Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-09 00:39:12
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/docker-cli/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/docker-cli/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/docker-cli/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/docker-cli/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | July 8th     | `sha256:8a70347cff5792d9c9234ac5709f7700dd89abfdfe653daf277e5d20ac30dd75` |
|  `latest`     | July 8th     | `sha256:203cd569f2e0af4ad21ea43efe6016002658c10e818c5c2dce7d45c82e5d919b` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `27.0` `27.0.3` `latest` `27`                 | July 8th     | `sha256:271e93fd15c9c6057adc52cb298a952bb0e7d1c81bfbbe340244f23167de4fe3` |
|  `latest-dev` `27.0.3-dev` `27-dev` `27.0-dev` | July 8th     | `sha256:50ad32ae4f2d52adc07ebaf4a5981aa03a115884cf4df0e2eae7cce44c7e6f7e` |

