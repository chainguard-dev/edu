---
title: "az Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the az Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-08 00:56:03
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/az/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/az/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/az/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/az/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | March 7th    | `sha256:5b41df088e6ffa02296839f172d8eb569765f22eaf8e197bfd8453d651ece968` |
|  `latest-dev` | March 7th    | `sha256:192536981ff37500ec3a8987bcb97fb02566f1342098cfdfed2cbd6c7e8f987b` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2.58` `2` `2.58.0` `latest`                 | March 7th    | `sha256:280c6e4a285477815ad5e96bba309e9d74499ba6313dd35c8a3a9b2904989045` |
|  `latest-dev` `2.58.0-dev` `2.58-dev` `2-dev` | March 7th    | `sha256:40ba032e2de81aaa213c3a200a3e3f34eae2a5bad84840e9759b897f21865521` |
|  `2.57-dev` `2.57.0-dev`                      | March 2nd    | `sha256:bbbddfde4935d20df168de07289a3fa937e70c42bde7730b5135c400e21543f9` |
|  `2.57.0` `2.57`                              | March 1st    | `sha256:df6efa3600d254a0177d52ed521a444349dba3a7d08a92a6ed23e26661f96651` |

