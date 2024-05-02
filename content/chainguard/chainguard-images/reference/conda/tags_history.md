---
title: "conda Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the conda Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-02 00:37:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/conda/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/conda/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/conda/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/conda/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 1st      | `sha256:5e7115902984214c56a167a557187b1fd533cba0ba1ec4e7f37888432e1e2b2d` |
|  `latest`     | May 1st      | `sha256:f57e6e97de67c27573d0df708fe4803e0898e806ea63d46d533d8773c6c6891c` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `24.1.2` `24.1` `latest` `24`                 | May 1st      | `sha256:31ccc25c39d60c4b9b85ce8a7ac91878109b6ab28cb4a489cf545156c328be9d` |
|  `24.4.0` `24.4`                               | May 1st      | `sha256:a961c830a1ec42efd0249f8a4ae9c327371988ecffc6f3e2eb82c32e91e03172` |
|  `24.4-dev` `24.4.0-dev`                       | May 1st      | `sha256:2e818fad4c9f8954684aedf2b1cb7a02a0dddb2cb25baf6ff1c3aac9ddc02f42` |
|  `24.1.2-dev` `24-dev` `24.1-dev` `latest-dev` | May 1st      | `sha256:b768eba8ac70a8c0c1c74cdda1f2a6309e1a9983789fa919fd1dbfdabc08914e` |
|  `24.1.1`                                      | May 1st      | `sha256:cb354e8d6e8ad71d42bc8c7d08adbd639db5c2ae64ee59dd8382c3499849e74b` |
|  `24.1.1-dev`                                  | May 1st      | `sha256:84a2c2def3abdd9c2c33d624d3253887fa1ac06d52ed2cd22b79a3c56981b7fb` |
|  `24.3-dev` `24.3.0-dev`                       | April 25th   | `sha256:65e9045a3417077a206733bcec75043a1e93822c967c7b576f8a90cd5998c827` |
|  `24.3` `24.3.0`                               | April 25th   | `sha256:bd669722f6234d0662bb2bfb7860c15ec9fd729f1cbdc474765848a2e591ddfb` |

