---
title: "harbor-core Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the harbor-core Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-03 00:45:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/harbor-core/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/harbor-core/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/harbor-core/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/harbor-core/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | April 29th   | `sha256:3a814a86291f75b71f03c22e457dca2b9ddf8e92176ac2622864267f791c333f` |
|  `latest-dev` | April 29th   | `sha256:93a65cc31f22fb1d3b8faf6d6d5a2c5da4d92896dc9c39e1a51e92adccf1f4ff` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2` `latest` `2.10` `2.10.2`                 | May 2nd      | `sha256:7f9e140e1ad7fd3e6153fca4b0529f85d230ac97258c23e8ca5af0158fda3e34` |
|  `2.8.6-dev` `2.8-dev`                        | May 2nd      | `sha256:fbfbfcd9923b3a81e1e9cda398a8b454a54d47dbe6ed5a5220069112a7ee5add` |
|  `latest-dev` `2.10.2-dev` `2-dev` `2.10-dev` | May 2nd      | `sha256:bdf0f057dfa6f998f58f73bbbe8dd6e41b4ad09c4fecd99a0b18a44e1a08fb9b` |
|  `2.8` `2.8.6`                                | May 2nd      | `sha256:38c28f5ad448e6e74beca5d55ca16b747d23bd0e08c735d65882199bf032a51c` |
|  `2.9` `2.9.4`                                | May 2nd      | `sha256:4c19ec259f01539a5599e0a502e3f9157f9af4d0143b5dfe44482ff3d02c9ce8` |
|  `2.9-dev` `2.9.4-dev`                        | May 2nd      | `sha256:98a5c971e997ceabcbf42a93c806229146c7ded03ede0ee67260e7564694a181` |
|  `2.8.5`                                      | April 21st   | `sha256:0658ade46bdeda39ef4c73cb1b482e12054bec8d9d92b308519d94e65f7e376b` |
|  `2.8.5-dev`                                  | April 21st   | `sha256:dc04549f03607e7f9ce712f17398058a98f1a19092042f922830d1190f976229` |

