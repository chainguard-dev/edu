---
title: "octo-sts Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the octo-sts Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-21 00:38:36
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/octo-sts/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/octo-sts/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/octo-sts/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/octo-sts/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 20th     | `sha256:42642423e91ad6fa57401a6f515b1207b0169c28db57f16645b28cbf65179979` |
|  `latest`     | May 18th     | `sha256:ea28f959dbf25f79e5b35359662d84459d21ec326a9a30e14014afdd4dbc640f` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `0-dev` `0.2.0-dev` `0.2-dev` | May 19th     | `sha256:c2a589b70ae2d3fc671e3271ecf7b7147a9d63d109c895de2e014a6863c2ed3b` |
|  `0.2.0` `0` `0.2` `latest`                 | May 18th     | `sha256:2e224cb2b7b9e1dd8ca77e5e720eee0ebceeffd6c715fb6eb445180e00cf2598` |
|  `0.1` `0.1.0`                              | May 17th     | `sha256:0ddf02893e4bd2de7632a03cbfd0e39a103429ffd7fbc8e825d61b53d62df6e8` |
|  `0.1.0-dev` `0.1-dev`                      | May 17th     | `sha256:6ec4d2c7a4f5492d5a8c93cd257309092c6abe41d13f39e26e51d4dc68bec509` |

