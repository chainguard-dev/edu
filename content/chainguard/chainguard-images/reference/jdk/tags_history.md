---
title: "jdk Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jdk Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-05 17:06:05
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/jdk/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/jdk/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/jdk/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/jdk/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | March 1st    | `sha256:9001f015e4bf5211e39ae66baf168ec75db0c1eee9aba2d9d985069eb6489b95` |
|  `latest`     | March 1st    | `sha256:c11bd3a7bc00b55bb730235d3aa57bb01aba9add4d36ebc2a07754b43e9d66bc` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-8.392.08-dev` `openjdk-8.392-dev` `openjdk-8-dev`                        | March 3rd    | `sha256:2f446325d3daa73c9a61facfcdb075e8af9086782b9fdf95e1f8b3c83706875e` |
|  `openjdk-8.392` `openjdk-8.392.08` `openjdk-8`                                    | March 3rd    | `sha256:c8a658ce036801477daac6aa959509ec49842b401cfea84dd622d67c2e581a5d` |
|  `openjdk-16.0-dev` `openjdk-16-dev` `openjdk-16.0.2.7-dev` `openjdk-16.0.2-dev`   | March 2nd    | `sha256:a5ed70edde373e12540f6a1e67b5f8da8627b9cbb8439b45166b83ba341602eb` |
|  `openjdk-15.0.10.5-dev` `openjdk-15.0.10-dev` `openjdk-15-dev` `openjdk-15.0-dev` | March 2nd    | `sha256:a49fe338eef9372dab5ce1503119604832aabee09081529481acab4516888049` |
|  `openjdk-17-dev` `openjdk-17.0-dev` `openjdk-17.0.10-dev`                         | March 2nd    | `sha256:ee39d9fe6f864118b27d452c65621a5e9ac688a6ca020cbe23265f24dd178404` |
|  `openjdk-11-dev` `openjdk-11.0.22-dev` `openjdk-11.0-dev`                         | March 2nd    | `sha256:5dd843c6755ef6b551ed1c9dc30a717c38379ebd83a0afc3f5b44581993bb46b` |
|  `openjdk-14.0-dev` `openjdk-14.0.2.12-dev` `openjdk-14.0.2-dev` `openjdk-14-dev`  | March 2nd    | `sha256:df2ae1a1485de7465bceb75a2f72851529ca34dce095a2a145b15f67e2de88ff` |
|  `openjdk-21-dev` `openjdk-21.0.2-dev` `openjdk-21.0-dev` `latest-dev`             | March 2nd    | `sha256:a899a135826c48fcb391f69f75f663c40b151765cb07a77d7be024d5c82236e4` |
|  `openjdk-16` `openjdk-16.0` `openjdk-16.0.2.7` `openjdk-16.0.2`                   | March 1st    | `sha256:964ca7554fb7140de7c535dd08adf790d48ec25dcc6664fddfc364b677e9fc6d` |
|  `openjdk-17` `openjdk-17.0.10` `openjdk-17.0`                                     | March 1st    | `sha256:d179405e7efdb760e291c2042493b5741191194bfa78fe9a22b7901c4495181c` |
|  `latest` `openjdk-21` `openjdk-21.0` `openjdk-21.0.2`                             | March 1st    | `sha256:f140aa7b74a7ab59ba28bcf1b3bafa110e8d489cfc7660d92b0ae386fe605602` |
|  `openjdk-14.0.2` `openjdk-14.0.2.12` `openjdk-14.0` `openjdk-14`                  | March 1st    | `sha256:e1782464cc7c04a3334bc25947713b1f0dfe9501683dce6af3ef1e05c9c9b199` |
|  `openjdk-11.0.22` `openjdk-11.0` `openjdk-11`                                     | March 1st    | `sha256:d62589445202abd322997bc026bccb22ccf728193710736ded1084e6e0376a55` |
|  `openjdk-15.0.10.5` `openjdk-15.0.10` `openjdk-15` `openjdk-15.0`                 | March 1st    | `sha256:edf75f890513630fd08f552a2b5de31cc7cf383dabaa3c5ce8db759f871c7069` |

