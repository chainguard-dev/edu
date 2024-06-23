---
title: "bazel Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the bazel Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-23 00:43:06
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/bazel/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/bazel/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/bazel/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/bazel/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | June 21st    | `sha256:d8cff6bb9d18fa11d58aa3c3bfa516d74436d4cd0643aae38c1321705665ed2a` |
|  `latest`     | June 21st    | `sha256:4b233111ee24fb827a09424bc9f77ed1f4f3eca7582f12ce41e2fc251c7362ad` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `7.2` `7.2.0` `7`                 | June 21st    | `sha256:80042429e1abab51214945184b7263386db1895d10aeeacddf0358386afe7a19` |
|  `7.2.0-dev` `7.2-dev` `7-dev` `latest-dev` | June 21st    | `sha256:fff2c25087da999ca0984aaf8bb43fcb69b54e6bdd69825cfda53fc96bcde553` |
|  `6-dev` `6.5.0-dev` `6.5-dev`              | June 21st    | `sha256:c92c8ac96e47579e1f53fd937d807b0ccd3021bae3ea4bf9e4a6040e05ee70a4` |
|  `5` `5.4` `5.4.1`                          | June 21st    | `sha256:af2f5e5234f5b15c92280bbe1b0e09e8a9614d7e88e4ef86080db7dd15b429ac` |
|  `6.5.0` `6` `6.5`                          | June 21st    | `sha256:b8759c355e521964c464a82d007337c1a280d46a3b0598b30715ff0907d67255` |
|  `5.4.1-dev` `5.4-dev` `5-dev`              | June 21st    | `sha256:e7888b8e394fdfdbce42cb759bbcf4515f598d9f36074d967735a2bc580798c4` |

