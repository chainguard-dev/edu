---
title: "az Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the az Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-14 00:37:02
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
|  `latest`     | March 13th   | `sha256:5b8702a182128c72a5e2e26fa601c83d8919ecf2513e2b4d0e5e89994df62775` |
|  `latest-dev` | March 13th   | `sha256:5fac215f5647cdf9d0b2b24a820191c633efc4d836a642993d802baf481ffb77` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2` `2.58.0` `2.58` `latest`                 | March 13th   | `sha256:7b3230c6c0d8fee13a84b0c48d969afa19f2ebfc31918d21884b0ce62e34ffae` |
|  `2.58-dev` `latest-dev` `2.58.0-dev` `2-dev` | March 13th   | `sha256:16b8f782a653c1d25dfcfd727414ab68147559fd663677912f9971734b2e363d` |
|  `2.57-dev` `2.57.0-dev`                      | March 2nd    | `sha256:bbbddfde4935d20df168de07289a3fa937e70c42bde7730b5135c400e21543f9` |
|  `2.57.0` `2.57`                              | March 1st    | `sha256:df6efa3600d254a0177d52ed521a444349dba3a7d08a92a6ed23e26661f96651` |

