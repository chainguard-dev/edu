---
title: "jdk Image Tags History"
type: "article"
unlisted: true
description: "Image Tags and History for the jdk Chainguard Image"
date: 2023-06-22T11:07:52+02:00
lastmod: 2024-07-08 00:34:55
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
|  `latest-dev` | July 3rd     | `sha256:d94570946c2c26a6a5efdaae31a2d04e5c997eb6762b80eb63ed5922a42f5136` |
|  `latest`     | July 3rd     | `sha256:c387dbd74f25a9b76f9ad1fcb584dbaa959be1aa464003fa0d05b8013b1aa309` |


### Private/Dedicated Registry
The Private/Dedicated Registry contains our **Production Images**, which include all versioned tags of an image and special images that are not available in the public registry (including FIPS images and other custom builds).

| Tag (s)                                                                            | Last Changed | Digest                                                                    |
|------------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------|
|  `openjdk-11.0.23-dev` `openjdk-11.0-dev` `openjdk-11-dev`                         | July 6th     | `sha256:c4bd7c424a51f50beb6f6e90a8ba4133789a7472f2d1436a64d05ac904087a7a` |
|  `openjdk-15.0.10.5` `openjdk-15` `openjdk-15.0` `openjdk-15.0.10`                 | July 6th     | `sha256:dfa4ebc58681ae6f7ce9dc7615fc45043ed97e88e606ad9840e9d3d1f002bb2f` |
|  `openjdk-17` `openjdk-17.0.11` `openjdk-17.0`                                     | July 6th     | `sha256:ca4036ea5600f5202741e331ac09f9a280c375882182434ce1b9fa609e5896ab` |
|  `openjdk-17.0-dev` `openjdk-17.0.11-dev` `openjdk-17-dev`                         | July 6th     | `sha256:c8e8c5913befe8ad1174fcd092fb713f66ec54aa8470b7602c015c93223527fb` |
|  `openjdk-8.412.08-dev` `openjdk-8-dev` `openjdk-8.412-dev`                        | July 6th     | `sha256:eedba64501dedfb55c80b27b7830cec5dfb8ed41d8013f42a2b1972a8d0f2924` |
|  `openjdk-14-dev` `openjdk-14.0.2.12-dev` `openjdk-14.0-dev` `openjdk-14.0.2-dev`  | July 6th     | `sha256:e1ee267cb03da754c732881b5738a14b829969e188f9fb1cc8225d46850efe5a` |
|  `openjdk-14` `openjdk-14.0.2.12` `openjdk-14.0` `openjdk-14.0.2`                  | July 6th     | `sha256:249874fdecac4b1b779e5e2b55ac7c48c26b875254d9fb47f75e72f49f33b54c` |
|  `openjdk-16.0.2` `openjdk-16` `openjdk-16.0` `openjdk-16.0.2.7`                   | July 6th     | `sha256:bff19fd38832f4e2edaf2eb33f20b4100697b73bc5024ff2b7bebc67b4f48a24` |
|  `openjdk-8` `openjdk-8.412.08` `openjdk-8.412`                                    | July 6th     | `sha256:c440de0d49b06cec55151724289b0bcd90cc7358b5ecf4d33b8a16972da609c7` |
|  `openjdk-11.0` `openjdk-11.0.23` `openjdk-11`                                     | July 6th     | `sha256:f6d19d3af2e366dd1c0d27e0c7702837bf8dd6e65f36c490782ebcd89ae3dc92` |
|  `openjdk-16-dev` `openjdk-16.0-dev` `openjdk-16.0.2.7-dev` `openjdk-16.0.2-dev`   | July 6th     | `sha256:3d33f3d12d91ef734c529668d580308b4b88193347b5e41524d28b7b82e9cc84` |
|  `latest` `openjdk-22.0` `openjdk-22` `openjdk-22.0.1`                             | July 6th     | `sha256:a1766e73c1f9fdb4cfad99afd06db27927f3ad3f92f478b252c8d03dd7106fa3` |
|  `openjdk-21-dev` `openjdk-21.0-dev` `openjdk-21.0.3-dev`                          | July 6th     | `sha256:72ccfc09ff20d89ae6eda00425024c60ed4a10afbaff5fec8a30f10def0a9802` |
|  `openjdk-15.0.10.5-dev` `openjdk-15.0.10-dev` `openjdk-15.0-dev` `openjdk-15-dev` | July 6th     | `sha256:cafc5ef4fc71a306362fbcc552560e0d353a031ee5463d5ca59f39c3b3980c70` |
|  `openjdk-21.0.3` `openjdk-21` `openjdk-21.0`                                      | July 6th     | `sha256:64437ab0c693b87bbdb345f32224e2eb39a7c8811f7444234a65d8d459a159cb` |
|  `openjdk-22.0-dev` `openjdk-22-dev` `openjdk-22.0.1-dev` `latest-dev`             | July 6th     | `sha256:5df05e280b0f39da68df9e468a8f1f9e378b15d3417e8cb266a5ce87304b9392` |

