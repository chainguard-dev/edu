---
title: "dotnet-sdk Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the dotnet-sdk Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-08 00:56:03
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/dotnet-sdk/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/dotnet-sdk/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/dotnet-sdk/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/dotnet-sdk/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | March 7th    | `sha256:efe22f480e3b756dbfdb030258144dd5fa8e4382abc2ec77d745f78097e7d722` |
|  `latest-dev` | March 7th    | `sha256:c57e865bfb4918d421f80715c6ca316d4b4a523a3c99d68829d9839f14800e19` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed  | Digest                                                                    |
|---------------------------------------------|---------------|---------------------------------------------------------------------------|
|  `6.0.127` `6.0` `6`                        | March 7th     | `sha256:b173f53c6ac0e944ae884097333492d46e7bd5b84ae5b65ff83b43e109f3612c` |
|  `7.0.116` `7.0` `7`                        | March 7th     | `sha256:c3a1f4b0a6694694bd73f383cab4d241d125fd36352a03cf891ee2146a2ac7dc` |
|  `6.0.127-dev` `6-dev` `6.0-dev`            | March 7th     | `sha256:0cb31af56eb6ca267fd278cbabc3087ceb541d8744152bf25a23cbf45a4942f0` |
|  `7-dev` `7.0-dev` `7.0.116-dev`            | March 7th     | `sha256:b3d3ac41d9d041d8bdae22c03a6e61de9fafb794c26e6d590aa5d66e62a1aad5` |
|  `latest` `8.0` `8` `8.0.2`                 | March 7th     | `sha256:2f8670f3e1ae95d4d0052beaed89ef48943f916da6eaf2743c3ca7323ce011ef` |
|  `8.0-dev` `8-dev` `8.0.2-dev` `latest-dev` | March 7th     | `sha256:b8b515ab5ff77d00b93e14c2296a6036998f2a2ca11fa21de0e0ea35d6828af5` |
|  `6.0.126-dev`                              | February 19th | `sha256:ef89b473e96ae850b91878e869dbe6ece299c1722980f21a7c73d443beef546d` |
|  `6.0.126`                                  | February 19th | `sha256:bc834f2a4f2cb066307793251a4bc9242a7a26d70eb46523ac8c29938bc6b1cd` |
|  `7.0.115-dev`                              | February 13th | `sha256:b4f473c1872138d0f83f5bc4a17370af8c22a5606488d3cc63f598eea4760876` |
|  `8.0.1-dev`                                | February 13th | `sha256:5cd59a45de9ff2fe1ba20e811587c31cd86e4742005343510d09a72c9cbbadb6` |
|  `8.0.1`                                    | February 8th  | `sha256:a07229d20ee83619223c47621ffa8699821e52567cd10b144a1f68454c326fb9` |
|  `7.0.115`                                  | February 8th  | `sha256:4cbbf91d1c108de45bd0ec9bb95b4b3ab9baa1c1d4cf888542a93001a86581c0` |

