---
title: "git Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the git Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-02 00:36:12
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/git/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/git/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/git/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/git/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)                  | Last Changed | Digest                                                                    |
|--------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev`            | April 1st    | `sha256:3e6970c321e8d8f65c7a646802b06147688fcc61f0630328e9b598624fdceb8c` |
|  `latest-root-dev`       | April 1st    | `sha256:73d3fe8a3e7931575a86a81e7c20e1b2be1648d2bc93dc3f68f2e1afaf4a7b26` |
|  `latest-root`           | April 1st    | `sha256:2376a025f6673a191697f7b76b3873214290b8d144deec540bcf7134caf50eb4` |
|  `latest`                | April 1st    | `sha256:e7a68ad581bf04f496ddb932f5dc72aadde0e78fcfab28a94d5f2a1b4a5f4d1e` |
|  `latest-glibc-dev`      | April 1st    | `sha256:161749d829c3b13e3135fbbd4123850b3ca400227240a98455b68d126788e2d4` |
|  `latest-glibc-root-dev` | April 1st    | `sha256:9d556b5a6693686f2edc817149f8818cf239ed95ef7f73ff6054c7dd969aea0f` |
|  `latest-glibc`          | March 28th   | `sha256:c29789ccae98fc407af318578952702ea20761f02935cb71edcca518c568ebca` |
|  `latest-glibc-root`     | March 28th   | `sha256:aac3cb4884b8dc8d7365145be83ecc2cfbbbac9eabb297238c49d3c07a2a327d` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                   | Last Changed | Digest                                                                    |
|-------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `glibc-2.44-dev` `glibc-2-dev` `glibc-2.44.0-dev` `latest-glibc-dev`                     | April 1st    | `sha256:a8cd95e0695078f2709f389dedb9a5b9e5355da587d777db6aa261681172f5ef` |
|  `glibc-root-2-dev` `glibc-root-2.44-dev` `glibc-root-2.44.0-dev` `latest-glibc-root-dev` | April 1st    | `sha256:bd345c1ec1bc9f3ce65330439600c1f017cab0006af8fd62f960ed6c6bc4aa3f` |
|  `glibc-root-2.44.0` `latest-glibc-root` `glibc-root-2` `glibc-root-2.44`                 | March 28th   | `sha256:74b31e12a0ee7e40189f12894378d2724c0cfd6f9241ee7842d593413b31b294` |
|  `glibc-2.44` `latest-glibc` `glibc-2` `glibc-2.44.0`                                     | March 28th   | `sha256:6c559901e2016a317b7ca1232efd86dbccb59705cc9532fee4d8c9f0f9040e03` |

