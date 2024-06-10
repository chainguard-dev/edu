---
title: "postgres Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the postgres Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-06-10 00:50:47
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
|  `latest-dev` | June 9th     | `sha256:ae12bcc07d1ad7251da49c14001d5ee45bcff59251404e802e57f89d6b2ae359` |
|  `latest`     | June 5th     | `sha256:f359eed58238db0c9dc24b791e11b197e997e799eb42455f31099fc1492617e7` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                           | Last Changed | Digest                                                                    |
|-----------------------------------|--------------|---------------------------------------------------------------------------|
|  `12-dev` `12.19-dev`             | June 8th     | `sha256:cb282e89d0639cbf5357fcedf200f631ebcbf365e131f23b2167c74f335424db` |
|  `15.7-dev` `15-dev`              | June 8th     | `sha256:42ee7adb25a6de5feca950b9f5ec5379b00d31143b67ca6a120a5d7ebcc7ea2e` |
|  `16-dev` `16.3-dev` `latest-dev` | June 8th     | `sha256:a82a11b439fda2977435d5aab381b29cafdd9e93ff0b68c1d4d84c00ddaedbb5` |
|  `14.12-dev` `14-dev`             | June 8th     | `sha256:9ce6c411409ef212385ceeee0ba6882b47e2a2ce78924d3ac674dda0bc8af0e3` |
|  `13.15-dev` `13-dev`             | June 8th     | `sha256:34e9dc74ffcdbf2d8b57a52113e228b5ce5e1d8e97306156ea9a3279864f0302` |
|  `15` `15.7`                      | June 5th     | `sha256:75b9bc83c130e0887718b511812345c560b112b5f142bb4b4e76d235f298248c` |
|  `16.3` `latest` `16`             | June 5th     | `sha256:301cb508dcbaa3f6d36b9da3bd132a91af1e82be0d58a3823f74863d70645f9b` |
|  `12.19` `12`                     | June 5th     | `sha256:9249fa250c7b0db868526fe54f6bea67724af3f8f08eb518a0324a503add77b2` |
|  `14.12` `14`                     | June 5th     | `sha256:fe6b82a1ccf0aadadff98cde9a1412cef34ea42ddac2e79d139b9998201b60c0` |
|  `13.15` `13`                     | June 5th     | `sha256:9eaeab77ae2200dae91bc2653c24c5271062a9804a5c045b1f1a7a8fa6777419` |

