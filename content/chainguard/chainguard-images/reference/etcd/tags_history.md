---
title: "etcd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the etcd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-08 00:34:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/etcd/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/etcd/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/etcd/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/etcd/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | July 3rd     | `sha256:8cedb5f57c9574edce58ccd06c7d410ad3124e3bf46ad10734f833aed2baad9d` |
|  `latest`     | July 3rd     | `sha256:2c5eb35720355d0ee7636dedd94885f58273111202460d0a711f6d977823cfb9` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                      | Last Changed | Digest                                                                    |
|----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `3.5.14-dev` `3-dev` `3.5-dev` | July 6th     | `sha256:4545b184a3a7ee2de777fc7e0e8f1c89fd5a8fa55345f475f83a9a2aaaba9438` |
|  `latest` `3.5` `3.5.14` `3`                 | July 6th     | `sha256:26423e9d65125c2ea28b0df3723dbcae69550f569b895b9af7089c6349ea2104` |
|  `3.4.33-dev` `3.4-dev`                      | July 6th     | `sha256:22b51e7ca998be1431845c1971ab7f858b4d9408eb2fd0a315134e01efaae7ed` |
|  `3.4` `3.4.33`                              | July 6th     | `sha256:df051310039fc22f807b014c61bec858bc4c8653998eda6aed0eb3683352ed5f` |

