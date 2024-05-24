---
title: "opentelemetry-collector Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the opentelemetry-collector Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-24 00:45:45
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/opentelemetry-collector/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/opentelemetry-collector/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/opentelemetry-collector/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/opentelemetry-collector/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | May 23rd     | `sha256:9b4bf1fd9fc2aca0f0009417ffd700d86e526762dabfe13671965d64889765e3` |
|  `latest-dev` | May 23rd     | `sha256:956fe5ef54d788f69fe6aabf7253c4af8aa8444d3ad7af3cf44cbc0d243df545` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                         | Last Changed | Digest                                                                    |
|-------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `0.101.0-dev` `0-dev` `0.101-dev` | May 23rd     | `sha256:d0233ed2625d2c7fcb8310a021aed4436ce222493a756496a693702b00a22c83` |
|  `0.101` `latest` `0.101.0` `0`                 | May 23rd     | `sha256:e7d409dfa5bc6f7341429e5f14eef09d36c1c15aa3e9799f9e626dd498bddb75` |
|  `0.100-dev` `0.100.0-dev`                      | May 19th     | `sha256:62e7da8d25d5746dd92d883ce3a61a3a37037cb296e57e6bb5af447fb76a0b50` |
|  `0.100` `0.100.0`                              | May 17th     | `sha256:5a965a8cc362879883a514a4fc84c31b59a88ffbbc110c17d054c87c8a404566` |
|  `0.99.0-dev` `0.99-dev`                        | May 2nd      | `sha256:426134a7a289f9afe3b728103cacdb83437bb707653aada28f57fe1248380c7a` |
|  `0.99` `0.99.0`                                | May 2nd      | `sha256:fd4edcdf64de8cfda943de5887d3a77d78c9fb9eeabceb281e38b693064dffbc` |

