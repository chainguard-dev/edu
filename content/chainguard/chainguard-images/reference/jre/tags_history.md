---
title: "jre Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jre Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-23 00:45:07
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/jre/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/jre/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/jre/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/jre/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 22nd     | `sha256:99c761670ec4535a6ed9b3959fe0bf9152aa99fcdb9a1ce8c9edf86bbc28f581` |
|  `latest`     | May 21st     | `sha256:a0ec8232291ce2dc680123f81baef88032f6f5b66a3daa12e5e1417aa5a7087b` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-22-dev` `latest-dev` `openjdk-22.0-dev` `openjdk-22.0.1-dev`             | May 22nd     | `sha256:3fc2ed4f6fd3abeb11de254470fb129ee302068e474ed03c3d40a64b8e50b4ee` |
|  `openjdk-17.0-dev` `openjdk-17-dev` `openjdk-17.0.11-dev`                         | May 22nd     | `sha256:e2b93f004d9b1fabac8a9913e913a15949adc99ba8b5a4dc88f4f7bce951b3d4` |
|  `openjdk-16-dev` `openjdk-16.0.2-dev` `openjdk-16.0.2.7-dev` `openjdk-16.0-dev`   | May 22nd     | `sha256:fd77deb2ef8ee1668b833adcbdfe44694ae39588aca9252964448d5b191ca816` |
|  `openjdk-21.0.3-dev` `openjdk-21-dev` `openjdk-21.0-dev`                          | May 22nd     | `sha256:42959b4eb0f6d6ae066946c9975427032f8bf359348cd488e3212c131f328a62` |
|  `openjdk-15.0.10-dev` `openjdk-15-dev` `openjdk-15.0.10.5-dev` `openjdk-15.0-dev` | May 22nd     | `sha256:ea476cd1ba2ea96ad39b312447fe5fa295534aaeb976d358341b504d4ad6e11d` |
|  `openjdk-14.0.2-dev` `openjdk-14-dev` `openjdk-14.0.2.12-dev` `openjdk-14.0-dev`  | May 22nd     | `sha256:30fef0b4eb3acdda78031dd5b0c003c10f4ed86fcc89eaa4efd8fb35f8aeb663` |
|  `openjdk-8-dev` `openjdk-8.392.08-dev` `openjdk-8.392-dev`                        | May 22nd     | `sha256:a2df50fd8dc2d2a446e8da1c04bcca8b2877a5b276451574447bd9f3263c054f` |
|  `openjdk-11-dev` `openjdk-11.0.23-dev` `openjdk-11.0-dev`                         | May 22nd     | `sha256:e9852e20273a16dad5059c5b714e0b70b13e06619d9b19c2121bf2f28003ac67` |
|  `openjdk-11.0.23` `openjdk-11.0` `openjdk-11`                                     | May 21st     | `sha256:d6f6f193cce88de59f8284a1c4d1790b966a2f49c99bc062aad739a3af2d6251` |
|  `openjdk-15.0.10` `openjdk-15.0` `openjdk-15` `openjdk-15.0.10.5`                 | May 21st     | `sha256:00b8ccdc9ecb5147dfa296bfb8d442cde2d9619cc7a5fa8a064e339cd9f3b59d` |
|  `openjdk-16` `openjdk-16.0.2` `openjdk-16.0` `openjdk-16.0.2.7`                   | May 21st     | `sha256:be26cca932f7632316b59780265efb475dc209c4eef78866943236bf01c92c9f` |
|  `openjdk-8` `openjdk-8.392.08` `openjdk-8.392`                                    | May 21st     | `sha256:6fbee2ff9a4a53c179c52ddb903221cea761e0d8be1d508cce0ac8faa238b255` |
|  `openjdk-22.0.1` `openjdk-22` `openjdk-22.0` `latest`                             | May 21st     | `sha256:995abd55e06d4c6203beb3f0a2e03c4245bcb96400f460c3e5c52a12bf0cb07a` |
|  `openjdk-17.0` `openjdk-17.0.11` `openjdk-17`                                     | May 21st     | `sha256:4f08b6a7d5be371fb4b46d4c70ac59e95c874caef2fe692301e97bc7c562afe7` |
|  `openjdk-14.0.2` `openjdk-14.0` `openjdk-14` `openjdk-14.0.2.12`                  | May 21st     | `sha256:d4b580e02b53f10e5fa2964fd72e3cb560e6fe6facd44379d2b715f25f0b0286` |
|  `openjdk-21` `openjdk-21.0.3` `openjdk-21.0`                                      | May 21st     | `sha256:3e0910d70e2a9a92516a009dce2eea5a1854ae697a3c1d1c53b43023ff0aff7a` |
|  `openjdk11.0.19.5` `openjdk11.0.19`                                               | May 16th     | `sha256:677dee78db811af812e1bb2bd33c1f247a5a4e0418169c194d965fc618768bba` |
|  `openjdk11.0.19.5-dev` `openjdk11.0.19-dev`                                       | May 16th     | `sha256:30327ab04c691b2d4f2bfa4391531384ea89b4e204cc65b90eee78a5cbc83156` |

