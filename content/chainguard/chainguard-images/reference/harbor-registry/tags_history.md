---
title: "harbor-registry Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the harbor-registry Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-01 00:50:07
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/harbor-registry/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/harbor-registry/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/harbor-registry/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/harbor-registry/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 31st     | `sha256:f47ba9210047ee85f2df8f57466da89e4804a868eb3646452bc42214144c3d03` |
|  `latest`     | May 23rd     | `sha256:22552619775a7b3a3e489caca71ed3a98d0a7977b94f572c9b90ac4ba7c0445f` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                            | Last Changed | Digest                                                                    |
|----------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `3.0-dev` `3-dev` `latest-dev` `3.0.0_alpha1-dev` | May 30th     | `sha256:d5b91fd629341be4d84752cc4745a29f9fc8c31e55674e134471a67d92c3d683` |
|  `3.0.0_alpha1` `3` `3.0` `latest`                 | May 23rd     | `sha256:42ead1956bfeeff1339f5856d6f6350cacec9b5d362a6ef3f1f888484fc868dc` |

