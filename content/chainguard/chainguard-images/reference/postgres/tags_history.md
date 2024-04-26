---
title: "postgres Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the postgres Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-26 00:36:54
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/postgres/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/postgres/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/postgres/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/postgres/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | April 25th   | `sha256:83daf955b55a4fbd26df37b45de8ad5bf635a8731a6aeb7248beea854e839b7e` |
|  `latest-dev` | April 25th   | `sha256:4274a0c9a7c3148ea6fb613cc2163b6ae03b7a15c237f25818708cae89705acf` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                           | Last Changed | Digest                                                                    |
|-----------------------------------|--------------|---------------------------------------------------------------------------|
|  `14.11` `14`                     | April 25th   | `sha256:baff90d969775c53935ebc210041dcc20e16423f18736c826d934d5b93145fde` |
|  `14-dev` `14.11-dev`             | April 25th   | `sha256:c3c526b235dea5a9d9003c83ed14df54881194d2ffd6046ea468aea397d61190` |
|  `15.6-dev` `15-dev`              | April 25th   | `sha256:a560251d1c2d558f973a263b7f86aea2c75c8c508a49489e760a6daac627335d` |
|  `15.6` `15`                      | April 25th   | `sha256:0bd278627da9a990346270f710cfc22661a0a73c84d0d7e97cfb34659cfe4ae3` |
|  `13.14` `13`                     | April 25th   | `sha256:3d45aa3cd41c706b9d426a4138cb6f44b0f71757299598fedc4e95590ff9047a` |
|  `12.18-dev` `12-dev`             | April 25th   | `sha256:fdc07d48d8c1aecc90d5b43277e4ede887ddab3e43a6ade8ae45f7e0e53db980` |
|  `13-dev` `13.14-dev`             | April 25th   | `sha256:a7147d5e88d2c02b4c9b83f93dd1758bb611604d5241e3fd7fb7d2abeba1084d` |
|  `12.18` `12`                     | April 25th   | `sha256:276e02576f27ab85d1d421d60c2a6decc3660818407f836c397c08ed71dc8b17` |
|  `16.2-dev` `latest-dev` `16-dev` | April 25th   | `sha256:4fa07b06167a1291d2760bb28eafae60106ceda603249fe94a3532b799b10483` |
|  `16.2` `latest` `16`             | April 25th   | `sha256:95799fe4ef2f7f335b19467da4af16805f465fceb8fb244810c52ed0812775a9` |

