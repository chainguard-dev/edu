---
title: "node-lts Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the node-lts Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-10 00:36:03
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/node-lts/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/node-lts/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/node-lts/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/node-lts/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)                  | Last Changed | Digest                                                                    |
|--------------------------|--------------|---------------------------------------------------------------------------|
|  `latest`                | July 9th     | `sha256:691fdeb1c1e7fbd76adb7156655f6083dd352720fc2cbd5848cd22faca7a0ced` |
|  `next`                  | July 9th     | `sha256:bb88d60717df655c462ccb2098d7ace5b05ccceb43a3acde14b9ef7d48680e2d` |
|  `next-dev` `latest-dev` | July 9th     | `sha256:dfff8238b4d203ad83eeec674354d3d31a616744ea088ad162ea4c512cd0fbe2` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                     | Last Changed | Digest                                                                    |
|-------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `20.15` `20` `latest` `20.15.1`                            | July 9th     | `sha256:a25df3da6a4d0e83d7fc4323266f0d31fae6b17988ad468c6e28ac534d4ec79e` |
|  `20.15-dev` `20.15.1-dev` `20-dev` `next-dev` `latest-dev` | July 9th     | `sha256:dfd94f09b197a6471afd3a6241ed5eb2e732b0d22615d050050069c8c752d727` |
|  `next`                                                     | July 9th     | `sha256:a85c8a6284576ff316b22fa9fae3285453472d7549906208764fbce9e2fbe482` |
|  `20.15.0`                                                  | July 8th     | `sha256:672e7913414d36a3327b8677896f0b18e89f3a34261b68186aec663df6591023` |
|  `20.15.0-dev`                                              | July 8th     | `sha256:a5338dfa62898eb0cc02795e7055e14b3643c4e8a2c917e17e1355c1117d2173` |

