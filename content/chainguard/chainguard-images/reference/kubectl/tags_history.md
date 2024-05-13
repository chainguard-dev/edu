---
title: "kubectl Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the kubectl Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-13 00:45:28
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
|  `1.29-dev` `1-dev` `1.29.4-dev` `latest-dev` | May 10th     | `sha256:d34e10b8bd954a8ff601bc1bbb31c19051ab2b7a8f84fd23edc8d0777c4baf3d` |
|  `latest` `1` `1.29.4` `1.29`                 | May 10th     | `sha256:192394971c8c3f3d358660e609025aa8e0aaf063f9e8ee06fd7c5faefa3230e2` |
|  `1.28` `1.28.9`                              | May 10th     | `sha256:f47182e6579a7a4765ead30f4cad73a9a00aec2bf7e7677d43f9706d47519721` |
|  `1.27.13-dev` `1.27-dev`                     | May 10th     | `sha256:d7f0cb5bd5ed3b52691e0da76a4ecf068f0197aa9b3849c7c261e95769aca5cc` |
|  `1.28-dev` `1.28.9-dev`                      | May 10th     | `sha256:d98ecb9a66801ab8cb335fbebf2a3d392eae1ca1bd148a64eda2d44190210642` |
|  `1.27.13` `1.27`                             | May 10th     | `sha256:b959d9966d8c6a8e34adf99030529a44e9dda63e16a2e229529e139d3bee42c3` |
|  `1.26.15-dev` `1.26-dev`                     | May 2nd      | `sha256:f8584bdb3a2e8373cb0aa515f0eabc3f1d8392bb32d427c4b657eb720334fbe5` |
|  `1.26` `1.26.15`                             | May 2nd      | `sha256:93a765a0c47c74985b04b152b7d573fd43252dc4e9f4f451ed62f5fffd5bd6b8` |
|  `1.25-dev` `1.25.16-dev`                     | May 2nd      | `sha256:2ce1f9daaf9f6b656808fa1647c7e5acb5418fc583689b4d9d89871aabf9c856` |
|  `1.25` `1.25.16`                             | May 2nd      | `sha256:51c66711b8efb6cb3ce2c2d9d8f5af35899e25636c3a98a82da98a102184b183` |
|  `1.28.8`                                     | April 24th   | `sha256:7fc7e22977b775a076be8989d68693b23780c5550ba13287f09cf31e628a86ba` |
|  `1.28.8-dev`                                 | April 24th   | `sha256:69f787fdf7ed164ec1a90071023b8efc952cd0e470b3188207c97ca7b52e02a7` |

