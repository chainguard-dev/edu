---
title: "fluentd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the fluentd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-19 00:54:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/fluentd/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/fluentd/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/fluentd/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/fluentd/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)              | Last Changed | Digest                                                                    |
|----------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev`        | March 18th   | `sha256:17eb939c5dfc4d7021b14acefbdd7517cce5a7bce02966bbc355ff042c1d5a2d` |
|  `latest`            | March 18th   | `sha256:695ac4f3a5725f7d7e1be4e52e7de047feb56c1345f3db36421d9e6b6ab244a3` |
|  `latest-splunk`     | March 18th   | `sha256:30ebcd0b2199a258cf19ff1757b54c06efc42c527efd6f3d7dd97e8c19cb43c4` |
|  `latest-splunk-dev` | March 18th   | `sha256:73b1bba18e5a2e107e86c3ea7db1b91d151906bc12dbab0a2d00d457d08dbd6d` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                      | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1-dev` `1.16.4-dev` `latest-dev` `1.16-dev`                                | March 18th   | `sha256:d29b1e4caabe3473f2d1e32b70ad811fb89d378722ce58db6a48ee9c1271e668` |
|  `1.16-splunk-dev` `1.16.4-r0-splunk-dev` `1.16.4-splunk-dev` `1-splunk-dev` | March 18th   | `sha256:c6c2f34d465b6923fdabed64788f70c5492a58459ff5b3a9c90c502d0995e6db` |
|  `1` `latest` `1.16.4` `1.16`                                                | March 18th   | `sha256:ed8bf9ddc1dce9940e5996d8d2b1c315f17b06efee388dd0eaf1f0838d8d1185` |
|  `1.16-splunk` `1-splunk` `1.16.4-r0-splunk` `1.16.4-splunk`                 | March 18th   | `sha256:b900e21439df253b35741477c84ae145fe352ae6089e6f239088e430650d8270` |
|  `1.16.3-r1-splunk-dev` `1.16.3-splunk-dev`                                  | March 14th   | `sha256:0fef6f7c2cd7b2050db62430cfcbda1321040a445611bd45912694c722feb2ba` |
|  `1.16.3-r1-splunk` `1.16.3-splunk`                                          | March 14th   | `sha256:7c8e444a1bd10fe1b2ff2420375ac5a307d06b9063555dc20522cc6725758e6c` |
|  `1.16.3`                                                                    | March 14th   | `sha256:a73b93df29394adca0c321d669efec4d21b1d50ab3e4f19728196a8023b66e2b` |
|  `1.16.3-dev`                                                                | March 14th   | `sha256:12cb8789fef98f45bd4be9de57f7e2974dd2109ae39dbbfe0fe00c7a2a8d447a` |

