---
title: "kubectl Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the kubectl Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-26 00:38:30
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
|  `latest`     | March 18th   | `sha256:d56c478cb60337c0dfb87910911a98ba77beca2f9cec64144c16f80e8b1aef55` |
|  `latest-dev` | March 18th   | `sha256:d318ded89f1819ca42677b0a7c4b4a86eb72e39da2bc0d73a17659cd22a431eb` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.28-dev` `1.28.8-dev`                      | March 25th   | `sha256:6f3dc7b4b5175abd798cb70aab51fc9a2cd788182d297e56735e2e0eafae6ed0` |
|  `1-dev` `1.29-dev` `latest-dev` `1.29.3-dev` | March 25th   | `sha256:7b02bd45d1475517e1043a4b62288f913d90ef5aab3e22cae1c7aa1e6c39b6dd` |
|  `1.27.12-dev` `1.27-dev`                     | March 25th   | `sha256:cc7878fac0317539797a289cd5c31a4f4e05b96d946ebd82dc29a3fd56346ed9` |
|  `1` `1.29` `latest` `1.29.3`                 | March 24th   | `sha256:24cf4138e8667d458e955f808798681ead46b29a7e68a7588e6518b6b5fd41bc` |
|  `1.28` `1.28.8`                              | March 24th   | `sha256:23cc96138c0a0c1ca046e365d9dc4faea5f034e33821af83ae3fe54af3ccc703` |
|  `1.27` `1.27.12`                             | March 24th   | `sha256:81ffb49ab03c5534e7ad1418cea82cc63d57032d3cb2a4dff442e88e23d2669e` |
|  `1.26` `1.26.15`                             | March 18th   | `sha256:93f58c70dc21f07632f4167af9eb33a4c23070e4e7af5d27b71c5d9f5dd837db` |
|  `1.25.16` `1.25`                             | March 18th   | `sha256:24a2a5837fefd6881d845b7737c92805cbe9f22e429765733d1a2b187fdec254` |
|  `1.25-dev` `1.25.16-dev`                     | March 18th   | `sha256:9165a44a7471b0fb0678992b6dab47f6add28e44f33e1d99376acb64861ff8cf` |
|  `1.26-dev` `1.26.15-dev`                     | March 18th   | `sha256:6023861a731cd23ed12907eab7cddbff6918e9de1e24af01c4ce92b7b1264f37` |
|  `1.29.2`                                     | March 14th   | `sha256:18d7c81638548c438d1206752fcbbb28111c92cd075acb5289ca75f5589b961d` |
|  `1.26.14`                                    | March 14th   | `sha256:98e08d20545be63880885c1b46845ee87172192284c9b432b820267b92f834aa` |
|  `1.28.7-dev`                                 | March 14th   | `sha256:6eb4b8d9dd7f99d8980ff1712d8e80621c2887ba4dabbb052a8d39ac2c808e02` |
|  `1.29.2-dev`                                 | March 14th   | `sha256:f497e1c83e3c0619852bef70fa8d24f1b5b441bedaa242dde28fb11eb336c0f9` |
|  `1.27.11-dev`                                | March 14th   | `sha256:baee8cde61402466f0e610bc5e99cd668667d08415326b8f6afc4f920dc62791` |
|  `1.26.14-dev`                                | March 14th   | `sha256:3bedddffdef8250d7f0ba41be5e9a9f0e8437cfc2ad7a44d532b649672268a36` |
|  `1.27.11`                                    | March 14th   | `sha256:945ec09fa7d749b22fbb881448483e80b1d02704fd9bd566cb896ec074e5cc34` |
|  `1.28.7`                                     | March 14th   | `sha256:2d8ecfff000918d7b2db320e80f3a2a2b986cdcea5d4b537eec3075047a88b63` |

