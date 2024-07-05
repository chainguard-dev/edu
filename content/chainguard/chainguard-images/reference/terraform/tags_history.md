---
title: "terraform Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the terraform Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-05 00:42:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/terraform/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/terraform/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/terraform/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/terraform/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)                                 | Last Changed | Digest                                                                    |
|-----------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev`                           | July 3rd     | `sha256:e30b4c5cea124c3c2a1b792e036fbcb955a6845ad3f8a41e49ec6d1080362c3a` |
|  `latest`                               | July 3rd     | `sha256:54143934777a03635cba4a93ebf025d2a3d127e71ab926e8fa2c031760abae5d` |
|  `1.5-dev` `latest-mpl-dev` `1.5.7-dev` | July 3rd     | `sha256:ed17e5b5ee43b40878da14dcacbc692213d8a6d191225765791d4c9214f210c8` |
|  `1.5` `latest-mpl` `1.5.7`             | July 3rd     | `sha256:e3e61da89b843c9e4ad3f7534c0c2dd1f54d1d4d9b316ae5b1e3dc1630f167ee` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.7.5-dev` `1.7-dev` `1-dev` `latest-dev` | July 3rd     | `sha256:8362b21ba00d19fded73833f2b593508d32284a5992f24c3a9a039fce176cdc8` |
|  `latest` `1.7` `1.7.5` `1`                 | July 3rd     | `sha256:ed70f00fff2add4ff8ae74c083d62733b2f7335ba3ff0917b4b05a9aa21cb6a0` |

