---
title: "skaffold Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the skaffold Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-13 00:45:28
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/skaffold/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/skaffold/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/skaffold/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/skaffold/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 10th     | `sha256:005f55c6ed54d9b2414e9b4923c66d6464d4756c0e08918c3c6c2e4cf191ed95` |
|  `latest`     | May 10th     | `sha256:ebdcbbf0adad41c6fb5f06f78bb07d2fcc1f42e58fdefd6e277d38dbebb8045f` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `2` `2.11.1` `2.11`                 | May 10th     | `sha256:472657740fe9123ebd6456a7cdf75759e6cf3528a29c0de4e3719d57e3e888a5` |
|  `2.11-dev` `latest-dev` `2.11.1-dev` `2-dev` | May 10th     | `sha256:9b46d0038bc5f566b64e7c96cbd1270e4f0857cc5b0d2012d0765581a4dd79ef` |
|  `2.4.0-dev`                                  | May 9th      | `sha256:372a7be3e7c7d86ae162e51e4d46de6d3df2e16df4139b02b2a67cf4d3bd5a08` |
|  `2.4.0`                                      | May 9th      | `sha256:997c86d21f52ab05db7cd830b687fdbc45906f787869659acc3e5ece9539b08a` |
|  `2.3.1` `2.3`                                | May 1st      | `sha256:6fe0d91b705f98ba087ab48a319e1894ac7ab9cd56a829d7e51e770f2965a867` |
|  `2.3.1-dev` `2.3-dev`                        | April 25th   | `sha256:f275f0c8dd5f8ee1cfe11d6f9bbb2a25c44ff6fe276b2af1dbbde9ad3bcf4386` |

