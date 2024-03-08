---
title: "maven Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the maven Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-03-08 00:56:03
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
|  `openjdk-17-dev` `latest-dev` | March 7th    | `sha256:76b40efa677b666a9c59ae87c0f00080673c81b6e89f279912e0f93906922ccd` |
|  `latest` `openjdk-17`         | March 7th    | `sha256:57f678006868e8c0fbbd6a77790e762dc1751ee14efdce1e3074ad5d9296a266` |
|  `openjdk-21`                  | March 7th    | `sha256:af849bff977430a01ad0cc3e9f09d1cf85ea18576ab1d189851f417efd0ccb14` |
|  `openjdk-11-dev`              | March 7th    | `sha256:e330d2d92f1fb5ce187ba8068538f76f26f85ba9b50b8f7b1ed549e03970040f` |
|  `openjdk-11`                  | March 7th    | `sha256:36b2dfd0e38fd15733141154c53bc9483bb42b966681122c9ddfb6e675215223` |
|  `openjdk-21-dev`              | March 7th    | `sha256:8b8bdb0621012d054235cbe620df56be9fd22926c78bc232aad4ead0de0e71b0` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                                       | Last Changed | Digest                                                                    |
|-----------------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` `openjdk-17-3-dev` `openjdk-17-3.9-dev` `openjdk-17-dev` `openjdk-17-3.9.6-dev` | March 7th    | `sha256:72e96639abfd0f28085e74fb0622fd40f9585e1393a1f2eda8c450abf044de68` |
|  `openjdk-21-3` `openjdk-21-3.9.6` `openjdk-21-3.9` `openjdk-21`                              | March 7th    | `sha256:64a6747b1e541702df44b8ad38f45e8c363e6e4e14bb8e0a482c21fd59034d14` |
|  `openjdk-11-3-dev` `openjdk-11-3.9.6-dev` `openjdk-11-dev` `openjdk-11-3.9-dev`              | March 7th    | `sha256:22d2f3397aa01d4bf1a4cda3e6e55da82a7853e39e32ad5c4dd9f7be0536c753` |
|  `openjdk-11-3.9` `openjdk-11-3` `openjdk-11-3.9.6` `openjdk-11`                              | March 7th    | `sha256:c0f9f9abc36669f7d8cbd974ee338a562cb0f13decf1c1819cc933991a1a6880` |
|  `openjdk-21-3-dev` `openjdk-21-3.9.6-dev` `openjdk-21-3.9-dev` `openjdk-21-dev`              | March 7th    | `sha256:c9dc1edb78210e5e996ec3b75bb9e8015eb0cf8a9861f8b74381e68cac34c21a` |
|  `openjdk-17-3` `openjdk-17-3.9.6` `openjdk-17-3.9` `latest` `openjdk-17`                     | March 7th    | `sha256:26aa19c4965545b6bd5b956e4d0b1e9d81db08ffcbd43228d0872c99fac86227` |

