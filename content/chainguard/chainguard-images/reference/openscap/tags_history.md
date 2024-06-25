---
title: "openscap Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the openscap Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-25 00:42:19
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/openscap/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/openscap/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/openscap/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/openscap/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | June 24th    | `sha256:c37ac5242b59a406cdf58d2f7e52e3ba4e7b018206eb7204de29f2dbc9323569` |
|  `latest-dev` | June 24th    | `sha256:a436312580a7755a080e6d7e124096347fd91b5134901f44747823323389aa32` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                      | Last Changed | Digest                                                                    |
|----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `1` `1.3.10` `1.3`                 | June 24th    | `sha256:db7b8f5d09e435f7c878e09913ea62abc7dbb7d55a291d12796f7bef0da97e26` |
|  `1.3.10-dev` `latest-dev` `1.3-dev` `1-dev` | June 24th    | `sha256:f579baa500af9c1058ce15ee78d9cbc5be65638f9c2e00ca54e22d881e3e1517` |

