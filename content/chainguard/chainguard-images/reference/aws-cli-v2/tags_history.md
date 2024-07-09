---
title: "aws-cli-v2 Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the aws-cli-v2 Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-09 00:39:12
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/aws-cli-v2/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/aws-cli-v2/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/aws-cli-v2/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/aws-cli-v2/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | July 8th     | `sha256:8dfdc1a17ed7b8c497bdf62fef165cb52cee07e4abbd366b04fd14bd8c81babe` |
|  `latest-dev` | July 8th     | `sha256:7c9913bff116c1b5b6e448e4edf287fd6f1f781222bf95d21318bc3a53a1847f` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2.17-dev` `latest-dev` `2.17.10-dev` `2-dev` | July 9th     | `sha256:52730040aa7ac23971ced4b1df16deeea539f5e0e526d98c6e483469bdce409e` |
|  `2` `2.17` `latest` `2.17.10`                 | July 9th     | `sha256:d9098ea4d25c54514c6972b132b5a8944ab550d3f0ce0b45d80b0220105f25bf` |
|  `2.17.9`                                      | July 8th     | `sha256:eebec0e9f805729a9ce50d3f889c5072a8196bc31430ad9bf0cf99c544bfed11` |
|  `2.17.9-dev`                                  | July 8th     | `sha256:4c336474d3e943b547af98b8eaf8fe8c5f132aea7069f05759d1256685686457` |
|  `2.17.8`                                      | July 3rd     | `sha256:4752f18146d920d661b0bee6c1be5c0cde891d657eec3fd6deecb03ab1d1b069` |
|  `2.17.8-dev`                                  | July 3rd     | `sha256:7357a7b497930d3daed7f709b6dd6763ac4dd289999f0afb48f28805d03e1b88` |
|  `2.17.7-dev`                                  | July 3rd     | `sha256:f2b319c873312a15082dd194b0d71e3c8f7ee456f57286eba5e09a05c1773559` |
|  `2.17.7`                                      | July 2nd     | `sha256:05ada930ecc9a1a00f43d31bcdb7c1aa8f8c0b16d88503581f5910023328d1bf` |

