---
title: "datadog-agent Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the datadog-agent Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-08 00:56:03
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/datadog-agent/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/datadog-agent/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/datadog-agent/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/datadog-agent/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | March 7th    | `sha256:468ddaf28b43d3d5a083dc52bc37c386eb189e78310b3811697306e55c58eced` |
|  `latest`     | March 7th    | `sha256:40ceba6f793ef8b4efc4f1089573fd6b5e5c301afc9a1b29a53d555755038470` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed  | Digest                                                                    |
|-----------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `7.51` `7.51.1` `latest` `7`                 | March 7th     | `sha256:62b142f846f145192604538ae2f6c212b6086e52a297d962b426c474b3a257b7` |
|  `7.51.1-dev` `latest-dev` `7-dev` `7.51-dev` | March 7th     | `sha256:bdc5354f417486c924a31edf0e841895a8760bf3f84bbfa7a9c30773705bc6aa` |
|  `7.51.0-dev`                                 | February 26th | `sha256:3afec2b02a020894496883b83d6a8dfdeacefe3062c0347865b68ad2ebfe06f6` |
|  `7.51.0`                                     | February 26th | `sha256:453d78217c039391c6c1cf1547e7a74efcf3c7a5c988454b379d427391e00354` |
|  `7.50` `7.50.3`                              | February 19th | `sha256:eade793be7ec70f19561c40b58d820896d93bc8fe96e5fe8e0ad81c68e0efd75` |
|  `7.50-dev` `7.50.3-dev`                      | February 19th | `sha256:337cbc8b2e407108f27ce44b5d1f9f7b15e93a876207f94a9b8de7947143619a` |

