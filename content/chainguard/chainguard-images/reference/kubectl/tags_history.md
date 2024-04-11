---
title: "kubectl Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the kubectl Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-11 00:54:43
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
|  `latest-dev` | April 9th    | `sha256:7b87d26f29e90e84b1da5390cf0c2e7ce7718a3c3ceea28d824dcc99f2f4fec0` |
|  `latest`     | April 4th    | `sha256:5869d857db2e4207f13580e2a28b72968a50b04e83d49219d0c9b6a5568923a5` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `1.28.8-dev` `1.28-dev`                      | April 9th    | `sha256:e52b5c0465ba9222153a83b2ff567e29fa7272bdc289ec169d3259509d59f8a4` |
|  `1.29-dev` `1-dev` `1.29.3-dev` `latest-dev` | April 9th    | `sha256:52850f530f3b333c7b6d81dec068515c0dc351349fdc04fb164a90652321f168` |
|  `1.26-dev` `1.26.15-dev`                     | April 9th    | `sha256:459dff8d4a823307aaa2fa9cad9ff76470bae81fdae2a92988c348794a7a0280` |
|  `1.25-dev` `1.25.16-dev`                     | April 9th    | `sha256:3f75428613663030a867d10851068c5a26ad0a8a19187f1f2bd1d13479a7b786` |
|  `1.27.12-dev` `1.27-dev`                     | April 9th    | `sha256:94ef78c93f532d99a430be7422db230ad29dc069a12a02ce75ffdd040f499661` |
|  `1.27` `1.27.12`                             | April 4th    | `sha256:4efb5f3802b099d9571990d2fffa989392632e0c48c8e9e539310cdbbf8aa227` |
|  `1.29` `1.29.3` `latest` `1`                 | April 4th    | `sha256:8f4d97526b12d7d185f285e7c2fa44366c5e7b07d4cf08cb26e04b5d828eebbf` |
|  `1.28` `1.28.8`                              | April 4th    | `sha256:e03d1dd4f1313b435087d33228a1810fe32a0b98c7c480e63abd419bc27c0954` |
|  `1.26.15` `1.26`                             | March 28th   | `sha256:c455c348adfe0fe2fd2e83f14f5c39c4944f09d17a000c1eeb1c4563037ab7f4` |
|  `1.25.16` `1.25`                             | March 28th   | `sha256:714ef12adc3074644347016121b06d540331299c217989db5730db4c67561897` |
|  `1.29.2`                                     | March 14th   | `sha256:18d7c81638548c438d1206752fcbbb28111c92cd075acb5289ca75f5589b961d` |
|  `1.26.14`                                    | March 14th   | `sha256:98e08d20545be63880885c1b46845ee87172192284c9b432b820267b92f834aa` |
|  `1.28.7-dev`                                 | March 14th   | `sha256:6eb4b8d9dd7f99d8980ff1712d8e80621c2887ba4dabbb052a8d39ac2c808e02` |
|  `1.29.2-dev`                                 | March 14th   | `sha256:f497e1c83e3c0619852bef70fa8d24f1b5b441bedaa242dde28fb11eb336c0f9` |
|  `1.27.11-dev`                                | March 14th   | `sha256:baee8cde61402466f0e610bc5e99cd668667d08415326b8f6afc4f920dc62791` |
|  `1.26.14-dev`                                | March 14th   | `sha256:3bedddffdef8250d7f0ba41be5e9a9f0e8437cfc2ad7a44d532b649672268a36` |
|  `1.27.11`                                    | March 14th   | `sha256:945ec09fa7d749b22fbb881448483e80b1d02704fd9bd566cb896ec074e5cc34` |
|  `1.28.7`                                     | March 14th   | `sha256:2d8ecfff000918d7b2db320e80f3a2a2b986cdcea5d4b537eec3075047a88b63` |

