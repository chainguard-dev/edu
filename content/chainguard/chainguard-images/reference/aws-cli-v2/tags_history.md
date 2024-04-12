---
title: "aws-cli-v2 Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the aws-cli-v2 Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-04-12 00:54:01
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/aws-cli-v2/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/aws-cli-v2/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/aws-cli-v2/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/aws-cli-v2/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | April 11th   | `sha256:438c9cfefd41389fc00c1172177e248c736c449e18528c272f9ad5e0c2c76b39` |
|  `latest`     | April 11th   | `sha256:560faf0bf8dd520f5c47a7e16f694a75e05719655e1fb4ffcc97bab9d01ccd65` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `2.15.37-dev` `latest-dev` `2.15-dev` `2-dev` | April 11th   | `sha256:4d358535d20c30143598867feebd57ba754e90d4af0be202f33afec6640366bf` |
|  `2` `2.15.37` `2.15` `latest`                 | April 10th   | `sha256:e6bb3abf322d6174a3e099575ec734ae30ee344d1d3c3b8827dab16cf8cd0267` |
|  `2.15.36-dev`                                 | April 9th    | `sha256:91a58d552e959e668e0e2b7e9b619488ec78ead9ff2fe7f3880c8a980cd1a7e2` |
|  `2.15.36`                                     | April 9th    | `sha256:9bcadb8954e20b13b699722c62765c6eb7a34cccc9f49bf5caa8bfbed1c113b7` |
|  `2.15.35-dev`                                 | April 5th    | `sha256:3be4b8f81bc68675a39256344c53df596bc4b1aa2f693686fb59b04ab612eb3f` |
|  `2.15.35`                                     | April 4th    | `sha256:3d20bfba367cab2805ed014b74530f8e45f2ed02680d9be07d40893c54c5233b` |
|  `2.15.34-dev`                                 | April 3rd    | `sha256:e9de560854521ccafb98daf2a85370bcd88a460f89b775cb4315911408b76a35` |
|  `2.15.34`                                     | April 3rd    | `sha256:db8dd0e8db5d17d71774cd560b6c2e54bb99a19fb90d239a89f9222873d32912` |

