---
title: "consul Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the consul Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-05 00:36:13
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
|  `latest-dev` | June 1st     | `sha256:0b3c6658f53a09c6e70493d1a1721d3b385ae00c31f77a5b1674b4237c20c718` |
|  `latest`     | May 31st     | `sha256:443890f50bd5c1c76fda867189d7821bf088ecaf02fb99fc73790bce61a335eb` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.15.11-dev` `1.15-dev`                     | June 1st     | `sha256:f04a5db3026797a94c910b2217fe73874f8822855605bcd45eb3f48daf267dba` |
|  `1.17-dev` `1.17.4-dev` `1-dev` `latest-dev` | June 1st     | `sha256:50a2790dfe474c92eef581a4e1c421b657dea91966281744a57d254e72ecade6` |
|  `1.16-dev` `1.16.7-dev`                      | June 1st     | `sha256:1f4e87a6bf095bdf7d8a8166b7ea2ee0bb1f71dfaefc881a6aa8c46ba6b659f5` |
|  `1.17.4` `1` `1.17` `latest`                 | May 30th     | `sha256:046de5407d7edd298e5f393fb1a3040e5f22fab63c6043d6f4ba040f03c738dd` |
|  `1.15` `1.15.11`                             | May 30th     | `sha256:1e96ac0606016fe16dab17f492f641ea2c844a21ab4688792b6266852d5b24a0` |
|  `1.16.7` `1.16`                              | May 30th     | `sha256:8aa7745f9a3b3e85e9bc9467a145654d2e22610a377f67c5ade0927626e2d5fd` |

