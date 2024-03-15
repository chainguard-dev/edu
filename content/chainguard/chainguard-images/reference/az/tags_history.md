---
title: "az Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the az Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-15 00:51:40
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
|  `latest`     | March 14th   | `sha256:16f84690b71e5382623effe99e798f3225f611c4831027437f1dab1ad3cc621c` |
|  `latest-dev` | March 14th   | `sha256:bb6d3c46d0f992452742f11f7cae25c003996169a11a2a982c728c8f408b47ec` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `2.58-dev` `2-dev` `2.58.0-dev` | March 14th   | `sha256:2c6cea43ca6c63703924eb3bfee70fe1085e88ae67fc9f0f3f3466137b9abae0` |
|  `2` `2.58` `latest` `2.58.0`                 | March 14th   | `sha256:ed68c1ca76be036306e7fec6b583460fc0bf435330825e35678f545d8ba361fd` |
|  `2.57-dev` `2.57.0-dev`                      | March 2nd    | `sha256:bbbddfde4935d20df168de07289a3fa937e70c42bde7730b5135c400e21543f9` |
|  `2.57.0` `2.57`                              | March 1st    | `sha256:df6efa3600d254a0177d52ed521a444349dba3a7d08a92a6ed23e26661f96651` |

