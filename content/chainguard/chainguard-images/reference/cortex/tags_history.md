---
title: "cortex Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the cortex Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-03 00:45:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/cortex/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/cortex/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/cortex/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/cortex/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | May 2nd      | `sha256:8cf49e0115c0f0015b26ad096c8c63b8c5cfa6261ccb7e8d5befa1f4be9cf70c` |
|  `latest-dev` | May 2nd      | `sha256:4c4a5f2a464e3aed4e597f1be4b0efdfc295149842da30b556c97f0acc7bdac9` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `1-dev` `1.17.0-dev` `1.17-dev` | May 2nd      | `sha256:6f00a983ac99b40d2135ab1c8ed4fea53b7ad647222f19926531689108f67265` |
|  `1.17.0` `latest` `1.17` `1`                 | May 2nd      | `sha256:7edd1a2d8da740e62641b47ab7a45ea73772c7d606987d47508a1f7682c73cfa` |
|  `1.16-dev` `1.16.1-dev`                      | May 1st      | `sha256:77032121933346276e59fd51e0405f3859fb03fc658a60c78b0820825aaf4f50` |
|  `1.16.1` `1.16`                              | May 1st      | `sha256:dc4d416c6eb3ac9cc37dd552f0b01d7653868f2c1003929eed5e2fa2c880be27` |
|  `1.16.0-dev`                                 | April 21st   | `sha256:8b9f9e3418a25ecefdf0e56bfd33c9506399c67d6c8c9a0ecabf41e97d249a8f` |
|  `1.16.0`                                     | April 21st   | `sha256:2f685e3a0ab543eba936bd57a5205754351311fac2ee5988b1f3f58705184645` |

