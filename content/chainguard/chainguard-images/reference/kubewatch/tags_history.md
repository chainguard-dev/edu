---
title: "kubewatch Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the kubewatch Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-03 00:45:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/kubewatch/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/kubewatch/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/kubewatch/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kubewatch/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 2nd      | `sha256:e063a9d70d31e9acb47a1baf299bdd52ad1a850889b47d27738b8a056258397c` |
|  `latest`     | May 2nd      | `sha256:f2873ca89aaf0b415f63e568d654ee52feda37656320269bd56f5b36286dfef8` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2.6-dev` `2-dev` `2.6.0-dev` `latest-dev` | May 2nd      | `sha256:3b1faf090da327aa94fa208503c6925036a5f6784ea29ba8ca52442699e28ce2` |
|  `2.6` `2.6.0` `2` `latest`                 | May 2nd      | `sha256:85c063ad05e1d5075b2937c49b85a1fa8ec6741ebe236f27477025e328d25cb0` |
|  `2.5.0-dev` `2.5-dev`                      | April 30th   | `sha256:2b2b1ad2fcf6aa504ce03ca74c9dd7c52145617bd0acd9774d9fd495dd135e03` |
|  `2.5.0` `2.5`                              | April 24th   | `sha256:6345d0bcd6c021e082664a5bb63e255852fd318a6b8132f94407c7d3c8466425` |

