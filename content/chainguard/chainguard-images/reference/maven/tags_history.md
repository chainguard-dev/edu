---
title: "maven Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the maven Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-08 00:34:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 700
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/maven/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/maven/image_specs/" >}}
{{< tab title="Tags History" active=true url="/chainguard/chainguard-images/reference/maven/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/maven/provenance_info/" >}}
{{</ tabs >}}

The following tables contains the most recent tags and digests that can be used to pin your Dockerfile to a specific build of this image. Check our guide on [Using the Tag History API](/chainguard/chainguard-images/using-the-tag-history-api/) for information on how to fetch all tags from an image and how to pin your Dockerfile to a specific digest.

Please note that digests and timestamps only change when there is a change to the image, even though images are rebuilt every night. The "Last Changed" column indicates when the image was last modified, and doesn't always reflect the latest build timestamp. For more information about how our reproducible builds work, please refer to [this blog post](https://www.chainguard.dev/unchained/reproducing-chainguards-reproducible-image-builds).

### Public Registry
The Public Registry contains our **Developer Images**, which typically comprise the `latest*` versions of an image.

| Tag (s)                        | Last Changed | Digest                                                                    |
|--------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-21-dev` `latest-dev` | July 5th     | `sha256:8476600c3d5767c138e84c0cab5819b75a0f778a9a8f79cd6b5fb2051fe4cfbf` |
|  `openjdk-11`                  | July 5th     | `sha256:225723aebccab0372374e38bd3bf825818883114f3399a118b42182591071478` |
|  `openjdk-17`                  | July 5th     | `sha256:4ef7acce2d7fd84b29b5a884f3f7f1cd126bc879572f78f03a431b0b9eea3264` |
|  `latest` `openjdk-21`         | July 5th     | `sha256:2f3d2a8dea0e95d5abe9d2b4847bc178d78045235ac20d86771ec5fa300378ae` |
|  `openjdk-11-dev`              | July 5th     | `sha256:bde4fea5e099cc8e38a466c061dfebe3c6dbcc0f7135375d9a3a99b66a5bdba6` |
|  `openjdk-17-dev`              | July 5th     | `sha256:47526dd81bfb431785deb0cc7cdf5b2917886552d0013a2de2de85c5969525ee` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-21-3.9-dev` `openjdk-21-3-dev` `openjdk-21-dev` `latest-dev` `openjdk-21-3.9.8-dev` | July 6th     | `sha256:e03a35d8d98d4348d3b0c92e6e39fc10c79c361eface19ec5028615107c417c5` |
|  `openjdk-17-3.9.8-dev` `openjdk-17-3-dev` `openjdk-17-dev` `openjdk-17-3.9-dev`              | July 6th     | `sha256:2a433715978538d26d60b6cb3f1d56d7856325e3532a7a4f6196058d9f4bd39a` |
|  `openjdk-11-3.9` `openjdk-11-3.9.8` `openjdk-11` `openjdk-11-3`                              | July 6th     | `sha256:a3d9a2402b78e4927b81b337fcf0b42dfedb42d8703d6aefcb6070baed193036` |
|  `latest` `openjdk-21-3.9` `openjdk-21` `openjdk-21-3` `openjdk-21-3.9.8`                     | July 6th     | `sha256:7f2400dc1716ea55c9ac807cc3f99da12b5c76b30d6ac96c543560b4c7ea7c4a` |
|  `openjdk-17-3` `openjdk-17-3.9.8` `openjdk-17` `openjdk-17-3.9`                              | July 6th     | `sha256:03611f1751f57fc27159e528c296fe81f2765c237ce6a9a02218c4755a9f56ad` |
|  `openjdk-11-3-dev` `openjdk-11-3.9-dev` `openjdk-11-dev` `openjdk-11-3.9.8-dev`              | July 6th     | `sha256:071580bd75b14802e20df620033426b5f73a0362b310eb15df6c948fe7614c03` |

