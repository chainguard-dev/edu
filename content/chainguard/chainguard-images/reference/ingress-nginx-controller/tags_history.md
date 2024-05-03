---
title: "ingress-nginx-controller Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the ingress-nginx-controller Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-03 00:45:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/ingress-nginx-controller/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/ingress-nginx-controller/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/ingress-nginx-controller/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/ingress-nginx-controller/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 29th   | `sha256:f01618a90bd552df9b2e6fd09641ac464e542152ba50599134218233f409d299` |
|  `latest`     | April 25th   | `sha256:c7d5586997025f443aed15422aa0d889ece0f11721ce56cf2196a7dee6c3fb2b` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.9.6` `1.9`                                | May 2nd      | `sha256:fe2c879defad124dbc5af135e5b4df2039b13903d9e526a890c0535bf41cbeeb` |
|  `1.10` `1` `latest` `1.10.1`                 | May 2nd      | `sha256:b68c822603c719650adedc065f6a6c0cb69a0d8a87e2c023b32006f457351fb8` |
|  `1.9.6-dev` `1.9-dev`                        | May 2nd      | `sha256:9482ff2110c09bf914807dd88af7a30ac1ef20e260e50c55784438db7901628f` |
|  `1.10.1-dev` `latest-dev` `1-dev` `1.10-dev` | May 2nd      | `sha256:efe43c1e7b990ccb016f55d5044ab4ca644795754759ae19a83d9a130676ce90` |
|  `1.10.0-dev`                                 | April 20th   | `sha256:27f7a69e168ba4b48506041601641dafb87118758ef4b408eb01c0e6867d5553` |
|  `1.10.0`                                     | April 20th   | `sha256:2a323e07711fb6b5f9f201d89610035cebaf5be7ef2466d92efc8a8031dcfb71` |

