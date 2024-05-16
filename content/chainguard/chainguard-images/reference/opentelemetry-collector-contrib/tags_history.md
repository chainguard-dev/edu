---
title: "opentelemetry-collector-contrib Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the opentelemetry-collector-contrib Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-16 00:37:58
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/opentelemetry-collector-contrib/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/opentelemetry-collector-contrib/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/opentelemetry-collector-contrib/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/opentelemetry-collector-contrib/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | May 15th     | `sha256:b41d72365f64f3448261cb2f7ddf095a954a5f6764c730faa465852f3d7ea35f` |
|  `latest-dev` | May 15th     | `sha256:fe8684fe38685b0ed67beda0518a5f45bd95590fd7453ddf5989ad2b8c30c8ce` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                         | Last Changed | Digest                                                                    |
|-------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `0` `0.100.0` `0.100`                 | May 15th     | `sha256:551e026a0f32cf9d4ed126fddbc286baa5d7d67115f3dd0231ed9e6a5cef598d` |
|  `0.100-dev` `0-dev` `latest-dev` `0.100.0-dev` | May 15th     | `sha256:16940ee416ad8e3ef06ebca9ec091e6eb4e2cee1dfef165b121c662dd8b840f4` |
|  `0.99.0` `0.99`                                | May 2nd      | `sha256:c6d911ffdff3af608e7bdb40ea9d3be28c82c81ac3f8f80941fa1ab2bb483b0e` |
|  `0.99-dev` `0.99.0-dev`                        | May 2nd      | `sha256:e0ac90336053b4f26edbe93462e978fc65dec7cd59fad0d045d702001385a955` |
|  `0.98` `0.98.0`                                | April 21st   | `sha256:dcc4f7715b67e8857aa309bc97183068e8096de000c3585c6f357fb9324bf876` |
|  `0.98.0-dev` `0.98-dev`                        | April 21st   | `sha256:2be5922025028c32c4ec14d50a2515b3ff3b477bad612f4b724a3dfaaecb30fc` |

