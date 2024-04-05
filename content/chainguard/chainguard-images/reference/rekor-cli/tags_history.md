---
title: "rekor-cli Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the rekor-cli Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-05 00:47:12
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/rekor-cli/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/rekor-cli/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/rekor-cli/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/rekor-cli/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 4th    | `sha256:e0534491c4acd3e5fd31979cd6db2759ec9a654298a0680046521964583d1844` |
|  `latest`     | April 4th    | `sha256:bbc074513b1df61d1dfa3378acf94e6216f794d3ddf82e6b5236654746a2bdb9` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1-dev` `latest-dev` `1.3-dev` `1.3.6-dev` | April 3rd    | `sha256:a9160fbd7bb09a617561f2ce79c38ca57244d4ea1e6c9f3b602530252b0d8aa1` |
|  `1` `1.3` `1.3.6` `latest`                 | April 3rd    | `sha256:3b42a1ac677b6368c8f229af22f0b6b9de5a0cfe5943eb629b08d858f6c1b1e3` |
|  `1.3.5-dev`                                | April 1st    | `sha256:2e45abbe81354116186bab5fd35949fd98ea1033250fc58c074fa05186fa2315` |
|  `1.3.5`                                    | March 28th   | `sha256:21c09126227ecf0fd3fa0047cf01361a8458185f170de99851efbec776598946` |

