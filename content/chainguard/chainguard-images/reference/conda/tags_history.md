---
title: "conda Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the conda Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-02 00:32:13
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
|  `latest-dev` | July 1st     | `sha256:1780664bcefbca3cb71ded1735ae37b14b273e03a3510db6df7f23d418622669` |
|  `latest`     | July 1st     | `sha256:304c26e8b27c9eee76eac8aa158f69ca2b6fddaf40152f7d857cac5106268fd6` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                        | Last Changed | Digest                                                                    |
|------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `24.1.1-dev`                                  | July 1st     | `sha256:7b0e3aab836a6460878a7c24257dbbaff6869abd6700a268c6cd12cfb75fa7a7` |
|  `24-dev` `24.1.2-dev` `24.1-dev` `latest-dev` | July 1st     | `sha256:4f0e9519ef48858ddd1ba59938109a970924c5702915d2736500f06ba4ac0444` |
|  `24.5.0` `24.5`                               | July 1st     | `sha256:c711bd428f22d9e38a9dee7cfd47e04e4d20e9346dea996fd1c30bee2e6360a9` |
|  `24.1.2` `latest` `24.1` `24`                 | July 1st     | `sha256:4c893d1ea4e08dcafbcb30ad377ff2e7fc2edf9b40cc0b30de5462f9ba00149a` |
|  `24.5-dev` `24.5.0-dev`                       | July 1st     | `sha256:ccc9410abd93090918ced4b9688bf1477ee538b186cb2b95a60e5c4c5b52f21d` |
|  `24.1.1`                                      | July 1st     | `sha256:e766405e46ba5f693b27f86de72bbc0b7afd50c4c8a3353243c1220bc2003118` |

