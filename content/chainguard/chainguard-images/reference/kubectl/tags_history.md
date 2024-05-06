---
title: "kubectl Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the kubectl Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-06 00:43:57
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/kubectl/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/kubectl/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/kubectl/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kubectl/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 29th   | `sha256:6bc9d9831a4c829e58eac58fe4690b990fae837ac1f30c2378984cbc89b64c10` |
|  `latest`     | April 17th   | `sha256:f1513165910da59ef3de9664559689fa51df43996b00a9dfa9facb5fcfc771cc` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.29.4` `latest` `1.29` `1`                 | May 2nd      | `sha256:d932ebddf8884fc47139b7b6ba36ec2018d94322adf804e07dc75b80f1ec427c` |
|  `1.28-dev` `1.28.9-dev`                      | May 2nd      | `sha256:b835210fe0cac141289f24a2e1e93a620b4203444262b8721d21704cdd5a610b` |
|  `1.28` `1.28.9`                              | May 2nd      | `sha256:79096f61f683a6130f7f1bf570da9729f60e6da3e2f53329604f2ed476dbcbb2` |
|  `1.27-dev` `1.27.13-dev`                     | May 2nd      | `sha256:0581b8447d58a5523e05939d232389958c48132a92a635ca87d1c8aa8fa40c03` |
|  `1.27` `1.27.13`                             | May 2nd      | `sha256:ff72f910045326eb19aeab80ca4a762fa9f775f3d783f5124afbc3189156b72b` |
|  `latest-dev` `1.29-dev` `1.29.4-dev` `1-dev` | May 2nd      | `sha256:9f1afa16a01c04916cbad39402393084e7c6a8c398f3d45f402d44dd75b0511a` |
|  `1.26.15-dev` `1.26-dev`                     | May 2nd      | `sha256:f8584bdb3a2e8373cb0aa515f0eabc3f1d8392bb32d427c4b657eb720334fbe5` |
|  `1.26` `1.26.15`                             | May 2nd      | `sha256:93a765a0c47c74985b04b152b7d573fd43252dc4e9f4f451ed62f5fffd5bd6b8` |
|  `1.25-dev` `1.25.16-dev`                     | May 2nd      | `sha256:2ce1f9daaf9f6b656808fa1647c7e5acb5418fc583689b4d9d89871aabf9c856` |
|  `1.25` `1.25.16`                             | May 2nd      | `sha256:51c66711b8efb6cb3ce2c2d9d8f5af35899e25636c3a98a82da98a102184b183` |
|  `1.28.8`                                     | April 24th   | `sha256:7fc7e22977b775a076be8989d68693b23780c5550ba13287f09cf31e628a86ba` |
|  `1.28.8-dev`                                 | April 24th   | `sha256:69f787fdf7ed164ec1a90071023b8efc952cd0e470b3188207c97ca7b52e02a7` |
|  `1.27.12-dev`                                | April 11th   | `sha256:3e212905c5dc3fd722dda20aa21114301fda5da6c3b00db5e8caa6f6bc153ea1` |
|  `1.29.3-dev`                                 | April 11th   | `sha256:1fef740978daccc104572c9e5c13a2353d0085a56f11ba560c422cea667e5796` |

