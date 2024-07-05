---
title: "openscap Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the openscap Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-05 00:42:00
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
|  `latest`     | July 4th     | `sha256:6a5dc698e959dc1c5e3bbd93375ce669d7e72a9b589b1530f19aa908d810d916` |
|  `latest-dev` | July 4th     | `sha256:e72a736e08ad141d679306c89f7c7ee07ce6a818ffa9533b52eeec108093e4d2` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                      | Last Changed | Digest                                                                    |
|----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.3` `1` `1.3.10` `latest`                 | July 4th     | `sha256:ca54dd23b8f1434473f891f45cf11e1fc8cc166fb63be87672c9e3a1470c92ad` |
|  `1.3-dev` `1.3.10-dev` `1-dev` `latest-dev` | July 4th     | `sha256:6e44c448b660261bb2ea3a9f78043ad5388973b5a35237406d7096539cc33f1b` |

