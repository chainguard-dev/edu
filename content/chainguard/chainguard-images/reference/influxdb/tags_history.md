---
title: "influxdb Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the influxdb Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-16 00:37:58
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/influxdb/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/influxdb/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/influxdb/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/influxdb/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | May 15th     | `sha256:cd5a10a01a6dba2053757659b6b658936f0514e1de42e90226d288408ebdcb7d` |
|  `latest-dev` | May 15th     | `sha256:6b5ba4bbc869917cd3d2dc8272a18dd068c4d2d85c822035bc947c83f98cc8e5` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2.7.5` `latest` `2.7` `2`                 | May 15th     | `sha256:1106287ceeab3968bf6f19c312b03ec80ae375ffa48ddae58dae6c0103be564f` |
|  `2.7-dev` `latest-dev` `2-dev` `2.7.5-dev` | May 15th     | `sha256:546628a51be7132bf77f87ed8778d747f572813ffdd0fd0f19526f4157cd76fa` |
|  `2.7.4-dev`                                | April 16th   | `sha256:b1cfbb75363b170664a1b0caa5cee0503941914eab711cd892db917a134cbc06` |
|  `2.7.4`                                    | April 16th   | `sha256:131ca5dd9dbcfb91f7f1702dcb487a2e5d764b3ca4261c56ec93f97b7647468b` |
|  `2.7.0-dev`                                | April 27th   | `sha256:8010a5bd4f42fdf112b072d563a4aca28195ba81f383919cad600b75b539953f` |
|  `2.7.0`                                    | April 27th   | `sha256:8bc8be1c00b8da700bca9293a2d274e98b44ef37c64d1b9ab2a9c15078a27947` |

