---
title: "kubectl Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the kubectl Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-22 00:45:38
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/kubectl/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/kubectl/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/kubectl/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kubectl/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 21st   | `sha256:0d1e2cdb27a5530e97fe7cdb57e7cc2c921026e3deaf67273448db66eacba762` |
|  `latest`     | April 17th   | `sha256:f1513165910da59ef3de9664559689fa51df43996b00a9dfa9facb5fcfc771cc` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.25.16-dev` `1.25-dev`                     | April 20th   | `sha256:74ef185c0792da01c3031520cecedb849b7b827c99a10490da00645a063ab1e5` |
|  `1.29.4-dev` `1.29-dev` `1-dev` `latest-dev` | April 20th   | `sha256:0d9f6b4ba56e70ecaa38205904c2b60f7194e5bdddb27cba20ac9142aaf51b89` |
|  `1.28.8-dev` `1.28-dev`                      | April 20th   | `sha256:ec5ae8086ba25bcf6b867cf880b1a4b0aeef54237e121ca68b80d47079ae1e74` |
|  `1.26-dev` `1.26.15-dev`                     | April 20th   | `sha256:20b202967ed13f3ea660baca808569dda9be9644eb60074503a0afaf66866beb` |
|  `1.27-dev` `1.27.13-dev`                     | April 20th   | `sha256:35f1f6b595d87af8dd8da0dfbab73e8b13425675d33e0744ee6f4e267ed80d81` |
|  `1.27.13` `1.27`                             | April 19th   | `sha256:1d8f9d341062eafffd702f1b316f27e174a44a70a45b430c5bc5933a9265deaa` |
|  `1.29` `1.29.4` `latest` `1`                 | April 17th   | `sha256:0b995846b452e4bd1e13066cf13f217c43fc34ccabc501d6c98860b9d0195529` |
|  `1.27.12-dev`                                | April 11th   | `sha256:3e212905c5dc3fd722dda20aa21114301fda5da6c3b00db5e8caa6f6bc153ea1` |
|  `1.29.3-dev`                                 | April 11th   | `sha256:1fef740978daccc104572c9e5c13a2353d0085a56f11ba560c422cea667e5796` |
|  `1.29.3`                                     | April 4th    | `sha256:8f4d97526b12d7d185f285e7c2fa44366c5e7b07d4cf08cb26e04b5d828eebbf` |
|  `1.28` `1.28.8`                              | April 4th    | `sha256:e03d1dd4f1313b435087d33228a1810fe32a0b98c7c480e63abd419bc27c0954` |
|  `1.27.12`                                    | April 4th    | `sha256:4efb5f3802b099d9571990d2fffa989392632e0c48c8e9e539310cdbbf8aa227` |
|  `1.26.15` `1.26`                             | March 28th   | `sha256:c455c348adfe0fe2fd2e83f14f5c39c4944f09d17a000c1eeb1c4563037ab7f4` |
|  `1.25.16` `1.25`                             | March 28th   | `sha256:714ef12adc3074644347016121b06d540331299c217989db5730db4c67561897` |

