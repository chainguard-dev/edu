---
title: "tekton-cli Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the tekton-cli Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-08 00:38:35
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/tekton-cli/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/tekton-cli/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/tekton-cli/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/tekton-cli/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 5th    | `sha256:c185aa292e7edd7d506a613d8ae8fddc9b143db3e4fd10075386791641e23378` |
|  `latest`     | April 4th    | `sha256:b35ed84f84f86478cdf62b4eef28de92dd1188ee00e99462c9f98a14c5052b1c` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `0-dev` `0.36-dev` `0.36.0-dev` | April 5th    | `sha256:6fa1a523507d6dc95ff8b578d900670562cef63cd32d79d3a40b2ba3b78e252b` |
|  `latest` `0.36.0` `0` `0.36`                 | April 3rd    | `sha256:7e2821be81039f4fd690b5d098f082232f5b4ec4ed91e1d005959373701aa572` |
|  `0.35-dev` `0.35.1-dev`                      | March 18th   | `sha256:7a0c802a34b054a874ed2b5d0d89e364b917405f42ab2c4e91b67e59b4f693b4` |
|  `0.35` `0.35.1`                              | March 18th   | `sha256:6fc4b6843b3b36c42d81217ad4b32ef0dfe865c305784d1b6f5e76ac419b8514` |

