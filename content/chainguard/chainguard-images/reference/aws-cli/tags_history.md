---
title: "aws-cli Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the aws-cli Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-01 00:46:56
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/aws-cli/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/aws-cli/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/aws-cli/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/aws-cli/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | April 30th   | `sha256:b9d5c9f622d3ad8bca156e30fc688af179bdd9fd2efa54bc7cce13159aecb908` |
|  `latest-dev` | April 30th   | `sha256:b4cb9f9179a796308f21862b45ad60e29d7fe10e9cafd04fb12d7de8b1f3d0ab` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.32` `1.32.71` `latest` `1`                 | April 30th   | `sha256:76261a9649e5d20226824158465f0548c99a638470305e3f25985e5b5d9fa96e` |
|  `1-dev` `latest-dev` `1.32-dev` `1.32.71-dev` | April 30th   | `sha256:1e4546d26226d28ce82c2092c841ec4b4bbf5a421c916d775f283d7fb8348901` |

