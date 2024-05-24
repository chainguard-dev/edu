---
title: "dotnet-runtime Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the dotnet-runtime Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-05-24 00:45:45
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/dotnet-runtime/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/dotnet-runtime/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/dotnet-runtime/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/dotnet-runtime/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | May 23rd     | `sha256:278f57742efaf8dce22ef0ba84b91282a0509fed67f753912771ddb92053f817` |
|  `latest`     | May 23rd     | `sha256:bf7367cd4b021f11ce71a771b03ce11ae9727c70966861994bcaca22d5c9b15a` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                     | Last Changed | Digest                                                                    |
|---------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `6.0-dev` `6-dev` `6.0.130-dev`            | May 23rd     | `sha256:b3a527d80a7637ec7a3448a57cd62be30867eadca1f2ce65cf5187bf49d9c15c` |
|  `6.0` `6` `6.0.130`                        | May 23rd     | `sha256:6bb1df5bff427942e72c39e842dc7627ff2faf7904040d09340221a03f90ba98` |
|  `8` `latest` `8.0.5` `8.0`                 | May 23rd     | `sha256:202af99ab252c0cf62be19e0232f0b6e7ef149d1b5d8044db616d4e4f2956e4d` |
|  `8.0-dev` `latest-dev` `8.0.5-dev` `8-dev` | May 23rd     | `sha256:dab2d2e1e28abecbb57b05939e9fe7dfd015561432fc6779174a745053cd1060` |
|  `7.0.119` `7.0` `7`                        | May 23rd     | `sha256:b29f3a03a70b0ec1db80b5e21fc610ba1a1dff3ecf2c0ba908a2f94e895892c3` |
|  `7-dev` `7.0.119-dev` `7.0-dev`            | May 23rd     | `sha256:109d58086d76e1059e9ea961b127f3428fceee69c151ce5d3e125bf01b0f32d9` |
|  `7.0.118-dev`                              | May 15th     | `sha256:8fc1d78b6eaba7551db8828f46e58f77fb14d787cec80b61386a33c30c793f3f` |
|  `7.0.118`                                  | May 15th     | `sha256:9ec31456cd9f5aed58235c42948e3af1efcf2694b0fe0668934c7b59b0030097` |
|  `6.0.129`                                  | May 15th     | `sha256:2280cf528fddc9c475481f0728ca27422c39ce282fb256b8551f05d6dc32387d` |
|  `6.0.129-dev`                              | May 15th     | `sha256:a4e3bbc5b7a2cc593782e4e81ae3d9dd86a8c5eff4ca7f18ce6c11c231c0c7a5` |
|  `8.0.4-dev`                                | May 14th     | `sha256:3039b70e198edaaf5b017cb4133201dc5e9024418457f8b686358168623a9bbb` |
|  `8.0.4`                                    | May 2nd      | `sha256:3d05229ea7be497a75b030bdf12878f35045423c06b53f6b68a37681f03382dd` |
|  `7.0.117`                                  | May 2nd      | `sha256:29577d91f915958270f3a6b2370914275f99a5f8a58548d48a5f75983dd91e50` |
|  `7.0.117-dev`                              | May 2nd      | `sha256:635aab079b1385ebbc9b6b346dd17545daa8767cd43e425959a707d8fe423899` |

