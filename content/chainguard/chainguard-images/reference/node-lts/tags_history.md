---
title: "node-lts Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the node-lts Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-20 00:48:18
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
|  `latest-dev` `next-dev` | May 17th     | `sha256:6c26d660aa9e5b0a0c58a73a065a896f1df39df5b76e24502171d6ffe559e345` |
|  `latest`                | May 17th     | `sha256:352823f86cfc66af25faa67f812ba011e96d28fc80b83f017970bf10bb69800e` |
|  `next`                  | May 17th     | `sha256:cb015e77d388a50bb9dc9cd1c33d316660ece006c234fb4e4c2f6c5b6e1ebf3d` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                     | Last Changed | Digest                                                                    |
|-------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `20.13.1-dev` `20-dev` `next-dev` `latest-dev` `20.13-dev` | May 19th     | `sha256:249a42ca1080fbafe5221aadf96d4b87efa35b3fcefb551c1ae1b75e03c04331` |
|  `latest` `20.13` `20.13.1` `20`                            | May 19th     | `sha256:832aa8e43d836b1cd0a0efd97d61e07f35fdf18dd24fa7d168f7d425af1f4fcd` |
|  `next`                                                     | May 19th     | `sha256:57aa08f0be80c87d372fc1bdea83b2a83d401cb9ada0fb69bfb677b7f828358c` |
|  `20.13.0-dev`                                              | May 8th      | `sha256:2360a32e40e19b859f6d47a78ff722b6e3533260547e961a24aae47ad2603aa1` |
|  `20.13.0`                                                  | May 7th      | `sha256:9e605246896ec5e57b3ca2c840df46d2736a52d8093823a237437374d1c1c788` |
|  `20.12-dev` `20.12.2-dev`                                  | May 2nd      | `sha256:e8836f7cb1c3a413655996eb25cda5e87fe8950b6af44ff77a39f0ca39b32bd0` |
|  `20.12` `20.12.2`                                          | May 2nd      | `sha256:a55a71363129778395bcc88cc8c2fe6a0f26affb1d7ee94862bef5c6e1f1c873` |

