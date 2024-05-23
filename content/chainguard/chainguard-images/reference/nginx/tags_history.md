---
title: "nginx Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the nginx Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-23 00:45:07
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/nginx/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/nginx/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/nginx/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/nginx/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 22nd     | `sha256:2773f51320220d204daeee23e4b9bc2bfcd80b47e458ed8f28707f774f378f5c` |
|  `latest`     | May 21st     | `sha256:54281cf88c859dd840e5184aa19eb90bdea238fe7bf0ba6c835f0330fa257c1f` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1-dev` `latest-dev` `1.25-dev` `1.25.5-dev` | May 22nd     | `sha256:6190e02339060ff55a9f040d304c554a22a341fe2c9c324e8402d50c1f913cf2` |
|  `1.26.0-dev` `1.26-dev`                      | May 22nd     | `sha256:4e9f1691b006031132e46cc57c68784ebdf5874142ddca3785901c5542544522` |
|  `1.25.5` `mainline` `1.25` `latest` `1`      | May 21st     | `sha256:6dbf404a343863721c7b91137d3170164a4774c9fe78faec0fec06931535e53a` |
|  `1.26.0` `1.26` `stable`                     | May 21st     | `sha256:8dfed28c172e07ea38095883eaec7ec5595ebef5b10b5f010394d63357d300a3` |
|  `1.24` `1.24.0`                              | May 2nd      | `sha256:f9cd4ff7d76ff0ce095f42fea4c9b5820fb99dcb49df0f0e302d87883fab7967` |
|  `1.24-dev` `1.24.0-dev`                      | May 2nd      | `sha256:15ebd2e4311a62e1d77e55ff87e6f494c8d3a84ef8e861fdf6a7a85a92b3b4f3` |

