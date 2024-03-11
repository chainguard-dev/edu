---
title: "postgres Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the postgres Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-11 00:52:51
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
|  `latest`     | March 8th    | `sha256:5707d437e5b385ee90d4b9800e5b460373d41b57e63765bb26e91f24e0cc16a9` |
|  `latest-dev` | March 8th    | `sha256:c61e98f3365e648074df1f2c4c46230387ad29c6335374b1930679e9c6751a74` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                           | Last Changed | Digest                                                                    |
|-----------------------------------|--------------|---------------------------------------------------------------------------|
|  `13.14-dev` `13-dev`             | March 10th   | `sha256:d07596dfebec9b0be0a4de64061c575e9f82808996159e870e5752bf13a4c70e` |
|  `14.11-dev` `14-dev`             | March 10th   | `sha256:236e0018faf29e17158dc821cdb455a1b7a786345c988ca4c7502f677991a980` |
|  `12-dev` `12.18-dev`             | March 10th   | `sha256:d753687d56d55616c3585ff0d85d9c6eb3e8c1b189d64139296229a859029f38` |
|  `15-dev` `15.6-dev`              | March 10th   | `sha256:d4f720bf126e7f5147cf1a329cdeb37573525aab304c57056221469f008efa9b` |
|  `latest-dev` `16.2-dev` `16-dev` | March 10th   | `sha256:21fa50e09e1f0178cba066bf654eaa0a74a095bb3d90f6766cc1f7e8aaee67e0` |
|  `15` `15.6`                      | March 8th    | `sha256:3be98095f3e7fb2abaa05e7381b93c979303dfddade5f855e065b44a3d2d0907` |
|  `14` `14.11`                     | March 8th    | `sha256:03824cca3e981141a3de5ca3032d0b1014ab82a55cf46e330a8e992ca09adb15` |
|  `16` `16.2` `latest`             | March 8th    | `sha256:1bae3f65bab3bcb2769c7fcb6938597470189a2cd19b9a67d1b0b5b29eedc001` |
|  `12.18` `12`                     | March 8th    | `sha256:9c3fd279cb6765d272d6e9493cd0514adcb95e2adb2134622214cbbf71e1de32` |
|  `13.14` `13`                     | March 8th    | `sha256:ed72b5d835d708b0e8175d7f88822770562185a5fa98211f7e886b0ec8e25711` |

