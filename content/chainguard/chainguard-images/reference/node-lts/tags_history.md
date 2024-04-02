---
title: "node-lts Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the node-lts Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-02 00:36:12
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/node-lts/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/node-lts/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/node-lts/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/node-lts/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 1st    | `sha256:4fd5a946dc91d82748c3209920f7933e712d1f25d313c26d0124675ae8a205d0` |
|  `latest`     | March 31st   | `sha256:9a8990a5f70b8b47e7479a1bfe3de7d25881786b3774e037cc2d90fad11528ce` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                          | Last Changed | Digest                                                                    |
|--------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `20.12-dev` `20-dev` `20.12.0-dev` `latest-dev` | April 1st    | `sha256:9c74d760442a50c0024ab7e04e485e368c394cbdd7cc14f6ec0222a59d59f202` |
|  `20.12.0` `20.12` `20` `latest`                 | March 31st   | `sha256:30c20918a9de29d705739c7bbd0a0aff85d8094f6564c81e4c1e119339d3fce9` |
|  `20.11` `20.11.1`                               | March 18th   | `sha256:c972cb33201cd945b4372c2369152967ee1f7493c906f098f8dd0112c481d1dd` |
|  `20.11-dev` `20.11.1-dev`                       | March 18th   | `sha256:9042c740b80df22bf549889ec2abe12170f3e4b836ecb2498ca67191d9e09be8` |

