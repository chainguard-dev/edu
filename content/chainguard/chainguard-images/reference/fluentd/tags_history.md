---
title: "fluentd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the fluentd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-16 00:33:13
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
|  `latest-splunk`     | March 16th   | `sha256:1f497b302bc46a7d47c02ea9d43dbfa76a4eca894c0c4b83c77f3700f7aae680` |
|  `latest-splunk-dev` | March 16th   | `sha256:3025b4ea293bad9eea20f5a314327ec31cf0976874bc2b041af455b87adfe746` |
|  `latest`            | March 15th   | `sha256:bac529500f0241b7d9b6fa7c06790b52c336a2166376123c3f8987c30387f6a7` |
|  `latest-dev`        | March 15th   | `sha256:33734b2b3b8c7f24070b7653a921da85f0c083e960a795fe250b15b7a0f4e114` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                      | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1-splunk-dev` `1.16.4-r0-splunk-dev` `1.16-splunk-dev` `1.16.4-splunk-dev` | March 15th   | `sha256:8ab459ec7698894c2c9255ea64ee1eb6da1a43120e50e8c3c296a431979ebc25` |
|  `1-splunk` `1.16.4-r0-splunk` `1.16-splunk` `1.16.4-splunk`                 | March 15th   | `sha256:b7aa0d352199da9c88f30629ae0656763f03fd2a51b0ef698bc9bcc6ea22954f` |
|  `1` `latest` `1.16` `1.16.4`                                                | March 14th   | `sha256:8299a592c729ebded42e9a69fae2cfeab8879ef81222de51a2275f381e9bd0ee` |
|  `1.16-dev` `1.16.4-dev` `latest-dev` `1-dev`                                | March 14th   | `sha256:b72894080cd5ec1d53220149d8d9322ea0d971468e40aed41b9d2e4cb9e92d31` |
|  `1.16.3-r1-splunk-dev` `1.16.3-splunk-dev`                                  | March 14th   | `sha256:0fef6f7c2cd7b2050db62430cfcbda1321040a445611bd45912694c722feb2ba` |
|  `1.16.3-r1-splunk` `1.16.3-splunk`                                          | March 14th   | `sha256:7c8e444a1bd10fe1b2ff2420375ac5a307d06b9063555dc20522cc6725758e6c` |
|  `1.16.3`                                                                    | March 14th   | `sha256:a73b93df29394adca0c321d669efec4d21b1d50ab3e4f19728196a8023b66e2b` |
|  `1.16.3-dev`                                                                | March 14th   | `sha256:12cb8789fef98f45bd4be9de57f7e2974dd2109ae39dbbfe0fe00c7a2a8d447a` |

