---
title: "wasmtime Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the wasmtime Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-03 00:45:55
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
|  `latest-dev` | May 2nd      | `sha256:f5ad49c5ed72ba5e64f85526b887d7eac95f2866d6085deeacc2efbcff703692` |
|  `latest`     | May 2nd      | `sha256:a2e2adb2d99052408800e55bac70b4de52609dd1bd855875a2e1e3e8ea40a55a` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `20.0.0` `20.0` `20`                 | May 2nd      | `sha256:8de7eb7fe541069bef87f22e1eb52a7c451b37cf67eac2735d854f66e3b69892` |
|  `latest-dev` `20.0-dev` `20.0.0-dev` `20-dev` | May 2nd      | `sha256:cdc832dadd05d7a50f8699d80b672dab938dca925d6ec6fe8668b4aea50a2b01` |
|  `19-dev` `19.0.2-dev` `19.0-dev`              | April 21st   | `sha256:6c541973f81c55a8dfe5368d0e40415ff474bd5ee103a96d12ddff8aa8e65559` |
|  `19.0` `19.0.2` `19`                          | April 21st   | `sha256:19084f45e28fdbc883f253e842eadd6df8ce3e5926ac38e096de824a3ff09ac7` |
|  `19.0.1-dev`                                  | April 11th   | `sha256:24274eea05e06b8e47d6c1cf39d6e4e3f158873c1e845dfc283a946b3bbc8e4f` |

