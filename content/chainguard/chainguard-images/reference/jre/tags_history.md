---
title: "jre Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jre Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-28 00:45:11
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
|  `latest`     | May 24th     | `sha256:c76802be2d6617236071f474ab6a20dcb560295c6000262473edd674f9dde9d6` |
|  `latest-dev` | May 24th     | `sha256:a9fc4404a3029beefd3c9bbd197f0848da57268ceb8111971093b49bf4493595` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-8.412.08-dev` `openjdk-8.412-dev` `openjdk-8-dev`                        | May 27th     | `sha256:8f601751eccef8ada472c15aa1ddd3f989dc1693076084998c15fd86de015637` |
|  `openjdk-8.412.08` `openjdk-8.412` `openjdk-8`                                    | May 27th     | `sha256:59602515acc769642969c77426fe4840f10ed26fc756948477a557fde34bfe30` |
|  `openjdk-21-dev` `openjdk-21.0.3-dev` `openjdk-21.0-dev`                          | May 24th     | `sha256:61791da8a856b7e8c85d2c1539db6d18d49a317b3de1e64122a0a634e2ab2d4f` |
|  `openjdk-17` `openjdk-17.0.11` `openjdk-17.0`                                     | May 24th     | `sha256:774515a499e016cccf009e291bf126e484a2be41bcb38e7104e3b142910b6117` |
|  `openjdk-15.0.10.5` `openjdk-15.0` `openjdk-15.0.10` `openjdk-15`                 | May 24th     | `sha256:6726ae6ffe9e59debb6ff441d6717da0b76b46c291da09c0fef9f8e2cc6f66be` |
|  `openjdk-14.0-dev` `openjdk-14.0.2.12-dev` `openjdk-14.0.2-dev` `openjdk-14-dev`  | May 24th     | `sha256:390d6dc4c20e5184942b61ffbd34cf90909df92c5b564af35b339e1a3cf05fd0` |
|  `openjdk-14.0.2.12` `openjdk-14` `openjdk-14.0` `openjdk-14.0.2`                  | May 24th     | `sha256:51077d48fea13acf0ddd7716c5437bf2fa463df1a04860438530d72ff2b4ecdd` |
|  `openjdk-16` `openjdk-16.0.2` `openjdk-16.0.2.7` `openjdk-16.0`                   | May 24th     | `sha256:1086c3eb4afcb801d33a1a4a53257903e0c679b1fc9e994e271e46bf3dca26bd` |
|  `openjdk-21.0.3` `openjdk-21.0` `openjdk-21`                                      | May 24th     | `sha256:4eeab22c3c14e3dfac67d8582fdf2b7573de71f3d85bce81ea72cf6fd27553fa` |
|  `latest-dev` `openjdk-22-dev` `openjdk-22.0.1-dev` `openjdk-22.0-dev`             | May 24th     | `sha256:8289d87ef9ddcea3c34ffeccec55e1ba5c88d6ac75a64f551ff12add26e5157e` |
|  `openjdk-8.392` `openjdk-8.392.08`                                                | May 24th     | `sha256:bee10fb31837f16c5619ab12bd23f4306aca19ccc0b9bcbe56414e409bf4df2c` |
|  `openjdk-16.0-dev` `openjdk-16.0.2.7-dev` `openjdk-16.0.2-dev` `openjdk-16-dev`   | May 24th     | `sha256:4947f48ce5b1cca399a4e76b4ce18ad87c6544a6f641ad344561c5dc2d25622e` |
|  `openjdk-15.0.10-dev` `openjdk-15.0.10.5-dev` `openjdk-15-dev` `openjdk-15.0-dev` | May 24th     | `sha256:f776451144890dde2494382e5ebe731f33d4ba508e0451fffbee77f4bc74b7e7` |
|  `openjdk-11-dev` `openjdk-11.0-dev` `openjdk-11.0.23-dev`                         | May 24th     | `sha256:f384500c18c5885ba0cc63304315cf2252fe0b9b78479f5ef687c5443bfa5a00` |
|  `openjdk-22.0.1` `latest` `openjdk-22.0` `openjdk-22`                             | May 24th     | `sha256:5dccee90002efae196d34df470a0f382c147a63b5ff1a06504f8747253ab8588` |
|  `openjdk-11` `openjdk-11.0` `openjdk-11.0.23`                                     | May 24th     | `sha256:fd0b991639039380efdc480bf0de29cc20ad6dba65ff3d91101a46fe1abf1919` |
|  `openjdk-17-dev` `openjdk-17.0-dev` `openjdk-17.0.11-dev`                         | May 24th     | `sha256:92f7b382784b40ba1eae7ecbbb009b370b08f1a98d21a8c39ecdddffb47289e3` |
|  `openjdk-8.392-dev` `openjdk-8.392.08-dev`                                        | May 24th     | `sha256:6b4e5dbd3bd694eb6e7e092b52b90a93912a07a68f83949a1f9dbf7f86345aed` |
|  `openjdk17.0.7.7-dev` `openjdk17.0.7-dev`                                         | May 24th     | `sha256:7ae7e3f4fd4d3ed8dc5079df0f2a3d8f5eb7a0bbb299c43b26087d0a0e606491` |
|  `openjdk17.0.7.7` `openjdk17.0.7`                                                 | May 24th     | `sha256:987c691df173a241a4398d60014a6f061e007e4323f19d9c487b95c7623dfeaa` |
|  `openjdk11.0.19.5` `openjdk11.0.19`                                               | May 16th     | `sha256:677dee78db811af812e1bb2bd33c1f247a5a4e0418169c194d965fc618768bba` |
|  `openjdk11.0.19.5-dev` `openjdk11.0.19-dev`                                       | May 16th     | `sha256:30327ab04c691b2d4f2bfa4391531384ea89b4e204cc65b90eee78a5cbc83156` |

