---
title: "ingress-nginx-controller Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the ingress-nginx-controller Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-02 00:32:13
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
|  `1.10` `latest` `1` `1.10.1`                 | July 1st     | `sha256:ebeeb7b3baadc2e35ca5d880dce473faaf951f2d2f6894656fab7c406647ed6e` |
|  `1-dev` `latest-dev` `1.10-dev` `1.10.1-dev` | July 1st     | `sha256:bfd4a4defdda41b1e9688976ccb8b2a1eecfc9b7216a94e850565e06ecc6bb68` |
|  `1.9-dev` `1.9.6-dev`                        | July 1st     | `sha256:e091863434a6436dd912b9b7ca2f280a53ee2e353af223802f845bedbd6385ed` |
|  `1.9` `1.9.6`                                | July 1st     | `sha256:8e5658bc62ed142dc5e3dfa2110e120e4670e712a8914eb459ac0af00dc3a07e` |

