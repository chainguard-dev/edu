---
title: "docker-cli Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the docker-cli Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-13 00:45:28
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
|  `latest-dev` | May 10th     | `sha256:1af2a5f732827093aef01e730b5898a9a086fd9c96a9aa75da74617c09b387c3` |
|  `latest`     | May 10th     | `sha256:d7ed3c99a52958e745fc43592d2d79fb9fcd5129b815a9d74cc14f382724c56f` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `24.0.6-dev` `24-dev` `24.0-dev` | May 10th     | `sha256:5b02d2980fb709452fcf7f153cf7aee7baf7205cc2ed571c3468f2f6f8e731de` |
|  `latest` `24.0.6` `24` `24.0`                 | May 10th     | `sha256:d0105321e68d1f8f323bd24e2113eb115c14a5fbbf52108bcda372c17c0a39fc` |

