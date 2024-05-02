---
title: "wasmtime Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the wasmtime Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-02 00:37:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/wasmtime/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/wasmtime/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/wasmtime/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/wasmtime/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 1st      | `sha256:73791db6b51cdec9885eb8602f0cae04097e20c4584b4088dc4e4fe43cbd9a1d` |
|  `latest`     | May 1st      | `sha256:d6de89a518eb7a0737271094d1e2c2ee589da1a1f84da48aea34dedee71571ca` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `20-dev` `20.0.0-dev` `20.0-dev` `latest-dev` | May 1st      | `sha256:ad6c41a22f238936e254db3c0977f628f35224727c37b601154717b0a30235b2` |
|  `latest` `20` `20.0.0` `20.0`                 | May 1st      | `sha256:3d73eb5234ac8b3eb57f62c318a2ddaa5dedebf68ddcb1912a58cb0f37945f94` |
|  `19-dev` `19.0.2-dev` `19.0-dev`              | April 21st   | `sha256:6c541973f81c55a8dfe5368d0e40415ff474bd5ee103a96d12ddff8aa8e65559` |
|  `19.0` `19.0.2` `19`                          | April 21st   | `sha256:19084f45e28fdbc883f253e842eadd6df8ce3e5926ac38e096de824a3ff09ac7` |
|  `19.0.1-dev`                                  | April 11th   | `sha256:24274eea05e06b8e47d6c1cf39d6e4e3f158873c1e845dfc283a946b3bbc8e4f` |
|  `19.0.1`                                      | April 2nd    | `sha256:24f331740d4f2c3cbe0959dbc9282ff5150ac745e1c31095b078496fa169c198` |

