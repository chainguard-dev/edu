---
title: "chromium Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the chromium Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-22 00:34:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/chromium/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/chromium/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/chromium/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/chromium/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | March 21st   | `sha256:844e46060a694ea4fbeaec37352c03aae3c3d714ae7de31f69c60c742b046874` |
|  `latest`     | March 21st   | `sha256:be764c8d2a5254f8bae608ddf8f2157e3d612f29ace91fbc273acc931869857a` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                  | Last Changed | Digest                                                                    |
|--------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `123` `123.0.6312` `123.0` `latest` `123.0.6312.58`                     | March 21st   | `sha256:5aec2dd2b9302fca621eed5b2384e72269deaf179d2c332e7a69dd13a94473e8` |
|  `123.0.6312-dev` `123.0-dev` `123.0.6312.58-dev` `123-dev` `latest-dev` | March 21st   | `sha256:8c47cbcb3d2a40faa15283489bf236012600d82155dc990549a44c914e22058c` |
|  `122.0.6261` `122.0` `122` `122.0.6261.128`                             | March 18th   | `sha256:205efdb878b9493fbc8320f7d1a882cb93c7513159488189b747d6175f238e9b` |
|  `122.0.6261.128-dev` `122.0.6261-dev` `122-dev` `122.0-dev`             | March 18th   | `sha256:411875021780446e9fafd0c15f4f900ab1f4255d05faad659336df47f3617bbf` |

