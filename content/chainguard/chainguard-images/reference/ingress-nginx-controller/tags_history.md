---
title: "ingress-nginx-controller Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the ingress-nginx-controller Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-08 00:34:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/ingress-nginx-controller/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/ingress-nginx-controller/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/ingress-nginx-controller/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/ingress-nginx-controller/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | July 1st     | `sha256:451e92b12ae260f087e52f4e88b2fa8b4746bb5318b726d5466d61d3ab86debb` |
|  `latest-dev` | July 1st     | `sha256:c5d55ddc2995d7c415f20ed1072d3c3caa60252ff96b0fdf5083879a718ae32f` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.10.1-dev` `latest-dev` `1.10-dev` `1-dev` | July 6th     | `sha256:86a061e592bf1e12b1b684fefc24c7e7413bdf7f26b8f8a14ae9c3557d4f0d21` |
|  `1.9` `1.9.6`                                | July 6th     | `sha256:230dfa808edd0e50e190f85a245b2bdf4bea76c68cd4dfc9c9ee5817141415e5` |
|  `latest` `1.10.1` `1.10` `1`                 | July 6th     | `sha256:418c969b3db9678a0daf21b90633357257c7ec88c2eec4bb154d20a4857837ae` |
|  `1.9.6-dev` `1.9-dev`                        | July 6th     | `sha256:5d2f7323a14888f89d422af1872e2693e89dbd22ba8ab5873855db0bf05fa63e` |

