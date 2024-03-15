---
title: "fluentd Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the fluentd Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-15 00:51:40
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
|  `latest`            | March 14th   | `sha256:c5b56a62a78c73e6e42fb8084a71461d9b0a0704885c0c8c33b71ef6c20d9b09` |
|  `latest-dev`        | March 14th   | `sha256:03a6f2fc4cca330893d9c144b039780cd33ef46a511a4bda330efd893e0f88f2` |
|  `latest-splunk-dev` | March 14th   | `sha256:1a6b819709d1a661970e3e1eb09ec5573e83a5ca285526cf80238802e56d7b46` |
|  `latest-splunk`     | March 14th   | `sha256:1d2733b9ea8714b0f84fd8eeff72ca02632af1ba579f01b441b557a10bfbdbc7` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                      | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1` `latest` `1.16` `1.16.4`                                                | March 14th   | `sha256:8299a592c729ebded42e9a69fae2cfeab8879ef81222de51a2275f381e9bd0ee` |
|  `1.16-dev` `1.16.4-dev` `latest-dev` `1-dev`                                | March 14th   | `sha256:b72894080cd5ec1d53220149d8d9322ea0d971468e40aed41b9d2e4cb9e92d31` |
|  `1.16.4-splunk` `1.16.4-r0-splunk` `1-splunk` `1.16-splunk`                 | March 14th   | `sha256:9d769e7edbdbd59368022247bc45da98e5f7d8ae3ab19533894e1d7a162bb9a2` |
|  `1-splunk-dev` `1.16.4-splunk-dev` `1.16.4-r0-splunk-dev` `1.16-splunk-dev` | March 14th   | `sha256:1e603b0791c8154387101fe6cf85dace859072d445ccec0ce966047e2c1098eb` |
|  `1.16.3-r1-splunk-dev` `1.16.3-splunk-dev`                                  | March 14th   | `sha256:0fef6f7c2cd7b2050db62430cfcbda1321040a445611bd45912694c722feb2ba` |
|  `1.16.3-r1-splunk` `1.16.3-splunk`                                          | March 14th   | `sha256:7c8e444a1bd10fe1b2ff2420375ac5a307d06b9063555dc20522cc6725758e6c` |
|  `1.16.3`                                                                    | March 14th   | `sha256:a73b93df29394adca0c321d669efec4d21b1d50ab3e4f19728196a8023b66e2b` |
|  `1.16.3-dev`                                                                | March 14th   | `sha256:12cb8789fef98f45bd4be9de57f7e2974dd2109ae39dbbfe0fe00c7a2a8d447a` |

