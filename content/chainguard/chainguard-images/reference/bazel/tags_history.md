---
title: "bazel Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the bazel Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-03 00:46:08
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
|  `latest-dev` | June 1st     | `sha256:8bd8edd6e0a389ddbb90c00a6b246e0f111fbaf986ccfcb11eeebac6b44aac78` |
|  `latest`     | June 1st     | `sha256:040fde78c717903cfbfcb272d534168962bc3f589b8be562843b6c1654411107` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `6.5-dev` `6.5.0-dev` `6-dev`              | June 1st     | `sha256:89f98db0fec0f65afea6f9cc8ba7788818eea79d68eca140284456b97ab7a0e8` |
|  `5.4-dev` `5-dev` `5.4.1-dev`              | June 1st     | `sha256:cfcf00156e3b045c6ddce90842edeae6ec848ef347d72c0687204f6ab7b25225` |
|  `latest` `7.1.2` `7.1` `7`                 | June 1st     | `sha256:a2b852b893eeb1d2c20039b028d7ab0fac623600c7e09d6ba17db314b009e2fb` |
|  `latest-dev` `7.1-dev` `7.1.2-dev` `7-dev` | June 1st     | `sha256:cac198f6136c742e2e5e79afec28e7444f6a22e08999d3a7da84e66b4602cad7` |
|  `6` `6.5.0` `6.5`                          | June 1st     | `sha256:2146c02a3d940778006dbeda6aef7186ce4fb8ec30163905550d58dec08579aa` |
|  `5.4.1` `5` `5.4`                          | June 1st     | `sha256:c12de5a6584d766edd75fc6e08cb4bfd9005b8129b0d91b7cd7ebf8883f6c2f7` |
|  `7.1.1`                                    | May 9th      | `sha256:14417579783d4513144a3ed611a6b3dbb2c5cc51453ad7c11cf3cdb595d737b2` |
|  `7.1.1-dev`                                | May 9th      | `sha256:cdd252e8dac5c1ceccfa2b49bb2279867f4c5686a559e40122327b9b37a114f7` |
|  `6.2.0`                                    | June 2nd     | `sha256:ba470fbd15c736353c8a3271a141b1dba02238004fbb51e5611a69e29be0950d` |
|  `6.1.2` `6.1`                              | May 22nd     | `sha256:eed2d4f320442b1498ee44dc54efd331844d9e2c7ec1a2ff0458bd2762172d0c` |

