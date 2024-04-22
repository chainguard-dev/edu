---
title: "wasmtime Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the wasmtime Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-22 00:45:38
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
|  `latest-dev` | April 21st   | `sha256:ac70be58aa4f8d3183661860e9f8b1947f5392c196a573859fa76d779a3f0dbb` |
|  `latest`     | April 11th   | `sha256:d5964e6ce1d30d2fee55e4b6671664fdad9d6df618d3562f4a81251eb3eebda4` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `19-dev` `latest-dev` `19.0.2-dev` `19.0-dev` | April 21st   | `sha256:6c541973f81c55a8dfe5368d0e40415ff474bd5ee103a96d12ddff8aa8e65559` |
|  `19.0` `latest` `19.0.2` `19`                 | April 21st   | `sha256:19084f45e28fdbc883f253e842eadd6df8ce3e5926ac38e096de824a3ff09ac7` |
|  `19.0.1-dev`                                  | April 11th   | `sha256:24274eea05e06b8e47d6c1cf39d6e4e3f158873c1e845dfc283a946b3bbc8e4f` |
|  `19.0.1`                                      | April 2nd    | `sha256:24f331740d4f2c3cbe0959dbc9282ff5150ac745e1c31095b078496fa169c198` |
|  `19.0.0-dev`                                  | April 1st    | `sha256:492a6f5655ac8096d9954b97f848e896b310e568e0b011e25b8011f4ecf861fa` |
|  `19.0.0`                                      | March 28th   | `sha256:ac1cc51f2dc0358d436d370246b7d8e4317d6bf19c38d37e212b28a1b7cd9e6e` |

