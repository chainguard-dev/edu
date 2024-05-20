---
title: "consul Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the consul Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-20 00:48:18
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/consul/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/consul/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/consul/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/consul/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 17th     | `sha256:8edd8903572cc5fd3c94ebe775f470f249cd5cfadeaf2f0dfd84078b33a8dbc6` |
|  `latest`     | May 17th     | `sha256:8c1ee36cc673f8fe12ec0884cf6dee93cba10c3dc6e5e5ace246a0d7245b3ae4` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.16.7` `1.16`                              | May 19th     | `sha256:9c3dc39934d16792d0a8a576ccc106f217783c0e8b69ec2bf3eb52091522b068` |
|  `1-dev` `1.17-dev` `1.17.4-dev` `latest-dev` | May 19th     | `sha256:bf3f178a30a6231a69f5f2a4acd90bea271a82a6e0061e78c56a9cf5093763ae` |
|  `1.16.7-dev` `1.16-dev`                      | May 19th     | `sha256:9eb485ca50571c50677bdc942fd5d35b8fe4aec43bc797446ae4b08c295e4653` |
|  `latest` `1` `1.17.4` `1.17`                 | May 19th     | `sha256:fe6f6634c3c180eb5ae9486806bfaacf2c68bc053d04b1720ed27461e8236691` |
|  `1.15-dev` `1.15.11-dev`                     | May 19th     | `sha256:8cce9f97d59024b37d503d5fb158918a28ae4a081f400dfc3580f025d53b21e8` |
|  `1.15.11` `1.15`                             | May 19th     | `sha256:2e2f37d75a741ac7b81a641b3832174f7b42a70ba2f3a9e3c2b1bb588333e3e0` |

