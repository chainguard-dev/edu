---
title: "vault Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the vault Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-13 00:45:28
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/vault/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/vault/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/vault/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/vault/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 2nd      | `sha256:fd3ec0d8b0c22f6a47ed3dd9a80bd8a6cf3e73939e359d3e4cc266d7d9753f0f` |
|  `latest`     | May 2nd      | `sha256:2baf8cbad827e519390f0346e3e7a1bc148506873b7f6446d26ccd4809c937d2` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `1.14` `1.14.12` `1`                 | May 11th     | `sha256:a8438e99661e6014d57551b5d58338a03b3f17936b28b058626a7a6318d4900b` |
|  `1.14-dev` `latest-dev` `1-dev` `1.14.12-dev` | May 11th     | `sha256:189e2abade1e478d087483b4f49a74a7caa930ac6e5e775ec4d592b2c2f4c7c6` |
|  `1.13.13-dev` `1.13-dev`                      | May 3rd      | `sha256:b08668d553fce9f554218dffbd116e2cf54903011244a4b8d3dcc3eb5e66d9df` |
|  `1.13` `1.13.13`                              | May 3rd      | `sha256:83ec106752437bf8ca5b3afd6fae5180bf72a5a7725257a6bff96281a54106dd` |
|  `1.14.11`                                     | April 26th   | `sha256:baa430d699817105639b081708b5bf3326f161308f97e5089e11851ec37c9dc9` |
|  `1.14.11-dev`                                 | April 26th   | `sha256:44281a4b321973f4480aa4be95bb23a048b8386caa19056b0786b9c180f5e0c7` |
|  `1.13.1`                                      | April 25th   | `sha256:4fa1f7cd2a3553f8f19748120b51c9ceea5f2735e67d9ee88bfd16b65513f275` |
|  `1.13.1-dev`                                  | April 25th   | `sha256:8b7f0986cd7d2835c2d3362b1d68e5e9d9837aff3ffeb3a308c3c1d379eb6ef7` |

