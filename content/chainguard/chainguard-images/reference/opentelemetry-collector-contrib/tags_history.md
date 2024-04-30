---
title: "opentelemetry-collector-contrib Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the opentelemetry-collector-contrib Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-30 00:52:22
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
|  `latest-dev` | April 29th   | `sha256:a2cd0032155fb587c915a21149dd152cc7118fb001c66962ba7c69cf37755b2d` |
|  `latest`     | April 23rd   | `sha256:77aa5fbbeae36544f68f865f44c7361e51096f34a891bc1ce7981179f0f94bee` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `0.99.0-dev` `0-dev` `0.99-dev` | April 29th   | `sha256:c116ba061a828e681c3d202172a0377f60fe647da0e060e03d27478753cefb68` |
|  `0.99` `0.99.0` `0` `latest`                 | April 23rd   | `sha256:f325770ffd96c90d0be47881f31f02e6ae2f52189f7c46632c0406fab1ecd283` |
|  `0.98` `0.98.0`                              | April 21st   | `sha256:dcc4f7715b67e8857aa309bc97183068e8096de000c3585c6f357fb9324bf876` |
|  `0.98.0-dev` `0.98-dev`                      | April 21st   | `sha256:2be5922025028c32c4ec14d50a2515b3ff3b477bad612f4b724a3dfaaecb30fc` |
|  `0.97-dev` `0.97.0-dev`                      | April 9th    | `sha256:489803c91c3f513c53b9b7ee5d5d9097fc15e90a05c123ed9892a9d3db511587` |
|  `0.97` `0.97.0`                              | April 3rd    | `sha256:5d96ae1c0ec886083577a63dfdaaea0bcc345d47c04a15c0bf0fed100749efb3` |

